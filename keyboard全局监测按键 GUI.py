import sys 
from PyQt5.QtWidgets import QApplication, QLabel
from pynput import keyboard
from threading import Thread

app = QApplication(sys.argv)
label = QLabel()

def on_press(key):
    label.setText(str(key))
    label.adjustSize()

def start_keyboard_listener():
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()

label.show()

keyboard_thread = Thread(target=start_keyboard_listener)
keyboard_thread.start()

sys.exit(app.exec_())