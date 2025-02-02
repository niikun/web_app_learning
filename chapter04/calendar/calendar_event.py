import os,json,calendar,re
from datetime import datetime
from flask import Flask,request,render_template,redirect,url_for

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(SCRIPT_DIR,"calendar_events.json")

events = {}
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE,"r") as f:
        events = json.load(f)

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index_get():
    now = datetime.now()
    year = int(request.args.get("year",now.year))
    month = int(request.args.get("month",now.month))

    cal = calendar.Calendar(calendar.MONDAY)
    weeks = cal.monthdayscalendar(year,month)

    next_year = year
    next_month = month + 1

    if next_month > 12:
        next_month = 1
        next_year += 1
    prev_year = year
    prev_month = month - 1
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1

    next_link = f"?year={next_year}&month={next_month}"
    prev_link = f"?year={prev_year}&month={prev_month}"

    return render_template("index.html",
                           weeknames=list("月火水木金土日"),
                           year=year,month=month,
                           weeks=weeks,events=events,
                           next_link=next_link,prev_link=prev_link)

@app.route("/",methods=["POST"])
def index_post():
    date = request.form.get("date","")
    event = request.form.get("event","")
    i = re.match(r"(\d{4})-(\d{2})-\d{2}",date)
    if not i:
        return "日付が不正です"
    year,month = int(i.group(1)),int(i.group(2))

    events[date] = event

    with open(SAVE_FILE,"w") as f:
        json.dump(events,f,ensure_ascii=False,indent=2)
    return redirect(url_for("index_get",year=year,month=month))

if __name__ == "__main__":
    app.run(debug=True)