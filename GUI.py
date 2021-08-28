from tkinter import messagebox
import tkinter
from tkinter import *
from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Button
import threading,sys

with open("settings.txt",'r') as f:
    settings = f.readlines()
    start_stop_key = settings[0].split("=")[1]
    exit_key = settings[1].split("=")[1]
    button = settings[2].split("=")[1]
    delay = settings[3].split("=")[1]
f.close()

class listener_command:
    def __init__(self):
        pass

    def listener_start(self):
        global delay,button,button_click
        with open("settings.txt",'r') as f:
            settings = f.readlines()
            start_stop_key = settings[0].split("=")[1]
            exit_key = settings[1].split("=")[1]
            button = settings[2].split("=")[1]
            delay = settings[3].split("=")[1]
        f.close()

        if (button_click.get() == 1):
            button = Button.left
        elif (button_click.get() == 2):
            button = Button.right

        try:
            delay = float(DELAY_entry.get())
            if (len(str(delay)) <= 0):
                messagebox.showerror("ERROR!","PLEASE ENTER A VALID DELAY")
                return 0
        except:
            messagebox.showerror("ERROR!","PLEASE ENTER A VALID DELAY")
            return 0

        with open("settings.txt",'w') as f:
            f.write(f"start_stop_key={str(start_stop_key).strip()}\nexit_key={str(exit_key).strip()}\nbutton={str(button).strip()}\ndelay={str(delay).strip()}")
        f.close()
        import auto_clicker
        threading.Thread(target=auto_clicker.main).start()
        start_listener.config(state=DISABLED)
        DELAY_entry.config(state=DISABLED)
        left_click.config(state=DISABLED)
        right_click.config(state=DISABLED)
        key_stroke_record.config(state=DISABLED)

    def if_listener_stop(self):
        start_listener.config(state=NORMAL)
        DELAY_entry.config(state=NORMAL)
        left_click.config(state=NORMAL)
        right_click.config(state=NORMAL)
        key_stroke_record.config(state=NORMAL)
        messagebox.showinfo("ATTENTION!","LISTENER STOPPED!")
    
class key_stroke_command:
    def __init__(self):
        pass

    def key_stroke_start_recording(self):
        threading.Thread(target=key_stroke_command().key_stroke_recording).start()

    def key_stroke_recording(self):
        global start_stop_key
        key_stroke_record.config(state=DISABLED)
        def on_press(key):
            if ("Key." not in str(key)):
                KEY = str(key)[1]
            if ("Key." in str(key)):
                KEY = str(key).split(".")[1]
            with open("settings.txt",'r') as f:
                settings = f.readlines()
                start_stop_key = settings[0].split("=")[1]
                exit_key = settings[1].split("=")[1]
                button = settings[2].split("=")[1]
                delay = settings[3].split("=")[1]
            f.close()
            start_stop_key = KEY
            with open("settings.txt",'w') as f:
                f.write(f"start_stop_key={start_stop_key.strip()}\nexit_key={exit_key.strip()}\nbutton={button.strip()}\ndelay={delay.strip()}")
            f.close()
            current_key_stroke_listener.config(text=f"YOUR CURRENT KEYSTROKE: {str(start_stop_key).upper()}")
            key_stroke_record.config(state=NORMAL)
            exit(0)

        with Listener(on_press=on_press) as listener:
            listener.join()
    
class other_command:
    def __init__(self):
        pass

    def kill_process(self):
        import os,psutil
        proc = psutil.Process(os.getpid())
        proc.kill()

        
def main():
    global start_listener,main_window,current_key_stroke_listener,key_stroke_record,DELAY_entry,button_click,left_click,right_click
    main_window = tkinter.Tk()
    main_window.title("AUTO CLICKER")
    main_window.geometry("400x400")
    main_window.config(background="black")
    main_window.resizable(False, False)
    button_click = IntVar()
    main_window.protocol("WM_DELETE_WINDOW", other_command().kill_process)

    c = Canvas(main_window, bg="gray16",height=1000,width=600)
    filename = PhotoImage(file="//root//Downloads//photo-1538481199705-c710c4e965fc.png")
    background_layer = Label(main_window, image=filename)
    background_layer.place(x=0, y=0, relwidth=1, relheight=1)
    current_key_stroke_listener = tkinter.Label(main_window, text=f"YOUR CURRENT KEYSTROKE: {str(start_stop_key).upper()}",fg="white", bg="black", font=("1"))
    current_key_stroke_listener.place(x=75,y=300)

    current_key_stroke_stop = tkinter.Label(main_window, text=f"YOUR CURRENT SHUTDOWN LISTENER KEYSTROKE: {str(exit_key).upper()}",fg="white", bg="black")
    current_key_stroke_stop.place(x=25, y=260)

    start_listener = tkinter.Button(main_window,width=20,height=2, text="START LISTENER",fg="white", bg="black",activeforeground="white", activebackground="#704685", command=listener_command().listener_start)
    start_listener.place(x=7, y=343)

    key_stroke_record = tkinter.Button(main_window,width=20, height=2, text="RECORD KEYSTROKES",fg="white", bg="black",activeforeground="white", activebackground="#704685", command=key_stroke_command().key_stroke_start_recording)
    key_stroke_record.place(x=205, y=343)

    DELAY_label = tkinter.Label(main_window, text="DELAY", font=("1"), fg="white", bg="black")
    DELAY_label.config(background="#87CEFA")
    DELAY_label.place(x=5, y=50)

    DELAY_entry = tkinter.Entry(main_window,width=10)
    DELAY_entry.insert(0,delay)
    DELAY_entry.place(x=5, y=75)

    if (button.strip() == "Button.right"):
        button_click.set(2)
    elif (button.strip() == "Button.left"):
        button_click.set(1)

    left_click = tkinter.Radiobutton(main_window,width=11, text="LEFT CLICK",selectcolor="black", variable=button_click, value=1, fg="white", bg="black",activeforeground="white", activebackground="#704685")
    left_click.place(x=275, y=93)
    
    right_click = tkinter.Radiobutton(main_window,width=11, text="RIGHT CLICK",selectcolor="black", variable=button_click, value=2, fg="white", bg="black",activeforeground="white", activebackground="#704685")
    right_click.place(x=275, y=70)


    try:
        main_window.mainloop()
    except KeyboardInterrupt:
        print("EXITING...")
        main_window.destroy()
        exit(0)
