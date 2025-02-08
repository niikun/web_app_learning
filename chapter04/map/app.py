import os
from flask import Flask,redirect,url_for,render_template,request
import plot_temp

SROIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MAP_HTML = os.path.join(SROIPT_DIR,"static", "map.html")

app = Flask(__name__)

@app.route("/")
def index():
    if os.path.exsits(MAP_HTML):
        st = os.stat(MAP_HTML)
        if st.st_mtime + 3600 < time.time():
            plot_temp.save_weather_map(MAP_HTML)
    else:
        plot_temp.save_weather_map(MAP_HTML)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)