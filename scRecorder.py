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

def minimize_me():
    mainBox.attributes("-alpha",0) # so you can't see the window when is minimized
    mainBox.minimized = True       

def deminimize(event):
    mainBox.focus() 
    mainBox.attributes("-alpha",1) # so you can see the window when is not minimized
    if mainBox.minimized == True:
        mainBox.minimized = False                              
        
def maximize_me():
    if mainBox.maximized == False: # if the window was not maximized
        mainBox.normal_size = mainBox.geometry()
        expand_button.config(text=" 🗗 ")
        mainBox.geometry(f"{mainBox.winfo_screenwidth()}x{mainBox.winfo_screenheight()}+0+0")
        mainBox.maximized = not mainBox.maximized 
        
    else: # if the window was maximized
        expand_button.config(text=" 🗖 ")
        mainBox.geometry(mainBox.normal_size)
        mainBox.maximized = not mainBox.maximized
        # now it is not maximized

# ---------- Main Config -----------

winTitle = "Screen Recorder" # Window Title

mainBox = Tk() # Main Window
mainBox.title(winTitle) 
mainBox.overrideredirect(True) # Removes title bar
mainBox.geometry('700x200+75+75')
mainBox.resizable(False, False)
mainBox.minimized = False
mainBox.maximized = False


Gray = '#3e4042' # Hex Color Codes
dGray = '#373940' 
rGray = '#232530' 

mainBox.config(bg="#25292e")

title_bar = Frame(mainBox, bg=rGray, relief='raised', bd=0, highlightthickness=0)

close_button = Button(title_bar, text='  ×  ', command=mainBox.destroy,bg=rGray,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=rGray,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=rGray,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
title_bar_title = Label(title_bar, text=winTitle, bg=rGray,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

mainBox.mainloop()

