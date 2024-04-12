from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os

class Viewbooking:
    def __init__(self, root,username):
        self.root = root
        self.username=username
        self.root.geometry("1200x500")
        self.root.resizable(True, True)



        Back_btt = Button(self.root, text = " Cancel the booking ", command=self.cancel_data,font=("times new roman", 12, "bold"), bg="Black", fg = "green", bd=4)
        Back_btt.place(x=100, y=420, width=200)

        Back_btt = Button(self.root, text = " Back ",command=self.Back ,font=("times new roman", 12, "bold"), bg="Black", fg = "green", bd=4)
        Back_btt.place(x=100, y=10, width=100)




        self.frm = Frame(self.root, width=700, height=500)
        self.frm.place(x=1, y=300)

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
        cursor = mydb.cursor()
        cursor.execute("select cus_id from customer where username=%s", (self.username,))
        cus_id = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM booking where cus_id = %s", (cus_id,))
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: " + str(total))
     

        self.ff = ttk.Treeview(self.frm, columns=(1, 2, 3, 4,5,6), show="headings", height="5")
        self.ff.pack()

        self.ff.heading(1, text="Booking ID")
        self.ff.heading(2, text="Pick Up Location")
        self.ff.heading(3, text="Pickup Time")
        self.ff.heading(4, text="No of Passenger")
        self.ff.heading(5, text="Drop Location")
        self.ff.heading(6, text="Pickup Date")


        for i in rows:
            self.ff.insert('', 'end', values=i)

        self.root.mainloop()


    def cancel_data(self):
        # try:
            connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             database='taxi_booking',
                                             password='')

            cursor = connection.cursor()
            selected_item = self.ff.selection()[0]

            book_id = self.ff.item(selected_item)['values'][0]
            print(book_id)

            cursor.execute("Update booking set status='Cancelled' where booking_id = %s", (book_id,))
            connection.commit()

            

            messagebox.showinfo("success", "Booking cancelled successfully!")
            self.ff.delete(selected_item)


      


    def Back(self):
     self.root.destroy()
    
    


   
