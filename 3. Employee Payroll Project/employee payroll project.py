import tkinter as tk
import tkinter.messagebox
import mysql.connector as mysql

cn = mysql.connect(database="testdb",user="root",password="Udayk0596@")
c=cn.cursor()
w=tk.Tk()
w.geometry("500x500+300+300")
w.title("Login")
w['bg']="lightgray"

l1 = tk.Label(w, text="UserName", font=("Arial", 15))
l1.grid(row=0, sticky="W", padx=10, pady=10)
e1 = tk.Entry(w, width=20, font=("Arial", 15))
e1.grid(row=0, column=1, sticky="W", padx=10, pady=10)


l2 = tk.Label(w, text="Password", font=("Arial", 15))
l2.grid(row=1, sticky="W", padx=10, pady=10)
e2 = tk.Entry(w, width=20, font=("Arial", 15), show="*") 
e2.grid(row=1, column=1, sticky="W", padx=10, pady=10)
def login():
    u=e1.get()
    p=e2.get()

    if not u or not p:
        tk.messagebox.showinfo("info","Please enter both username and password.")
        return
    c.execute("select * from user_profile where uname=%s and pwd=%s",(u,p))
    result=c.fetchone()
    if result is None:
        tkinter.messagebox.showinfo("info","invalid username or password")
    else:
        w.destroy()
        open_payroll_system()

