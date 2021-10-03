import keyboard
import time
import random
import tkinter
from tkinter import ttk
import tkinter.font as font

window = tkinter.Tk(className='Python Word Bomb Cheat!?!?')
window.title('Word Bomb')
window.geometry("800x600")

Font1 = font.Font(family="Arial", size=30)

rand = random.randint(1,30)
def setRandom():
    rand = random.randint(1,100)

def onClick():
    text = Text.get().lower()
    keyboard.wait('insert')
    for i in range(len(text)):
        keyboard.wait('insert')
        keyboard.send(text[i])
    

Text = tkinter.Entry(window,width=100)
WriteText = tkinter.Button(window,text="Write Text",command=onClick,relief=tkinter.GROOVE,padx=250,pady=20,bg="#0000ff",activebackground="#000091",fg="#ffffff",font=Font1)
Label = tkinter.Label(window,text="(to use this, after pressing write text press insert to send a character. Made with python, love & care❤, and with visual studio code (made by edwa)")

Text.grid(row=0,column=0,columnspan=1)
WriteText.grid(row=2,column=0,columnspan=1)
Label.grid(row=1,column=0)

Text.insert(1,"put word here.")
window.mainloop()