from tkinter import *
from ctypes import windll
from datetime import datetime
import pyscreenrec as pys

Gray = '#3e4042' # Hex Color Codes
dGray = '#373940' 
rGray = '#232530' 


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

# ---------- Additional Functions for Widgets and Window Behavior --------------------

def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'
    
    
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=rGray
    

def change_size_on_hovering(event):
    global expand_button
    expand_button['bg']=Gray
    
    
def return_size_on_hovering(event):
    global expand_button
    expand_button['bg']=rGray
    

def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=Gray
    
    
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']= rGray
    

def get_pos(event): # This is to be run if the User decides to move the App Window
    if mainBox.maximized == False:
 
        xwin = mainBox.winfo_x()
        ywin = mainBox.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event): # Execute when window is dragged
            mainBox.config(cursor="fleur")
            mainBox.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


        def release_window(event): # Execute when window is released
            mainBox.config(cursor="arrow")
            
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        mainBox.maximized = not mainBox.maximized

# ---------- Functions for Screen Recording ------------

def start_record():
    fileN = usrFile.get()
    comName = str(fileN + ".mp4")
    scRecord.start_recording(comName, 30)

def pause_record():
    scRecord.pause_recording()

def resume_record():
    scRecord.resume_recording()

def stop_record():
    scRecord.stop_recording()


# ---------- Main Config for Windows -----------

winTitle = "Screen Recorder" # Window Title

mainBox = Tk() # Window
mainBox.title(winTitle) 
mainBox.overrideredirect(True) # Removes title bar
mainBox.geometry('700x150+75+75') # Window Dimensions
mainBox.resizable(False, False)   # Fixed --> Not resizable
mainBox.minimized = False
mainBox.maximized = False
mainBox.config(bg="#25292e")

scRecord = pys.ScreenRecorder()

title_bar = Frame(mainBox, bg=rGray, relief='raised', bd=0, highlightthickness=0)

# Buttons for the Title Bar
close_button = Button(title_bar, text='  ×  ', command=mainBox.destroy,bg=rGray,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=rGray,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=rGray,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
title_bar_title = Label(title_bar, text=winTitle, bg=rGray,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

window = Frame(mainBox, bg=dGray, highlightthickness=0)

# Fitting the Widgets/Buttons
title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=7,ipady=1)
expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
window.pack(expand=1, fill=BOTH)

title_bar.bind('<Button-1>', get_pos) # For dragging window
title_bar_title.bind('<Button-1>', get_pos)

# Button Effects
close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
expand_button.bind('<Enter>', change_size_on_hovering)
expand_button.bind('<Leave>', return_size_on_hovering)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)

mainBox.bind("<FocusIn>",deminimize)
mainBox.after(10, lambda: set_appwindow(mainBox))

# --------------- Screen Recorder Code -----------------

firstbutton = PhotoImage(file="Start_Button.png")
startBtn = Button(mainBox, image=firstbutton, bd=0, bg=dGray, width=80, height=80, activebackground=dGray, command=start_record)
startBtn.place(x=45, y=48)

secbutton = PhotoImage(file="Resume_Buttonsmall.png")
resumeBtn = Button(mainBox, image=secbutton, bd=0, bg=dGray, width=55, height=55, activebackground=dGray, command=resume_record)
resumeBtn.place(x=165, y=56)

label1 = Label(mainBox, text="Resume", bg=dGray, font="calibri 12", fg="#6A757E")
label1.place(x=165, y=111)

thrbutton = PhotoImage(file="Pause_Buttonsmall.png")
pauseBtn = Button(mainBox, image=thrbutton, bd=0, bg=dGray, width=55, height=55, activebackground=dGray, command=pause_record)
pauseBtn.place(x=240, y=56)

label2 = Label(mainBox, text="Pause", bg=dGray, font="calibri 12", fg="#6A757E")
label2.place(x=245, y=111)

frbutton = PhotoImage(file="Stop_Buttonsmall.png")
pauseBtn = Button(mainBox, image=frbutton, bd=0, bg=dGray, width=55, height=55, activebackground=dGray, command=stop_record)
pauseBtn.place(x=315, y=56)

label3 = Label(mainBox, text="Stop", bg=dGray, font="calibri 12", fg="#6A757E")
label3.place(x=325, y=111)


timeOfSave = datetime.now()
tempSaveName = " recording_" + timeOfSave.strftime("%d-%m-%Y_%H-%M-%S")

usrFile = StringVar()
saveFile = Entry(mainBox, textvariable=usrFile, width=20, font="arial 11", background="#6f6f6f", fg="#fff")
saveFile.place(x=420, y=75)
usrFile.set(tempSaveName)

labelsave = Label(mainBox, text="Filename", bg=dGray, font="calibri 12", fg="#6A757E")
labelsave.place(x=425, y=50)

mainBox.mainloop()

