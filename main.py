import pyautogui as ss
import time as t
import os
import random
import tkinter as tk
from threading import Thread

def takess(delay):
    def capture_screenshot(delay):
        r = random.random()
        r = str(r)
        x, y = r.split(".")
        
        if not os.path.exists("Saved Screenshots"):
            os.makedirs("Saved Screenshots")
        
        if delay == "":
            t.sleep(3)
        else:
            t.sleep(int(delay))
        
        img = ss.screenshot(f"Saved Screenshots/img{y}.png")
        img.show()
    # Create and start a new thread for the screenshot process
    #i have created this cause i get introduced by a bug my gui stops if i use this func but i dont want this so using threading
    
    
    screenshot_thread = Thread(target=capture_screenshot, args=(delay,))
    screenshot_thread.start()

def gui():
    root = tk.Tk()
    root.geometry("500x500")
    root.title('Screenshot app')
    
    delay = tk.StringVar()
 
    canvas = tk.Canvas(
        root,
        bg = "#2148C0",
        height=495,
        width=495,
        bd=5,
        relief="groove"
    )
    canvas.place(x=0, y=0)
    canvas.create_text(250, 30, text="ScreenShot App", fill="#FFFFFF",
                       font=("HammersmithOne Regular", 30), justify="center")
    
    frame = tk.Frame(canvas, height=30, width=200, background="#2148C0")
    label = tk.Label(frame, text="Enter time of Delay:", background="#2148C0",
                     font=("Roboto", 10, "bold"), fg="WHITE")
                     
    label.grid(row=0, column=0)
    frame.place(x=80, y=100)
    entry = tk.Entry(frame, insertbackground="WHITE", textvariable=delay)
    entry.grid(row=0, column=1)
    
    button = tk.Button(canvas, text="Take ScreenShot", command=lambda: takess(entry.get()))
    button.place(x=100, y=150)
    button2 = tk.Button(canvas, text="Minimize Screen", command=root.iconify)
    button2.place(x=300, y=150)
    
    root.resizable(False, False)
    
    root.mainloop()

def main():
    gui()

main()
