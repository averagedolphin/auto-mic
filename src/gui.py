import tkinter
from tkinter import *

def initGui():
  # Root Window Characteristics and Layout.

    root = Tk()
    root.title("Auto Mic")
    root.geometry("500x500")

    selectTxt = Label(root, text="⠀⠀⠀Select a Audio Input              ")
    selectTxt.pack()
    selectTxt.place(bordermode=OUTSIDE, x=10, y=20)

    thresholdTxt = Label(root, text="Select Audio Threshold")
    thresholdTxt.place(bordermode=OUTSIDE, x=250, y=20)


    audioScroll = Scrollbar(root, orient="vertical")
    audioSelect = Listbox(root, selectmode=EXTENDED, yscrollcommand=audioScroll)
    audioSelect.place(bordermode=OUTSIDE, x=20, y=50)
    audioScroll.place(bordermode=OUTSIDE, x=150, y=50)

    thresholdSlider = Scale(root, orient=VERTICAL, length = 164)
    thresholdSlider.place(bordermode=OUTSIDE, x=315, y=45)

    visualThreshold = Canvas(root, width = 25, height = 165)
    visualThreshold.place(bordermode=OUTSIDE, x=265, y = 46)

    visualThreshold.create_polygon(0,0,0,165,25,165,25,0,fill="black")
    root.mainloop()

def refreshGui():
    visualThreshold.create_polygon(0, 0, 0, 165, 25, 165, 25, 0, fill="black")
    visualThreshold.create_line()
    pass