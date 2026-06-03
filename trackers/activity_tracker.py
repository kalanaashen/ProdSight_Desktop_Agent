import time
from datetime import datetime
import pywinctl as pwc
from data.apptracker import create_log_entry
from services.api_services import (
    send_active_data,
)
from trackers.idle_tracker import get_input_data


def extract_title(title):
    if not title:
        return "Unknown"

    if "-" in title:
        parts = title.split("-")
        return parts[-1].strip()

    return title


def get_active_window(token):
    app_start_time = time.time()
    last_activity_time = time.time()
    previous_window = None

    while True:
        try:
            current_window = pwc.getActiveWindowTitle()
            current_time = time.time()

            if previous_window is None:
                previous_window = current_window
                app_start_time = current_time

            elif previous_window != current_window:
                title = extract_title(previous_window)
                duration = int(current_time - app_start_time)

                data = {
                    "appName": title,
                    "windowTitle": previous_window,
                    "duration": duration,
                    "date":datetime.now().isoformat()
                }

                create_log_entry(data, token)
                previous_window = current_window
                app_start_time = current_time

            if current_time - last_activity_time > 60:
                active_data = get_input_data()
                active_data["activeWindow"] = extract_title(current_window)
                active_data["duration"] = int(current_time - app_start_time)

                send_active_data(active_data, token)
                print(active_data)

                last_activity_time = current_time

            time.sleep(2)

        except Exception as e:
            print(f"error occured! {e}")
