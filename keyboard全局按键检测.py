from pynput import keyboard
def on_press(key):
    print(key)
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
keyboard_listener.join()