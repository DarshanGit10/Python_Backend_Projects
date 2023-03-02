
  
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import tkinter as tk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.config(width=root.winfo_screenwidth(),height=root.winfo_screenheight(),bg='white')
        self.root.pack_propagate(0)


        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"), bg="white", fg="black")
        title.pack(side=TOP, fill=X)

        #require data variables
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.txt_Address = StringVar()
        
        self.entry = tk.Entry(self.root, textvariable=self.txt_Address)
        self.entry.pack()

        self.search_by = StringVar()
        self.search_txt = StringVar()


        #manage frame left side
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="Manage Student",  bg="white", fg="black", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)
       
        lbl_roll = Label(Manage_Frame, text="Roll No.",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_roll.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        txt_roll = Entry(Manage_Frame, textvariable=self.roll_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_var,  font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state="readonly" )
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        
        lbl_contact = Label(Manage_Frame, text="Contact",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")


        lbl_dob = Label(Manage_Frame, text="DOB",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_dob.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        txt_gender = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_gender.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address",  bg="white", fg="black", font=("times new roman", 18, "bold"))
        lbl_address.grid(row=7, column=0, padx=20, pady=10, sticky="w")
        self.txt_Address =Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.txt_Address.grid(row=7, column=1, padx=20, pady=10, sticky="w")
        
        #button frame
        Button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="white")
        Button_Frame.place(x=10, y=510, width=430)

        addbtn = Button(Button_Frame, text="Add", width=8, command=self.add_student).grid(row=0, column=0, padx=5, pady=5)
        updatebtn = Button(Button_Frame, text="Update", width=8, command=self.update_data).grid(row=0, column=1, padx=5, pady=5)
        deletebtn = Button(Button_Frame, text="Delete", width=8, command=self.delete_data).grid(row=0, column=2, padx=5, pady=5)
        clearbtn = Button(Button_Frame, text="Clear", width=8, command=self.clear).grid(row=0, column=3, padx=5, pady=5)
        

        #Detail Frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=100, width=750, height=580)


        
        #Table Frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")

        Table_Frame.place(x=20, y=60, width=700, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name","email","gender", "contact", "dob", "address"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show']='headings' # removing extra index col at begining

        #setting up widths of cols
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=100)
        self.Student_table.pack(fill=BOTH, expand=1) #fill both is used to fill cols around the frame
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)# this is an event to select row 
        
        self.fetch_data() #to display data in grid

    def add_student(self):

        if self.roll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")

        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="Student")
            cur = con.cursor()
            
            cur.execute("insert into students values(%s, %s, %s, %s, %s, %s, %s)", (self.roll_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.entry.get()   ))


            con.commit()
            self.fetch_data() # this is for if we add any new student then it will call and update the pool
            self.clear()
            con.close()
            messagebox.showinfo("Successfull", "Record has been inserted.")

    def fetch_data(self):
            
        con = pymysql.connect(host="localhost", user="root", password="", database="Student")
        cur = con.cursor()

        cur.execute("select * from students")
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

            con.commit()
        con.close()

    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.entry.delete('1.0', END)

    def get_cursor(self, evnt):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.entry.delete('1.0', END)
        self.entry.insert(END, row[6])

    def update_data(self):
        if self.roll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="Student")
            cur = con.cursor()
            cur.execute("UPDATE students SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll=%s", (self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.entry.get(), self.roll_var.get(),  ))
            con.commit()
            self.fetch_data() # this is for if we add any new student then it will call and update the pool
            self.clear()
            con.close()
            messagebox.showinfo("successfull", "Record has been updated.")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="Student")
        cur = con.cursor()
        
        cur.execute("delete from students where roll=%s",self.roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("successfull", "Record has been deleted.")

root = Tk()
obj = Student(root)
root.mainloop()



