import time
import pywinctl as pwc
from services.api_services import (send_app_usage)

from services.api_services import (send_active_data)
from trackers.idle_tracker import (get_input_data)


def extract_title(title):
    
    if "-" in title:
        parts=title.split("-")
    
    
        return parts[-1].strip()
    
    return title


start_time=time.time()



def get_active_window(token):

    global start_time
    previous_window=None
    while True:
        try:

            current_window=pwc.getActiveWindowTitle()
            if current_window:

                if(previous_window!=current_window):
                    title=extract_title(current_window)
                    duration=int(time.time()-start_time)
                 
                    data={
                       "appName":title,
                       "windowTitle":current_window,
                       "duration":duration 
                    }
                    active_data=get_input_data()
                    active_data["activeWindow"]=title
                    print(active_data)
                    send_app_usage(data,token)
                    send_active_data(active_data,token)
                previous_window=current_window
                start_time=time.time()                

            time.sleep(10)

        except Exception as e:
            print (f"error occured!{e}")


