from tkinter import *

from App.implement import timeSwift, timeSync


class escapeButton(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.timeSetter = Button(bd=1, width=10, height=2, text='开逃!', command=timeSwift)
        self.timeSetter.pack(side='top')


class resetButton(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.timeResetter = Button(bd=1, width=10, height=2, text='重置时间', command=timeSync)
        self.timeResetter.pack(side='top')



class authorTag(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.master, text="制作者:布尔值@柔风海湾")
        self.label.pack(side="bottom", anchor=W)