def open_payroll_system():
    w1 = tk.Tk()
    w1.title("Payroll System")
    w1.geometry("500x500+300+300") 
    label = tk.Label(w1, text="Welcome to Payroll System",fg="Black",font=("Arial",15,"bold"))
    label.pack(padx=20,pady=20)

    def add():
        w1.destroy()
        w2=tk.Tk()
        w2.title("Add Employee")
        w2.geometry("500x500+300+300")
        l1=tk.Label(w2,text="EmployeeNo",font=("Arial",15))
        l1.grid(row=0,padx=10,pady=10,sticky="W")
        l2=tk.Label(w2,text="EmployeeName",font=("Arial",15))
        l2.grid(row=1, sticky="W", padx=10, pady=10)
        l3=tk.Label(w2,text="EmployeeSalary",font=("Arial",15))
        l3.grid(row=2,padx=10,pady=10,sticky="W")

        e1=tk.Entry(w2,width=15,font=("Arial",15))
        e1.grid(row=0, column=1, sticky="W", padx=10, pady=10)
        e2=tk.Entry(w2,width=20,font=("Arial",15))
        e2.grid(row=1, column=1, sticky="W", padx=10, pady=10)
        e3=tk.Entry(w2,width=20,font=("Arial",15))
        e3.grid(row=2, column=1, sticky="W", padx=10, pady=10)

        def save():
            eno=e1.get()
            ename=e2.get()
            s=e3.get()
            c=cn.cursor()
            if  not eno or not ename or not s:
                tk.messagebox.showinfo("Error","All fields must be filled")
                return
            try:
                c.execute("insert into emp (empno,ename,sal) values(%s,%s,%s)",(eno,ename,s))
                cn.commit()
                tk.messagebox.showinfo("Success",f"Employee {ename} inserted successfully.")
            except mysql.Error as err:
                tk.messagebox.showerror("Error",f"Error inserting employee details: {err}")
        def close():
            w2.destroy()


        save_button=tk.Button(w2,text="save",bg="lightgreen",font=("Arial",15,"bold"),command=save)
        save_button.grid(row=3,sticky="E",padx=10,pady=10)
        close_button=tk.Button(w2,text="close",bg="red",font=("Arial",15,"bold"),command=close)
        close_button.grid(row=3,column=2,sticky="W",padx=10,pady=10)

    def update():
        w1.destroy()
        w3=tk.Tk()
        w3.title("Update Employee")
        w3.geometry("500x500+300+300")
        l1=tk.Label(w3,text="EmployeeNo",font=("Arial",15))
        l1.grid(row=0,padx=10,pady=10,sticky="W")
        l2=tk.Label(w3,text="EmployeeName",font=("Arial",15))
        l2.grid(row=1, sticky="W", padx=10, pady=10)
        l3=tk.Label(w3,text="EmployeeSalary",font=("Arial",15))
        l3.grid(row=2,padx=10,pady=10,sticky="W")

        e1=tk.Entry(w3,width=15,font=("Arial",15))
        e1.grid(row=0, column=1, sticky="W", padx=10, pady=10)
        e2=tk.Entry(w3,width=20,font=("Arial",15))
        e2.grid(row=1, column=1, sticky="W", padx=10, pady=10)
        e3=tk.Entry(w3,width=20,font=("Arial",15))
        e3.grid(row=2, column=1, sticky="W", padx=10, pady=10)

        def save():
            eno=e1.get()
            ename=e2.get()
            s=e3.get()
            c=cn.cursor()

            if not eno or not ename or not s:
                tk.messagebox.showinfo("Error","All fields must be filled.")
                return
            try:
                c.execute("update emp set ename=%s,sal=%s where empno=%s",(ename,s,eno))
                cn.commit()
                tk.messagebox.showinfo("Success",f"Employee {ename} updated successfully.")

            except mysql.Error as err:
                tk.messagebox.showerror("Error",f"Error inserting employee details: {err}")
        def close():
            w3.destroy()
        save_button=tk.Button(w3,text="save",bg="lightgreen",font=("Arial",15,"bold"),command=save)
        save_button.grid(row=3,sticky="E",padx=10,pady=10)
        close_button=tk.Button(w3,text="close",bg="red",font=("Arial",15,"bold"),command=close)
        close_button.grid(row=3,column=2,sticky="W",padx=10,pady=10)
    def delete():
        w1.destroy()
        w4=tk.Tk()
        w4.title("Delete Employee")
        w4.geometry("500x500+300+300") 
        c=cn.cursor()
        l1=tk.Label(w4,text="EmployeeNumber",font=("Arial",15))
        l1.grid(row=0,padx=10,pady=10,sticky="W")
        e1=tk.Entry(w4,width=15,font=("Arial",15))
        e1.grid(row=0,column=1,padx=10,pady=10,sticky="W")
        
        def  save():
            eno=e1.get()
            if not eno:
                tk.messagebox.showinfo("Error",f"All fields must be filled.")
                return
            try:
                c.execute("delete from emp where empno=%s",(eno,))
                k=c.rowcount
                if k>0:
                    tk.messagebox.showinfo("info",f"Employee {eno} Deleted successfully.")
                    cn.commit()
                else:
                    tk.messagebox.error("Error",f"Invalid Employee Number.")
            except mysql.Error as err:
                tk.messagebox.showerror("Error",f"Error deleting employee details: {err}")
        def close():
            w4.destroy()
        delete_button=tk.Button(w4,text="delete",bg="lightgreen",font=("Arial",15,"bold"),command=save)
        delete_button.grid(row=3,sticky="E",padx=10,pady=10)
        close_button=tk.Button(w4,text="close",bg="red",font=("Arial",15,"bold"),command=close)
        close_button.grid(row=3,column=2,sticky="W",padx=10,pady=10)
          

    add_button=tk.Button(w1,text="Add Employee",width=20,font=("Arial",15,"bold"),bg="lightblue",command=add)
    add_button.pack(pady=10)
    update_button=tk.Button(w1,text="Update Employee",width=20,font=("Arial",15,"bold"),bg="lightblue",command=update)
    update_button.pack(pady=10)
    delete_button=tk.Button(w1,text="Delete Employee",width=20,font=("Arial",15,"bold"),bg="lightblue",command=delete)
    delete_button.pack(pady=10)
    close_button=tk.Button(w1,text="close",width=20,command=w1.destroy,bg="red",font=("Arial",15,"bold"))
    close_button.pack(pady=10,)

def close():
    w.destroy()
    
b1=tk.Button(w,text="Login",bg="lightgreen",command=login,font=("Arial",14,"bold")).grid(row=2,columnspan=2,column=0,sticky="W",padx=10,pady=10)
b2=tk.Button(w,text="Close",bg="red",command=close,font=("Arial",14,"bold")).grid(row=2,columnspan=2,sticky="W",column=1,padx=10,pady=10)
