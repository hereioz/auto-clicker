from tkinter import messagebox
import tkinter
import time


messagebox.showinfo("by hereioz","this simple project created by hereioz.\n\ninstagram: https://instagram.com/hereioz\ngithub: https://github.com/hereioz")


try:
    open("settings.txt",'r')
except:
    messagebox.showerror("ERROR!","Misssing settings.txt file!\nquitting..") 
    time.sleep(0.75)
    exit(0)

try:
    import GUI
except:
    messagebox.showerror("ERROR!","Missing GUI.py file!\nquitting..") 
    time.sleep(0.75)
    exit(0)

try:
    import auto_clicker
except:
    messagebox.showerror("ERROR!","Missing auto_clicker.py file!\nquitting..")
    time.sleep(0.75)
    exit(0)


GUI.main()