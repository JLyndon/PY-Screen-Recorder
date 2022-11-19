from tkinter import *
import pyscreenrec as pys

winTitle = "Screen Recorder" # Window Title

mainBox = Tk() # Main Window
mainBox.title(winTitle) 
mainBox.overrideredirect(True) # Removes title bar
mainBox.geometry('700x200+75+75')
mainBox.resizable(False, False)


Gray = '#3e4042' # Hex Color Codes
dGray = '#25292e' 
rGray = '#10121f' 

mainBox.config(bg="#25292e")

title_bar = Frame(mainBox, bg=rGray, relief='raised', bd=0, highlightthickness=0)

mainBox.mainloop()

