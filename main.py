from matplotlib.figure import Figure
from Utils import analyze,process,global_constants
import threading
import multiprocessing
import random
import tkinter as tk
from tkinter.constants import HORIZONTAL
from tkinter import Button, messagebox
import tkinter.font as tkFont
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib import style
from matplotlib import animation
import matplotlib.pyplot as plt
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

"""
    Instructions for developing 

    initially it only work for start+Logs+help
    for Page2 ie View page -> add Page in frames List (in developing face have some issues)
"""

style.use("ggplot")


def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))
global xGlobal, yGlobal
xGlobal = []
yGlobal = []

BACK1 = "#3E8E7E"
BACK2 = "#7CD1B8"
FONT_COLOR1 = "#00ADB5"
FONT_COLOR2 = "#EBE645"
FONT_COLOR3 = ""
BUTTON_COLOR1 = "#577BC1"
BUTTON_COLOR2 = ""

LARGEFONT =("Verdana", 35)

f = Figure(figsize=(1,1),dpi=100)
a = f.add_subplot(111)

def animate(i):
    # pullData = open("sampleText.txt","r").read()
    # dataList = pullData.split('\n')
    xList = xGlobal
    yList = yGlobal
    # for eachLine in dataList:
    #     if len(eachLine) > 1:
    #         x, y = eachLine.split(',')
    #         xList.append(int(x))
    #         yList.append(int(y))

    a.clear()
    a.plot(xList, yList)


