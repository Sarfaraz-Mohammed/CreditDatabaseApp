from tkinter import *
import sqlite3

root = Tk()
root.title("Sign Up")
root.iconbitmap('C:/Users/Sarfaraz Mohammed/Documents/CreditDatabase/credit.ico')

#database
conn2DB = sqlite3.connect('users.db')
c = conn2DB.cursor()


#table
'''c.execute("""CREATE TABLE users (
            first_name text,
            last_name text,
            user_name text,
            password text
            )""")
'''

#delete a record function
def delete():
    conn2DB = sqlite3.connect('users.db')
    c = conn2DB.cursor()

    c.execute("DELETE from users WHERE oid= " + delete_box.get())
    conn2DB.commit()
    conn2DB.close()

#submit function to store record to DB
def submit():
    conn2DB = sqlite3.connect('users.db')
    c = conn2DB.cursor()

    c.execute("INSERT INTO users VALUES (:first_name, :last_name, :user_name, :password)",
            {
                'first_name': first_name.get(),
                'last_name': last_name.get(),
                'user_name': user_name.get(),
                'password': password.get()
            })
    conn2DB.commit()
    conn2DB.close()
    #clear text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    user_name.delete(0, END)
    password.delete(0, END)

#function to query all records from DB
def query():
    conn2DB = sqlite3.connect('users.db')
    c = conn2DB.cursor()

    c.execute("SELECT *, oid FROM users")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[4]) + " " + str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=6, column=0, columnspan=2)

    conn2DB.commit()
    conn2DB.close()



#text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1,padx=20, pady=(10,0))
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
user_name = Entry(root, width=30)
user_name.grid(row=2, column=1)
password = Entry(root, width=30)
password.grid(row=3, column=1)
#delete_box = Entry(root, width=30)
#delete_box.grid(row=7, column=1, pady=5)

#labels for text boxes
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0, pady=(10,0))
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
user_name_label = Label(root, text="User Name")
user_name_label.grid(row=2, column=0)
password_label = Label(root, text="Password")
password_label.grid(row=3, column=0)
#delete_box_label = Label(root, text="Delete ID")
#delete_box_label.grid(row=7, column=0, pady=5)

#buttons
submit_btn = Button(root, text="Register", command=submit)
submit_btn.grid(row=4,columnspan=2, pady=10,padx=10, ipadx=100)
query_btn = Button(root, text="Show Records",command=query)
query_btn.grid(row=5,columnspan=2, pady=10, padx=10, ipadx=137)
#delete_btn = Button(root, text="Delete Record",command=delete)
#delete_btn.grid(row=8,columnspan=2, pady=10, padx=10, ipadx=136)


conn2DB.commit()
             
conn2DB.close()

root.mainloop()