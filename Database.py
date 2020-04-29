import tkinter as tk
from tkinter import ttk

import pymysql
import tk as tkk
from tkinter import *

db = pymysql.connect("localhost","root", "avani@123", "sql_databse")
cursor =db.cursor()

sql = "select * from arushiuser"
cursor.execute(sql)
rows = cursor.fetchall()
total = cursor.rowcount
print("Total Data entries"+str(total))

root =tk.Tk()
root.title("Kuch kassh nai")
root.geometry("600x600")

frm = Frame(root)
frm.pack(side=tk.LEFT,padx=20)

tv= ttk.Treeview(frm,columns=(1,2),show="headings",height="5")
tv.pack()

tv.heading(1,text="username")
tv.heading(2,text="password")

for i in rows:
    tv.insert('','end', values=i)

root.resizable(FALSE,FALSE)
root.mainloop()