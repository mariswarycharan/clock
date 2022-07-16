from time import strftime, time
from tkinter import *

from time import strftime
root=Tk()

root.title("age calculator age")
lebal=Label(root,font=("ds-digital",30),background="black",foreground="white")
lebal.pack()

def time():
    a=strftime('%H:%M:%S %p')
    lebal.config(text=a)
    lebal.after(1000,time)
   
time()        
mainloop()

# #FF8040





