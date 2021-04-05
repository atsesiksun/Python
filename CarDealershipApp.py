from tkinter import *
from tkinter import ttk
import os
import pyodbc

def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k,col), k) for k in tv.get_children()] #Display column #0 cannot be set
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

def delete6():
    screen11.destroy()

def delete5():
    screen10.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def search_now():
    selected = drop.get()
    if selected == "All":
        remove_all()
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        cur.execute("select h.car_id,h.type,h.date,s.type,s.lease_start,s.lease_end,sp.first_name + ' ' + sp.last_name salesperson_name,cp.first_name + ' ' + cp.last_name customer_name,mp.first_name + ' ' + mp.last_name mechanic_name,c.vin,c.color,c.list_price,m.model_name from sales.history h left join sales.sales s on s.id = h.sale_id left join sales.persons sp on sp.id = s.salesperson_id left join sales.persons cp on cp.id = s.customer_id left join sales.services r on r.id = h.service_id left join sales.persons mp on mp.id = r.mechanic_id left join inventory.cars c on c.id = h.car_id left join inventory.models m on m.id = c.model_id order by h.date")
        records = cur.fetchall()
        
        for record in records:
            my_tree.insert(parent="", index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]))

        conn.commit()
        conn.close()

    if selected == "Car ID":
        remove_all()
        selected2 = drop3.get()
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        sql = "select h.car_id,h.type,h.date,s.type,s.lease_start,s.lease_end,sp.first_name + ' ' + sp.last_name salesperson_name,cp.first_name + ' ' + cp.last_name customer_name,mp.first_name + ' ' + mp.last_name mechanic_name,c.vin,c.color,c.list_price,m.model_name from sales.history h left join sales.sales s on s.id = h.sale_id left join sales.persons sp on sp.id = s.salesperson_id left join sales.persons cp on cp.id = s.customer_id left join sales.services r on r.id = h.service_id left join sales.persons mp on mp.id = r.mechanic_id left join inventory.cars c on c.id = h.car_id left join inventory.models m on m.id = c.model_id where h.car_id =" + str(selected2)
        cur.execute(sql)
        records = cur.fetchall()
            
        for record in records:
            my_tree.insert(parent="", index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]))

        conn.commit()
        conn.close()

    if selected == "Customer":
        remove_all()
        selected3 = drop4.get()
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        sql = "select h.car_id,h.type,h.date,s.type,s.lease_start,s.lease_end,sp.first_name + ' ' + sp.last_name salesperson_name,cp.first_name + ' ' + cp.last_name customer_name,mp.first_name + ' ' + mp.last_name mechanic_name,c.vin,c.color,c.list_price,m.model_name from sales.history h left join sales.sales s on s.id = h.sale_id left join sales.persons sp on sp.id = s.salesperson_id left join sales.persons cp on cp.id = s.customer_id left join sales.services r on r.id = h.service_id left join sales.persons mp on mp.id = r.mechanic_id left join inventory.cars c on c.id = h.car_id left join inventory.models m on m.id = c.model_id where cp.first_name + ' ' + cp.last_name = '" + selected3 + "'"
        cur.execute(sql)
        records = cur.fetchall()
            
        for record in records:
            my_tree.insert(parent="", index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]))

        conn.commit()
        conn.close()

    if selected == "Salesperson":
        remove_all()
        selected4 = drop5.get()
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        sql = "select h.car_id,h.type,h.date,s.type,s.lease_start,s.lease_end,sp.first_name + ' ' + sp.last_name salesperson_name,cp.first_name + ' ' + cp.last_name customer_name,mp.first_name + ' ' + mp.last_name mechanic_name,c.vin,c.color,c.list_price,m.model_name from sales.history h left join sales.sales s on s.id = h.sale_id left join sales.persons sp on sp.id = s.salesperson_id left join sales.persons cp on cp.id = s.customer_id left join sales.services r on r.id = h.service_id left join sales.persons mp on mp.id = r.mechanic_id left join inventory.cars c on c.id = h.car_id left join inventory.models m on m.id = c.model_id where sp.first_name + ' ' + sp.last_name = '" + selected4 + "'"
        cur.execute(sql)
        records = cur.fetchall()

        for record in records:
            my_tree.insert(parent="", index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]))

        columns = ('car_id','event_type','event_date','sale_type','lease_start','lease_end','salesperson_name','customer_name', 'mechanic_name','vin','color','list_price','model_name')
        for cols in columns:
            my_tree.heading(cols, text=cols, command=lambda _col=cols: treeview_sort_column(my_tree, _col, False))

        conn.commit()
        conn.close()



