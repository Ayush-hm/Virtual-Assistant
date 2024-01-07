from tkinter import *
from script import listen
import tkinter.ttk as ttk
master = Tk()
master.geometry("800x450") 
master['background']='#373f6e'
click_btn= PhotoImage(file='Microphone.png')
b1 = Button(background="#373f6e",activeforeground = "#373f6e", image=click_btn, command=listen())
b1.place(x=300, y=135)
mainloop()