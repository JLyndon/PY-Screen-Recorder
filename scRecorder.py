from tkinter import *
from ctypes import windll
import pyscreenrec as pys

def set_appwindow(mainWindow): # Display the window icon on the taskbar, 

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080

    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

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