def second_drop():
    global drop5
    global drop4
    global drop3
    global drop2
    selected = drop.get()
    if selected == "All":
        drop2 = ttk.Combobox(screen9, value=[""])
        drop2.current(0)
        drop2.grid(row=1, column=1, padx=0, pady=5)
    if selected == "Car ID":
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        cur.execute("select distinct car_id from sales.history where car_id is not null")
        records = cur.fetchall()
        str1 = []
        for record in records:
            str1.append(record[0])
        drop3 = ttk.Combobox(screen9, value=str1)
        drop3.current(0)
        drop3.grid(row=1, column=1, padx=0, pady=5)
        conn.commit()
        conn.close()
    if selected == "Customer":
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        cur.execute("select distinct cp.first_name + ' ' + cp.last_name customer_name from sales.history h left join sales.sales s on s.id = h.sale_id left join sales.persons cp on cp.id = s.customer_id where cp.first_name is not null or cp.last_name is not null")
        records = cur.fetchall()
        str1 = []
        for record in records:
            str1.append(record[0])
        drop4 = ttk.Combobox(screen9, value=str1)
        drop4.current(0)
        drop4.grid(row=1, column=1, padx=0, pady=5)  
        conn.commit()
        conn.close()
    if selected == "Salesperson":
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
        cur = conn.cursor()
        cur.execute("select distinct sp.first_name + ' ' + sp.last_name salesperson_name from sales.history h left join sales.sales s on s.id = h.sale_id left join sales.persons sp on sp.id = s.salesperson_id where sp.first_name is not null or sp.last_name is not null")
        records = cur.fetchall()
        str1 = []
        for record in records:
            str1.append(record[0])
        drop5 = ttk.Combobox(screen9, value=str1)
        drop5.current(0)
        drop5.grid(row=1, column=1, padx=0, pady=5)  
        conn.commit()
        conn.close()
    

