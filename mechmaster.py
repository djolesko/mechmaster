import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3


#https://www.youtube.com/watch?v=YXPyB4XeYLA
LARGE_FONT = ("OpenSans", 16)
NORMAL_FONT = ("OpenSans", 12)
SMALL_FONT = ("OpenSans", 10)

class Mechmaster(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.grid()

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

		
class StartPage(tk.Frame):

		def __init__(self, parent, controller):
				tk.Frame.__init__(self, parent)
				header_label=tk.Label(text='Dobrodosli u Mechmaster',font=LARGE_FONT,bg='gray31', fg='white').grid(column=5,row=0)
				header2_label=tk.Label(text='Izaberite opcije',font=NORMAL_FONT,bg='gray31', fg='white').grid(column=5,row=1)
				button1 = tk.Button(text='Lista Kupaca', bg='gray35', fg='white', font=NORMAL_FONT,command=lambda : tree()).grid()
				button2 = tk.Button(text='Novi Kupac', bg='gray35', fg='white', font=NORMAL_FONT).grid()


class PageOne(tk.Frame):

		def __init__(self, parent, controller):
			tk.Frame.__init__(self, parent,bg='gray31')
			
			global tree
			def tree():
					conn=sqlite3.connect('mechmaster.db')
					df = pd.read_sql("select * from mechmaster_test",con=conn)
					tree = ttk.Treeview(columns=("ime", "prezime", "datum", "opis"),show='headings')
					for i in tree.get_children():
							tree.delete(i)
					tree.heading('#1', text='ime')
					tree.heading('#2', text='prezime')
					tree.heading('#3', text='datum')
					tree.heading('#4', text='opis')
					tree.column('#1',stretch=NO)
					tree.column('#2',stretch=NO)
					tree.column('#3',stretch=NO)
					tree.column('#4',stretch=NO)
					for column, row in df.iterrows():		
							tree.insert('', END, values=list(row))
							tree.columnconfigure(0,weight=1)
							tree.place(anchor='nw', relheight=0.4, relwidth=1.0, rely=0.6)
				#tree.bind('<ButtonRelease-1>', on_double_click)
		
class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
		label.grid()

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.grid()

		button2 = tk.Button(self, text="Page One",
							command=lambda: controller.show_frame(PageOne))
		button2.grid()
		



app = Mechmaster()
app.geometry("")
app.mainloop()

