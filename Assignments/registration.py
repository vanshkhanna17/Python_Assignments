from tkinter import *
import pymysql

def sub():
    d1 = {1: "Male", 2: "Female"}
    selection = d1[var.get()]
    d = {1: "Python", 2: "JAVA", 3: "React"}
    lb = ''
    for l in li:
        a = l.get()
        if a > 0:
            sele = d[a]
            lb = lb +" "+ sele
        else:
            sele = ""
            lb = lb + sele
    print(var1.get(),"ye")
    print(selection)
    print(lb)
    db = pymysql.connect("localhost", "root", "", "user")
    if db:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        # data = cursor.execute("Select * from user")
        data = cursor.execute('''CREATE TABLE User(NAME CHAR(50) NOT NULL, GENDER CHAR(10), SKILLS CHAR(50) )''')
        for i in range(0, len(u.li), 2):
            s = u.li[i]
            t = u.li[i + 1]
            dat = cursor.execute(
                '''INSERT INTO User (FNAME,LNAME) VALUES ('{0}','{1}','{2}')'''.format(var1.get(), selection, lb))
            db.commit()


top = Tk()
li=[IntVar(), IntVar(), IntVar()]
var = IntVar()
var1 = StringVar()
frame1 = Frame(top, width=300,height=700)
frame2 = Frame(top, width=300,height=700)
frame3 = Frame(top, width=300,height=700)
frame4 = Frame(top, width=300,height=700)
label=Label(frame1)
label.config(text = "Name: ")
label.pack(side = LEFT)
E1 = Entry(frame1, bd = 1, textvariable= var1)
E1.pack(side = RIGHT)
label=Label(frame2)
label.config(text = "Gender: ")
label.pack(side = LEFT)

R1 = Radiobutton(frame2, text = "Male",
				variable = var,
				value = 1,
                )

R2 = Radiobutton(frame2, text = "Female",
				variable = var,
				value = 2
                  )

R2.pack(side= RIGHT)
R1.pack(side= RIGHT)
label=Label(frame3)
label.config(text = "Skills: ")
label.pack(side = LEFT)
C1 = Checkbutton(frame3, text = "Python",
				variable = li[0],
                 onvalue = 1,
				 offvalue = 0,
				)
C2 = Checkbutton(frame3,
				text = "JAVA",
				variable = li[1],
                 onvalue = 2,
				 offvalue = 0,
				 )
C3 = Checkbutton(frame3,
				text = "React",
				variable = li[2],
                 onvalue = 3,
				 offvalue = 0,
				 )
C1.pack()
C2.pack()
C3.pack()
L1 = Button(frame4, text = "Submit", command=sub)
L1.pack()
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
top.mainloop()
