import json
import os
from datetime import datetime
from services.api_services import send_app_usage

file_name = "app_usage_log.json"


def _get_log_date(date_value):
    if not date_value:
        return datetime.now().date().isoformat()

    try:
        return datetime.fromisoformat(date_value).date().isoformat()
    except ValueError:
        return date_value


def create_log_entry(details, token):
    appname = details.get("appName")
    window_title = details.get("windowTitle")
    duration = int(details.get("duration") or 0)
    date = _get_log_date(details.get("date"))

    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, "r") as f:
            data = json.load(f)
    else:
        data = []

    log_entry = None
    for log in data:
        if (
            log.get("appName") == appname
            and log.get("windowTitle") == window_title
            and log.get("date") == date
        ):
            log["duration"] = int(log.get("duration") or 0) + duration
            log_entry = log
            break

    if log_entry is None:
        log_entry = {
            "appName": appname,
            "windowTitle": window_title,
            "duration": duration,
            "date": date,
        }
        data.append(log_entry)


    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

    send_app_usage(log_entry, token)
