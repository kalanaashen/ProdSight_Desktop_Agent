import time
import pywinctl as pwc


def get_active_window():

    while True:
        try:
            previous_window=None


            current_window=pwc.getActiveWindowTitle()
            if current_window:

                if(previous_window!=current_window):

                    print(f"Current Window is {current_window}")

                previous_window=current_window


            time.sleep(10)

        except Exception as e:
            print (f"error occured!{e}")


get_active_window()