import json
from services.api_services import send_active_data
from datetime import datetime
import os

json_file="active_data_log.json"



def  _get_log_date(date_value):
    if not date_value:
        return datetime.now().date().isoformat()

    try:
        return datetime.fromisoformat(date_value).date().isoformat()
    except ValueError:
        return date_value
    
    
def create_active_log_entry(data,token):
    
    
    active_window = data.get("activeWindow")
    duration = int(data.get("duration") or 0)
    date = _get_log_date(data.get("date"))
    keystrokes = int(data.get("keystrokes") or 0)
    mouse_clicks = int(data.get("mouseClicks") or 0)
    idle_seconds = int(data.get("idleSeconds") or 0)

    if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
        with open(json_file, "r") as f:
            log_data = json.load(f)
    else:
        log_data = []

    log_entry = None
    for log in log_data:
        if (
            log.get("activeWindow") == active_window
            and log.get("date") == date
        ):
            log["duration"] = int(log.get("duration") or 0) + duration
            log["keystrokes"] = int(log.get("keystrokes") or 0) + keystrokes
            log["mouseClicks"] = int(log.get("mouseClicks") or 0) + mouse_clicks
            log["idleSeconds"] = int(log.get("idleSeconds") or 0) + idle_seconds
            log_entry = log
            break

    if log_entry is None:
        log_entry = {
            "activeWindow": active_window,
            "duration": duration,
            "date": date,
            "keystrokes": keystrokes,
            "mouseClicks": mouse_clicks,
            "idleSeconds": idle_seconds,
        }
        log_data.append(log_entry)

    with open(json_file, "w") as f:
        json.dump(log_data, f, indent=4)

    send_active_data(log_entry, token)
