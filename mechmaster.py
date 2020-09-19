import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3
from tkcalendar import DateEntry


#https://www.youtube.com/watch?v=YXPyB4XeYLA
LARGE_FONT = ("OpenSans", 16)
NORMAL_FONT = ("OpenSans", 12)
SMALL_FONT = ("OpenSans", 10)

def popupmsg(msg):
    popup = tk.Tk()
    #popup.iconbitmap("content_portal_Hm6_icon.ico")
    popup.wm_title("BIRequestApplication")
    label = ttk.Label(popup, text=msg, font=NORMAL_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.geometry('300x150')
    popup.mainloop()




class Mechmaster(tk.Tk):

    def __init__(self, *args, **kwargs):
        # tk.Tk.iconbitmap(self,"icon.ico")

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #tk.Tk.iconbitmap(self, "containertent_portal_Hm6_icon.ico")
        self.frames = {}
        self.wm_title('Mechmaster 0.9')

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            # self.frames[PageOne] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
		
class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='gray31')
        label = tk.Label(self, text="MECH MASTER PRO ", bg='gray31', fg='white', font=LARGE_FONT, height=3, width=30)
        label.pack(pady=20, padx=20)

        button1 = tk.Button(self, text="Otvori Bazu", bg='medium aquamarine', fg='white', width=40,
                            height=4, font=NORMAL_FONT, command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Novi Kupac", bg='orange', fg='white', width=40, height=4, font=NORMAL_FONT,
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack(pady=10, padx=10)


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='gray31')
		button1  = tk.Button(self,text="Ucitaj postojece", font = NORMAL_FONT, command=lambda : import_data()).pack()
		button1  = tk.Button(self,text="Nazad", font = NORMAL_FONT, command=lambda : [refresh(),controller.show_frame(StartPage)]).pack()
		def import_data():
			conn=sqlite3.connect('mechmaster.db')
			df = pd.read_sql("select * from mechmaster_test",con=conn)
			global tree
			tree = ttk.Treeview(columns=("ime", "prezime", "datum", "opis","iznos","faktura","kilometraza","napmomene","model"),show='headings')
			for i in tree.get_children():
					tree.delete(i)
			tree.heading('#1', text='ime')
			tree.heading('#2', text='prezime')
			tree.heading('#3', text='datum')
			tree.heading('#4', text='opis')
			tree.heading('#5', text='iznos')
			tree.heading('#6', text='faktura')
			tree.heading('#7', text='kilometraza')
			tree.heading('#8', text='napomene')
			tree.heading('#9', text='model')
			tree.column('#1',width = 80,stretch=NO)
			tree.column('#2',width = 80,stretch=NO)
			tree.column('#3',width = 80,stretch=NO)
			tree.column('#4',width = 340,stretch=NO)
			tree.column('#5',width = 60,stretch=NO)
			tree.column('#6',width = 60,stretch=NO)
			tree.column('#7',width = 80,stretch=NO)
			tree.column('#8',width = 340,stretch=NO)
			tree.column('#9',stretch=NO)
			for column, row in df.iterrows():		
					tree.insert('', END, values=list(row))
					tree.columnconfigure(0,weight=1)
					tree.place(anchor='nw', relheight=0.4, relwidth=1.0, rely=0.6)
			#tree.bind('<ButtonRelease-1>', on_double_click)
		
		def refresh():
			tree.destroy()
			
			

		
class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='gray31')
		#self.grid_rowconfigure(5, minsize=2000, weight=1)
		header_label2=tk.Label(self,text='Dobrodosli u Mechmaster page two',font=LARGE_FONT,bg='gray31', fg='white').pack()
		#e0 = Text(self, height=3, width=30, wrap="none").grid()
		tk.Label(self,text="Unesite Ime",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e0=tk.Entry(self)
		e0.pack()
		tk.Label(self,text="Prezime",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e1=tk.Entry(self)
		e1.pack()
		tk.Label(self,text="Datum",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e2=DateEntry(self,locale='en_US',date_pattern='dd-mm-y')
		e2.pack()
		tk.Label(self,text="Opis",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e3=Text(self, height=5, width=30, wrap="none")
		e3.pack()
		tk.Label(self,text="Iznos RSD",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e4=tk.Entry(self)
		e4.pack()
		tk.Label(self,text="Faktura",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e5=tk.Entry(self)
		e5.pack()
		tk.Label(self,text="Kilometraza",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e6=tk.Entry(self)
		e6.pack()
		tk.Label(self,text="Napomene",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e7=Text(self, height=3, width=30, wrap="none")
		e7.pack()
		tk.Label(self,text="Model",font=NORMAL_FONT,bg='gray31', fg='white').pack()
		e8=tk.Entry(self)
		e8.pack()

		button5 = tk.Button(self, text="Unesi podatke u bazu", bg='snow4', fg='white', command=lambda: import_data2())
		button5.pack()

		def import_data2():
			global data
			data= {'ime':[e0.get()],
			'prezime':[e1.get()],
			'datum':[e2.get_date()],
			'opis':[e3.get("1.0",END)],
			'iznos':[e4.get()],
			'faktura':[e5.get()],
			'kilometraza':[e6.get()],
			'napomene':[e7.get("1.0",END)],
			'model':[e8.get()]
			}
			df = pd.DataFrame(data)	
			print(df)
			conn=sqlite3.connect('mechmaster.db')
			df.to_sql('mechmaster_test',con=conn, index=False, schema = 'mechmaster.db',if_exists='append')
			popupmsg('New project added to the database!')



app = Mechmaster()
app.geometry('1280x720')
app.mainloop()