def get_car_history():
    global my_tree
    global screen9
    global drop
    screen9 = Toplevel(root)
    screen9.title("Car History")
    screen9.geometry("800x600")
    search_label = Label(screen9, text="Search By")
    search_label.grid(row=0, column=0, padx=5, pady=10)
    search_label1 = Label(screen9, text="Choose By")
    search_label1.grid(row=1, column=0, padx=5, pady=10)
    search_button = Button(screen9, text="Select",command=second_drop)
    search_button.grid(row=0, column=2, padx=10, pady=10)
    drop = ttk.Combobox(screen9, value=["All", "Car ID", "Customer", "Salesperson"])
    drop.current(0)
    drop.grid(row=0, column=1, padx=0, pady=5)
    drop1 = ttk.Combobox(screen9, value=[""])
    drop1.current(0)
    drop1.grid(row=1, column=1, padx=0, pady=5)
    search_button1 = Button(screen9, text="Search",command=search_now)
    search_button1.grid(row=1, column=2, padx=10, pady=10)

    tree_frame = Frame(screen9)
    tree_frame.grid(row=2, column=1, padx=10, pady=10, columnspan=109)

    tree_scroll = Scrollbar(tree_frame,orient="vertical")
    tree_scroll.pack(side=RIGHT, fill="y")
    tree_scroll1 = Scrollbar(tree_frame, orient="horizontal")
    tree_scroll1.pack(side=BOTTOM, fill="x")

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", 
        background="white",
        foreground="black",
        rowheight=25,
        fieldbackground="white")

    style.map('Treeview', background=[('selected','silver')])

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll1.set, selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)
    tree_scroll1.config(command=my_tree.xview)

    my_tree['columns'] = ("car_id","event_type","event_date","sale_type","lease_start","lease_end","salesperson_name","customer_name", "mechanic_name","vin","color","list_price","model_name")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("car_id", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("event_type", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("event_date", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("sale_type", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("lease_start", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("lease_end", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("salesperson_name", anchor=W , width=150, minwidth=150, stretch=NO)
    my_tree.column("customer_name", anchor=W , width=150, minwidth=150, stretch=NO)
    my_tree.column("mechanic_name", anchor=W , width=150, minwidth=150, stretch=NO)
    my_tree.column("vin", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("color", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("list_price", anchor=CENTER , width=100, minwidth=100, stretch=NO)
    my_tree.column("model_name", anchor=W , width=250, minwidth=250, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("car_id", text="Car ID", anchor=CENTER)
    my_tree.heading("event_type", text="Event Type", anchor=CENTER)
    my_tree.heading("event_date", text="Event Date", anchor=CENTER)
    my_tree.heading("sale_type", text="Sale Type", anchor=CENTER)
    my_tree.heading("lease_start", text="Lease Start", anchor=CENTER)
    my_tree.heading("lease_end", text="Lease End", anchor=CENTER)
    my_tree.heading("salesperson_name", text="Salesperson Name", anchor=W)
    my_tree.heading("customer_name", text="Customer Name", anchor=W)
    my_tree.heading("mechanic_name", text="Mechanic Name", anchor=W)
    my_tree.heading("vin", text="VIN", anchor=CENTER)
    my_tree.heading("color", text="Color", anchor=CENTER)
    my_tree.heading("list_price", text="List Price", anchor=CENTER)
    my_tree.heading("model_name", text="Model Name", anchor=W)

    columns = ('car_id','event_type','event_date','sale_type','lease_start','lease_end','salesperson_name','customer_name', 'mechanic_name','vin','color','list_price','model_name')
    for cols in columns:
        my_tree.heading(cols, text=cols, command=lambda _col=cols: treeview_sort_column(my_tree, _col, False))

    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
    cur = conn.cursor()
    cur.execute("select ch.car_id,ch.event_type,ch.event_date,s.sale_type,s.lease_start,s.lease_end,sp.first_name + ' ' + sp.last_name salesperson_name,cp.first_name + ' ' + cp.last_name customer_name,mp.first_name + ' ' + mp.last_name mechanic_name,c.vin,c.color,c.list_price,m.model_name from sales.carhistory ch inner join sales.sales s on s.sale_id = ch.sale_id inner join sales.persons sp on sp.person_id = s.salesperson_id inner join sales.persons cp on cp.person_id = s.customer_id inner join sales.repairs r on r.repair_id = ch.repair_id inner join sales.persons mp on mp.person_id = r.mechanic_id inner join inventory.cars c on c.car_id = ch.car_id inner join inventory.models m on m.model_id = c.model_id")
    records = cur.fetchall()
        
    for record in records:
        my_tree.insert(parent="", index='end', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]))

    conn.commit()
    conn.close()

    
def session():
    global screen8
    screen8 = Toplevel(root)
    screen8.title("Dashboard")
    screen8.geometry("500x500")
    Label(screen8, text="Get Data", bg="silver", width="800", height="2", font=("Calibri", 13)).pack()
    Label(screen8, text="").pack()
    Button(screen8, text="Car History", width=30, height=2, command=get_car_history).pack()
    Label(screen8, text="").pack()

def login_success():
    session()

def login_failed():
    global screen4
    screen4 = Toplevel(root)
    screen4.title("Success")
    screen4.geometry("400x400")
    Label(screen4, text = "Login Failed: Password Error").pack()
    Button(screen4, text = "OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(root)
    screen5.title("Success")
    screen5.geometry("400x400")
    Label(screen5, text = "Login Failed: User not found").pack()
    Button(screen5, text = "OK", command=delete4).pack()

def registration_failed():
    global screen10
    screen10 = Toplevel(root)
    screen10.title("Success")
    screen10.geometry("400x400")
    Label(screen10, text = "Please Try Again: Username is already taken").pack()
    Button(screen10, text = "OK", command=delete5).pack()

def registration_passed():
    global screen11
    screen11 = Toplevel(root)
    screen11.title("Success")
    screen11.geometry("400x400")
    Label(screen11, text = "Registration Sucess").pack()
    Button(screen11, text = "OK", command=delete6).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
    cur = conn.cursor()
    cur.execute("select username from sales.login")
    records1 = cur.fetchall()
    str2 = 0
    for record1 in records1:
        if username_info.upper() == (record1[0]).upper():
            str2 =+ 1
    if str2 > 0:
        registration_failed()
    else:
        cur = conn.cursor()
        cur.execute("ALTER TABLE sales.login ADD password1 VARBINARY(256) OPEN SYMMETRIC KEY TestTableKey DECRYPTION BY CERTIFICATE EncryptTestCert")
        cur.execute("UPDATE sales.login SET password1 = (Convert(VARBINARY(256),DECRYPTBYKEY(password))) from sales.login ALTER TABLE sales.login DROP COLUMN password EXEC sp_rename 'sales.login.password1', 'password', 'COLUMN' INSERT INTO sales.login (username, password) values ('" + username_info +"', cast ('" + password_info + "' as varbinary)) OPEN SYMMETRIC KEY TestTableKey DECRYPTION BY CERTIFICATE EncryptTestCert UPDATE sales.login SET password = ENCRYPTBYKEY(KEY_GUID('TestTableKey'), password) CLOSE SYMMETRIC KEY TestTableKey")
        registration_passed()
    conn.commit()
    conn.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=SERVER_NAME; Database=CarDealership; Trusted_Connection=yes;")
    cur = conn.cursor()
    cur.execute("OPEN SYMMETRIC KEY TestTableKey DECRYPTION BY CERTIFICATE EncryptTestCert SELECT username, cast(Convert(VARBINARY(256),DECRYPTBYKEY(password)) as varchar) FROM sales.login")
    records2 = cur.fetchall()
    str3 = 0
    str4 = 0
    for record2 in records2:
        if username1.upper() == (record2[0]).upper():
            str3 += 1
            if password1 == (record2[1]):
                str4 += 1 
            else:
                str4 += 0
        else:
            str3 += 0
    
    if str3 > 0 and str4 > 0:
        login_success()
        screen2.destroy()
    elif str3 > 0  and str4 == 0: 
        login_failed()
    if str3 == 0:
        user_not_found()

    cur.execute("CLOSE SYMMETRIC KEY TestTableKey")

    conn.commit()
    conn.close()


def register():
    global screen1
    screen1 = Toplevel(root)
    screen1.title("Register")
    screen1.geometry("400x400")

    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    

    Label(screen1, text="Please enter details below to register:").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(root)
    screen2.title("Login")
    screen2.geometry("400x400")
    Label(screen2, text="Please enter details below to login:").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show='*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()
    

root = Tk()
root.title('CarDealership')
root.geometry("400x400")

Label(root, text="Adeline's Car Dealership", bg="silver", width="400", height="2", font=("Calibri", 13)).pack()
Label(root, text="").pack()
Button(root, text="Login", height="2", width="30", command=login).pack()
Label(root, text="").pack()
Button(root, text="Register", height="2", width="30", command=register).pack()


root.mainloop()

