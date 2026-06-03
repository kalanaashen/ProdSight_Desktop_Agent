import json
import os


file_name = "app_usage_log.json"


def create_log_entry(details,token):
    
    appname=details.get("appName")
    window_title=details.get("windowTitle")
    duration=details.get("duration")
    date=details.get("date")
    
    if os.path.exists(file_name) and os.path.getsize(file_name)>0:
        with open(file_name,"r") as f:
            data=json.load(f)
    else:
            data=[]
        
        
    entry_found=False
    for log in data:
        if log["appName"]==appname and log["date"]==date:
            log["duration"]+=duration
            entry_found=True
            break
        
    if not entry_found:
        log_entry={
                "appName":appname,
                "windowTitle":window_title,
                "duration":duration,
                
        }
        
        data.append(log_entry)             


    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
