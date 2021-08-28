import time
import threading,sys
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import GUI

delay = float(GUI.delay)

if (GUI.button.strip() == "Button.left"):
    button = Button.left
elif (GUI.button.strip() == "Button.right"):
    button = Button.right

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


def main():
    global mouse
    mouse = Controller()
    click_thread = ClickMouse(delay, button)
    click_thread.start()


    def on_press(key):
        if ("Key." not in str(key)):
            KEY = str(key)[1]
        if ("Key." in str(key)):
            KEY = str(key).split(".")[1]
        if str(KEY) == str(GUI.start_stop_key).strip() or str(KEY) == str(GUI.start_stop_key).strip().upper():
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif str(KEY) == str(GUI.exit_key).strip() or str(KEY) == str(GUI.exit_key).strip().upper():
            GUI.listener_command().if_listener_stop()
            click_thread.exit()
            listener.stop()


    with Listener(on_press=on_press) as listener:
        listener.join()
