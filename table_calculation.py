from tkinter import GROOVE, LEFT, TOP, Button, Frame, Label, Tk
from tkinter.filedialog import askopenfilename
from customtkinter import CTkFrame
import pandas as pd

def t_cal(h,sh):

    main = CTkFrame(app, )
    headings = CTkFrame(height=50, border_color='red')
    headings.pack(side=TOP)

    side_headings = CTkFrame()
    side_headings.pack(side=LEFT)
    for i in h:
        labels = Label(headings,text=i,width=10,borderwidth=3)
        labels.pack(side=LEFT)
    
    for j in sh:
        labels = Label(side_headings,text=j,width=8,borderwidth=3,anchor='w')
        labels.pack()
    pass
    
def openfile():
    global cols
    btn = askopenfilename(initialdir="Desktop",
                                          title="Select A File",
                                          filetype=(('text files','*.csv'),("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    df= pd.read_csv(btn)
    
    cols = df.columns

    h = df['Category'].unique()
    sh = df['Sub-Category'].unique()
    t_cal(h,sh)

listofu = []



app = Tk()

screen_width = app.winfo_screenwidth()
btn =Button(command=openfile,text='open file',height=2,bg='blue',fg='yellow',borderwidth=3,relief=GROOVE)
btn.pack(side=TOP)

app.mainloop()