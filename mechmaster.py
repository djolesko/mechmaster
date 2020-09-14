import tkinter as tk
from tkinter import *


#https://www.youtube.com/watch?v=YXPyB4XeYLA
LARGE_FONT = ("OpenSans", 16)
NORMAL_FONT = ("OpenSans", 12)
SMALL_FONT = ("OpenSans", 10)

MechMaster=Tk()
header_label =tk.Label(text='Dobrodosli u Mechmaster',font=LARGE_FONT,bg='gray31', fg='white').grid(row=0,column=5)
header2_label=tk.Label(text='Izaberite opcije',font=NORMAL_FONT,bg='gray31', fg='white').grid(row=1,column=5)
def lista_kupaca():
	
button1 = tk.Button(text='Lista Kupaca', bg='gray35', fg='white', font=NORMAL_FONT).grid(row=3,column=1)
button2 = tk.Button(text='Novi Kupac', bg='gray35', fg='white', font=NORMAL_FONT).grid(row=3,column=3)


	
		
#MechMaster.geometry('1280x720')
MechMaster.configure(bg='gray41')
MechMaster.mainloop()

