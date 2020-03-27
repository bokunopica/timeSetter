from tkinter import *
from App.models import escapeButton, resetButton, authorTag

root = Tk()
root.geometry('220x120+500+200')
root.resizable(width=False, height=False)
root.wm_title('逃课工具')
root.iconbitmap("static/icon.ico")

authorFunc = authorTag(master=root)
escapeFunc = escapeButton(master=root)
resetFunc = resetButton(master=root)

