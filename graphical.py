import tkinter as tk
from tkinter import *
import time
import keyboard

def Options():
    if InitialOptions.get() == "Single Key":
        SingleKey = tk.Tk()
        SingleKey.title("Single Key")

        #Key Entry
        SingleKeyChoiseLabel = Label(SingleKey, text="Enter Key")
        SingleKeyChoiseLabel.grid(row=0,column=0)
        SingleKeyChoiseEntry = Entry(SingleKey)
        SingleKeyChoiseEntry.grid(row=0,column=1)

        #Delay
        SingleKeyDelayLabel = Label(SingleKey,text="Enter Delay (in Seconds)")
        SingleKeyDelayLabel.grid(row=1,column=0)
        SingleKeyDelayEntry = Entry(SingleKey)
        SingleKeyDelayEntry.grid(row=1,column=1)

        #Activation/Deactivation Key
        ADKeyLabel = Label(SingleKey, text="Enter key for Activation/Deactivation")
        ADKeyLabel.grid(row=2,column=0)
        ADKeyEntry = Entry(SingleKey)
        ADKeyEntry.grid(row=2, column=1)

        #Process
        def SingleKeyProcess():
            print("On")
            global  status
            status = False

            def onoff(eventtype):
                global status
                status = not bool(status)  # Toggle
                print("On" if status else "Off")


            ADKey = ADKeyEntry.get()
            keyboard.on_press_key(ADKey, onoff)
            while True:
                if status == True:
                    keyboard.press_and_release(SingleKeyChoiseEntry.get())
                    time.sleep(int(SingleKeyDelayEntry.get()))

        #Confirm Choise
        ConfirmSK = Button(SingleKey, text="Confirm", command=SingleKeyProcess)
        ConfirmSK.grid(row=3, column=0)


    elif InitialOptions.get() == "MultiKey":
        Multikey = tk.Tk()
        Multikey.title("Multikey")
    elif InitialOptions.get() == "Hotkey":
        Hotkey = tk.Tk()
        Hotkey.title("Hotkey")


window = tk.Tk()
window.title("Options")


InitialOptions = StringVar()
InitialOptions.set("Single Key")

OptionsDropDown = OptionMenu(window,InitialOptions,"Single Key", "MultiKey", "Hotkey")
OptionsDropDown.pack()
OptionsButton = Button(window, text="Confirm", command=Options)
OptionsButton.pack()

window.mainloop()