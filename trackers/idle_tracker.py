import time
from pynput import keyboard
from pynput import mouse


last_active_time=time.time()


keystrokes=0
mouseclicks=0


def update_activity():
    global last_active_time
    last_active_time=time.time()
    
def on_key_press(key):
    global keystrokes
    keystrokes+=1
    update_activity()
    
def on_mouse_click(x,y,button,pressed):
    global mouseclicks
    if pressed:
        mouseclicks+=1
        update_activity()
    
    
    
keyboard_listener=keyboard.Listener(on_press=on_key_press)

mouse_listener=mouse.Listener(on_click=on_mouse_click)

keyboard_listener.start()
mouse_listener.start()


def get_input_data():
    idle_seconds=int(time.time()-last_active_time)
    
    
    return {
        "keystrokes":keystrokes,
        "mouseClicks":mouseclicks,
        "idleSeconds":idle_seconds
    }
    
    
    
    
    
 

 



