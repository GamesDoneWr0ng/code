from pynput import keyboard

def on_press(key):
    if "char" in dir(key):
        if key.char == "1" or key.char == "0":
            keyboard.Controller().type(", ")

while True:
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()