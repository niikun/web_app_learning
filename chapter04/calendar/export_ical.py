import json,datetime

def export_ical(infile:str,outfile:str,debug:bool=False):
    with open(infile,"r")as f:
        events = json.load(f)

    ical = []
    for (date,event) in events.items():
        d = datetime.datetime.strptime(date,"%Y-%m-%d")
        date_ical = d.strftime("%Y%m%d")
        ical.append(f"BEGIN:VEVENT")
        ical.append(f"DTSTART;VALUE=DATE:{date_ical}")
        ical.append(f"DTEND;VALUE=DATE:{date_ical}")
        ical.append(f"SUMMARY:{event}")
        ical.append(f"END:VEVENT")
    ical.insert(0,"BEGIN:VCALENDAR")
    ical.insert(1,"VERSION:2.0")
    ical.insert(2,"PRODID: calendar_events")
    ical.append("END:VCALENDAR")

    with open(outfile,"w") as f:
        f.write("\r\n".join(ical))

    if debug:
        print("\r\n".join(ical))

if __name__ == "__main__":
    INFILE = "calendar_events.json"
    OUTFILE = "calendar_events.ical"
    export_ical(INFILE,OUTFILE,debug=True)