import tkinter as tk
import pymysql
from tkinter import *
from tkinter import messagebox, ttk
import PIL


db = pymysql.Connect("localhost", "root", "avani@123", "sql_databse")  ## Connect to database
cursor = db.cursor()

def submitact():
    user = Username.get()
    passw = password.get()

    print(
        f"""The name entered by you is {user} {passw}
    """)

    logintodb(user)
    openHome()

def openHome():
    canvas = tk.Tk()
    canvas.title("Home Page")
    canvas.geometry('300x300')


    ttk.Label(canvas, text="Movie Recommendation system",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=0, column=1)

    ttk.Label(canvas, text="Please choose the movie you like",
              background='blue', foreground="white",
              font=("Times New Roman", 12)).grid(row=10, column=1)

    # label
    ttk.Label(canvas, text="Select the Movie :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=14, padx=10, pady=25)

    # Combobox creation
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(canvas, width=27, textvariable=n)

    # Adding combobox drop down list
    monthchoosen['values'] = ('Mission Mangal',
                              'Tanhaji:The Unsung Warrior',
                              'War: Hrithik VS Tiger',
                              'Pati Patni aur woh',
                              'Luv aaj kal',
                              'Bhoot (Vicky Kaushal)'
                              )

    def checkcmbo():

        if monthchoosen.get() == "Mission Mangal":
            messagebox.showinfo("What user choose", "you choose Mission mangal")

            sql = "select * from DeshBakhti"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Patriotic Movies")
            SciFi.geometry("800x800")

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_Id")
            tv.heading(2, text="Movie_name")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Box_office")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()

        elif monthchoosen.get() == "Tanhaji:The Unsung Warrior":
            messagebox.showinfo("What user choose", "you choose Tanhaji:The Unsung Warrior")

            sql = "select * from Historical"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("historical movies")
            SciFi.geometry("800x800")

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_Id")
            tv.heading(2, text="Movie_name")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Box_office")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()


        elif monthchoosen.get() == "War: Hrithik VS Tiger":
            messagebox.showinfo("What user choose", "you choose War: Hrithik VS Tiger")

            sql = "select * from Action"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Action Thriller movies")
            SciFi.geometry("600x800")

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_Id")
            tv.heading(2, text="Movie_name")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Box_office")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()

        elif monthchoosen.get() == "Bhoot (Vicky Kaushal)":
            messagebox.showinfo("What user choose", "Bhoot (Vicky Kaushal)")

            sql = "select * from Horror"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Horror movies")
            SciFi.geometry("800x800")

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_Id")
            tv.heading(2, text="Movie_name")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Box_office")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()

        elif monthchoosen.get() == "Pati Patni aur woh":
            messagebox.showinfo("What user choose", "you choose  Pati Patni aur woh")

            sql = "select * from Comedy"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Comedy movies")
            SciFi.geometry("800x800")

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_Id")
            tv.heading(2, text="Movie_name")
            tv.heading(2, text="Ratings")
            tv.heading(2, text="Box_office")


            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()

        elif monthchoosen.get() == "Luv aaj kal":
            messagebox.showinfo("What user choose", "you choose Luv aaj kal")

            sql = "select * from Love"
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print("Total Data entries" + str(total))

            SciFi = tk.Tk()
            SciFi.title("Romance movies")
            SciFi.geometry("800x800")

            frm = Frame(SciFi)
            frm.pack(side=tk.LEFT, padx=20)

            tv = ttk.Treeview(frm, columns=(1, 2,3,4), show="headings", height="10")
            tv.pack()

            tv.heading(1, text="Movie_Id")
            tv.heading(2, text="Movie_name")
            tv.heading(3, text="Ratings")
            tv.heading(4, text="Box_office")

            for i in rows:
                tv.insert('', 'end', values=i)

            SciFi.resizable(FALSE, FALSE)
            SciFi.mainloop()

        elif monthchoosen.get() == "":
            messagebox.showinfo("nothing to show!", "you have to be choose something")

    Nexttkk = ttk.Button(canvas,text="Next",command=checkcmbo)
    Nexttkk.grid(column=1,row=20)

    monthchoosen.grid(column=1, row=14)
    monthchoosen.current()
    canvas.mainloop()

def logintodb(user):
    savequery = "select * from arushiuser where username = %s"
    try:
        cursor.execute(savequery, (user))
        db.commit()
        print("Feedback saved succesfully")
    except:
        db.rollback()
        print("Error occured")

def regbtnact():

    def loginact():
        Regpage.destroy()

    def registeract():
        userreg = Usernamereg.get()
        passwreg = passwordreg.get()

        print(
            f"""The name entered by you is {userreg} {passwreg}
               """)
        regtodb(userreg, passwreg)

    Regpage = Toplevel()
    Regpage.geometry('300x300')
    Regpage.title("Register page")
    my = Canvas(Regpage, bg="blue", height=400, width=400)
    filename1 = PhotoImage(file="E:\\Arushi_app\\moviebg.png")
    background_label1 = Label(Regpage, image=filename1)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)



    lblreg = tk.Label(Regpage, text="Username -", )
    lblreg.place(x=50, y=20)
    Usernamereg = tk.Entry(Regpage, width=35)
    Usernamereg.place(x=150, y=20, width=100)

    lbl2reg = tk.Label(Regpage, text="Password -")
    lbl2reg.place(x=50, y=50)
    passwordreg = tk.Entry(Regpage, width=35)
    passwordreg.place(x=150, y=50, width=100)

    regbtn = tk.Button(Regpage, text="Register", bg='blue', command=registeract)
    regbtn.place(x=150, y=120, width=55)

    regsitermsg = tk.Label(Regpage, text="Already a User?, Click on Login-")
    regsitermsg.place(x=20, y=250)
    logbtn = tk.Button(Regpage, text="Login", bg='blue', command=loginact)
    logbtn.place(x=200, y=250, width=55)
    Regpage.mainloop()



def regtodb(userreg,passwreg):
    regquery = "insert into arushiuser values(%s,%s)"
    try:
        cursor.execute(regquery, (userreg,passwreg))
        db.commit()
        print("Registered succesfully")
        msg = tk.messagebox.askquestion('Welcommsg', f"""Hello {userreg} your account was succesfully created selected yes to visit home page""", )

        if msg == 'yes':
            openHome()
        else:
            messagebox.destroy()
    except:
        db.rollback()
        print("Error occured, cannot register")



root = tk.Tk()
root.geometry("300x300")
root.title("Movie Recommendatiion system")

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "E:\\Arushi_app\\moviebg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Definging the first row
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)
Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)
password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)


submitbtn = tk.Button(root, text="Login", bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

regsitermsg = tk.Label(root, text="New User?, Click on Register-")
regsitermsg.place(x=20, y=250)



regbtn = tk.Button(root,text="Register", bg = 'blue',command=regbtnact)
regbtn.place(x=200,y=250,width=55)



root.mainloop()