class App(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (FirstDisplay,FApp, Page1, Page2, Page3, Page4):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(FirstDisplay)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class FirstDisplay(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        btnPlacex = 260
        btnPlacey = 400

        def next(event):
            import time
            progress.place(x=btnPlacex-120,y=btnPlacey)
            event.place_forget()
            hide.place(x=btnPlacex-40,y=btnPlacey,width=150,height=150)
            progress['value']=20
            self.update_idletasks()
            time.sleep(1)
            progress['value']=50
            self.update_idletasks()
            time.sleep(1)
            progress['value']=80
            self.update_idletasks()
            time.sleep(1)
            progress['value']=100
            controller.show_frame(FApp)

        GLabel_40=tk.Label(self)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_40["font"] = ft
        GLabel_40["fg"] = FONT_COLOR2
        GLabel_40["bg"] = "#222831"
        GLabel_40["justify"] = "center"
        GLabel_40.place(width=600,height=500)

        Title = tk.Label(self)
        Title["fg"] = "#EEEEEE"
        Title["bg"] = "#393E46"
        Title["text"] = "SCOUTTING-SNIFFER"
        Title["font"] = tkFont.Font(size=20)
        Title.place(x=100,y=100,width=400,height=200)

        hide = tk.Label(self)
        hide["bg"] = "#222831"
        
        progress = Progressbar(self,orient=HORIZONTAL,length=300,mode="determinate")
        btn = Button(self,text='START',command=lambda :next(btn), activebackground="#08D9D6",activeforeground="#EEEEEE")
        btn["bg"] = "#00ADB5"
        btn["fg"] = "#EEEEEE"
        btn["border"] = "0"
        btn["font"] = tkFont.Font(size=20)
        changeOnHover(btn,"#08D9D6","#00ADB5")
        btn.place(x=btnPlacex-40,y=btnPlacey,height=50,width=150)  

# first window frame startpage
class FApp(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.config(background="#222831")
        
        def start_protocols():
            if analyze.__Check__():
                messagebox.showerror("Error", "You caught!!!!")
                with open("mytextLogs.txt") as f:
                    #to write in log file I will decide it later 
                    pass
                controller.show_frame(Page2)

        def start():

            messagebox.showinfo("showinfo", "We are start monitoring your computer now you are safe")
            thread1 = threading.Thread(target=controller.show_frame,args=(Page1,))
            thread2 = threading.Thread(target=start_protocols)
            thread1.start()
            thread2.start()
        
        def proc():
            i = 1
            while True:
                yGlobal.append(process.__TCPpacketFreq__(global_constants.TIME,global_constants.T4))
                xGlobal.append(i)
                i = i+1


                    

        def start1():
            thread3 = threading.Thread(target=lambda : controller.show_frame(Page2))
            thread4 = threading.Thread(target=proc) 
            thread3.start()
            thread4.start()


        GLabel_50=tk.Label(self)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_50["font"] = ft
        GLabel_50["fg"] = "#FFFFFF"
        GLabel_50["bg"] = "#393E46"
        GLabel_50["justify"] = "center"
        GLabel_50.place(x=0,y=90,width=600,height=250)

        GButton_342=tk.Button(self,activebackground="#F05454",activeforeground="#EEEEEE")
        GButton_342["bg"] = "#F05454"
        ft = tkFont.Font(family='Times',size=18)
        GButton_342["font"] = ft
        GButton_342["fg"] = "#EEEEEE"
        GButton_342["justify"] = "center"
        GButton_342["border"] = "0"
        GButton_342["text"] = "RUN"
        GButton_342.place(x=225,y=120,width=150,height=45)
        GButton_342["command"] = start

        GButton_521=tk.Button(self,activebackground="#B958A5",activeforeground="#EEEEEE")
        GButton_521["bg"] = "#B958A5"
        ft = tkFont.Font(family='Times',size=18)
        GButton_521["font"] = ft
        GButton_521["fg"] = "#EEEEEE"
        GButton_521["justify"] = "center"
        GButton_521["border"] = "0"
        GButton_521["text"] = "VIEW"
        GButton_521.place(x=225,y=170,width=150,height=45)
        GButton_521["command"] = start1

        GButton_645=tk.Button(self,activebackground="#EC255A",activeforeground="#EEEEEE")
        GButton_645["bg"] = "#EC255A"
        ft = tkFont.Font(family='Times',size=18)
        GButton_645["font"] = ft
        GButton_645["fg"] = "#EEEEEE"
        GButton_645["justify"] = "center"
        GButton_645["border"] = "0"
        GButton_645["text"] = "LOGS"
        GButton_645.place(x=225,y=220,width=150,height=45)
        GButton_645["command"] = lambda : controller.show_frame(Page3)

        GButton_644=tk.Button(self,activebackground="#4C0070",activeforeground="#EEEEEE")
        GButton_644["bg"] = "#4C0070"
        ft = tkFont.Font(family='Times',size=18)
        GButton_644["font"] = ft
        GButton_644["fg"] = "#EEEEEE"
        GButton_644["justify"] = "center"
        GButton_644["border"] = "0"
        GButton_644["text"] = "HELP"
        GButton_644.place(x=225,y=270,width=150,height=45)
        GButton_644["command"] = lambda : controller.show_frame(Page4)

        changeOnHover(GButton_644,"#4C3F91","#4C0070")
        changeOnHover(GButton_645,"#F14668","#EC255A")
        changeOnHover(GButton_521,"#C996CC","#B958A5")
        changeOnHover(GButton_342,"#FF6B6B","#F05454")


        

# second window frame page1
class Page1(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.config(background="#222831")

        def back():
            a = messagebox.askquestion("Info","we will keep you safe you can go elsewhere")
            if a == "yes":
                controller.show_frame(FApp)
        

        GButton_112=tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        GButton_112["bg"] = "#08D9D6"
        ft = tkFont.Font(family='Times',size=10)
        GButton_112["font"] = ft
        GButton_112["fg"] = "#EEEEEE"
        GButton_112["justify"] = "center"
        GButton_112["text"] = "Back"
        GButton_112["border"] = "0"
        GButton_112.place(x=20,y=460,width=70,height=25)
        GButton_112["command"] = back

        GLabel_847=tk.Label(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        ft = tkFont.Font(family='Times',size=30)
        GLabel_847["font"] = ft
        GLabel_847["fg"] = "#EEEEEE"
        GLabel_847["bg"] = "#393E46"
        GLabel_847["justify"] = "center"
        GLabel_847["text"] = "You are now safe."
        GLabel_847.place(x=50,y=40,width=493,height=320)

        changeOnHover(GButton_112,"#08D9D6","#00ADB5")


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame(FApp)
        
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        LabelP21 = tk.Label(self)
        LabelP21["text"] = "Current status of TCP packet frequency"
        LabelP21["fg"] = "#EEEEEE"
        LabelP21["bg"] = "#393E46"
        LabelP21["font"] = tkFont.Font(size=15)
        LabelP21.place(x=80,y=20)

        GButton_11=tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        GButton_11["bg"] = "#08D9D6"
        ft = tkFont.Font(family='Times',size=10)
        GButton_11["font"] = ft
        GButton_11["fg"] = "#EEEEEE"
        GButton_11["justify"] = "center"
        GButton_11["text"] = "Back"
        GButton_11["border"] = "0"
        GButton_11.place(x=20,y=460,width=70,height=25)
        GButton_11["command"] = back

        changeOnHover(GButton_11,"#08D9D6","#00ADB5")

        toolbar = NavigationToolbar2Tk( canvas, self )
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        
        

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background="#393E46")
        def back():
            controller.show_frame(FApp)
        
        LabelP31 = tk.Label(self)
        LabelP31["text"] = "System Logs"
        LabelP31["bg"] = "#393E46"
        LabelP31["font"] = tkFont.Font(size=20)
        LabelP31["fg"] = "#EEEEEE"
        LabelP31.place(x=220,y=10)
        
        a = open(file="D:\pmmp\scouting-sniffer\mytextLogs.txt")
        b = a.read()
        textArea = tk.Text(self)
        textArea.insert(tk.END,b)
        textArea.place(x=45,y=50,height=400,width=500)

        ButtonP3 = tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        ButtonP3["text"] = "Back"
        ButtonP3["bg"] = "#00ADB5"
        ButtonP3["fg"] = "#EEEEEE"
        ButtonP3["command"] = back
        ButtonP3["border"] = "0"
        ButtonP3.place(x=20,y=460,width=70,height=25)

        changeOnHover(ButtonP3,"#08D9D6","#00ADB5")

        



class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background="#222831")
        def back():
            controller.show_frame(FApp)
        
        LabelP41 = tk.Label(self)
        LabelP41["text"] = "Feeling confused? Dont worry! we are here to help you out"
        LabelP41["fg"] = "#EEEEEE"
        LabelP41["bg"] = "#393E46"
        LabelP41["font"] = tkFont.Font(size=15)
        LabelP41.place(x=40,y=40)

        Lx=35


        LabelP42 = tk.Label(self)
        LabelP42["text"] = "how to start app?"
        LabelP42["fg"] = "#EEEEEE"
        LabelP42["bg"] = "#393E46"
        LabelP42["font"] = tkFont.Font(size=14)
        LabelP42.place(x=Lx,y=150,width=170,height=200)

        LabelP43 = tk.Label(self)
        LabelP43["text"] = "how to see logs?"
        LabelP43["fg"] = "#EEEEEE"
        LabelP43["bg"] = "#393E46"
        LabelP43["font"] = tkFont.Font(size=14)
        LabelP43.place(x=Lx+175,y=150,width=170,height=200)

        LabelP44 = tk.Label(self)
        LabelP44["text"] = "how to see graphs?"
        LabelP44["fg"] = "#EEEEEE"
        LabelP44["bg"] = "#393E46"
        LabelP44["font"] = tkFont.Font(size=14)
        LabelP44.place(x=Lx+350,y=150,width=170,height=200)

        ButtonP41 = tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        ButtonP41["text"] = "Demo"
        ButtonP41["bg"] = "#00ADB5"
        ButtonP41["fg"] = "#EEEEEE"
        ButtonP41["border"] = "0"
        ButtonP41.place(x=Lx,y=350,width=170)

        ButtonP42 = tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        ButtonP42["text"] = "Demo"
        ButtonP42["bg"] = "#00ADB5"
        ButtonP42["fg"] = "#EEEEEE"

        ButtonP42["border"] = "0"
        ButtonP42.place(x=Lx+175,y=350,width=170)
        
        ButtonP43 = tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        ButtonP43["text"] = "Demo"
        ButtonP43["bg"] = "#00ADB5"
        ButtonP43["fg"] = "#EEEEEE"

        ButtonP43["border"] = "0"
        ButtonP43.place(x=Lx+350,y=350,width=170)

        ButtonP44 = tk.Button(self,activebackground="#08D9D6",activeforeground="#EEEEEE")
        ButtonP44["text"] = "Back"
        ButtonP44["bg"] = "#00ADB5"
        ButtonP44["fg"] = "#EEEEEE"
        ButtonP44["command"] = back
        ButtonP44["border"] = "0"
        ButtonP44.place(x=20,y=460,width=70,height=25)

        changeOnHover(ButtonP41,"#08D9D6","#00ADB5")
        changeOnHover(ButtonP42,"#08D9D6","#00ADB5")
        changeOnHover(ButtonP43,"#08D9D6","#00ADB5")
        changeOnHover(ButtonP44,"#08D9D6","#00ADB5")





# Driver Code
app = App()
ani = animation.FuncAnimation(f,animate,interval=1000)
width=600
height=500
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
app.geometry(alignstr)
app.resizable(width=False, height=False)
app.mainloop()
