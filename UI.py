import tkinter as tk
import URLFileRead
import requests
from requests.auth import HTTPBasicAuth
from string import *
# from pynput.keyboard import Key, Listener,Controller
# import pyautogui
from tkinter import *
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(100, count)
    count()
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
def callback():
    print ("click!")
    respons=str(requests.get('https://mon.qcluster.org'))
    if("[200]" in respons):
        print("thats ok")

    print(respons)
    print("sdfs")
button = tk.Button(root, text='Stop', width=25, command=callback)
button.pack()
root.mainloop()