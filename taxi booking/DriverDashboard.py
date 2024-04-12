import os
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector





class Driver_Dashboard:

    def __init__(self,root,username):

        self.root = root
        self.username = username
        self.root.geometry("800x600")
        self.root.resizable(True, True)




        #frame and table number 1
        self.frame = Frame(self.root,width=700,height=200,bg="red")
        self.frame.place(x=50,y=350)

        scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.user_tbb = ttk.Treeview(self.frame, columns=(
        "booking_id", "Pick_Up_Location", "Pick_Up_Time", "No_Of_Passenger", "Destination","Pick_Up_Date", "status",)
                                       , xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_tbb.xview)
        scroll_y.config(command=self.user_tbb.yview)
        self.user_tbb.heading("booking_id", text="booking_id")
        self.user_tbb.heading("Pick_Up_Location", text="Pickup Location")
        self.user_tbb.heading("Pick_Up_Time", text="Drop address")
        self.user_tbb.heading("No_Of_Passenger", text="No Of Passenger")
        self.user_tbb.heading( "Destination", text= "Destination")
        self.user_tbb.heading( "Pick_Up_Date", text= "Pick_Up_Date")
        self.user_tbb.heading("status", text="Status")

        self.user_tbb['show'] = 'headings'
        self.user_tbb.column("booking_id", width=100, anchor=CENTER)
        self.user_tbb.column("Pick_Up_Location", width=100, anchor=CENTER)
        self.user_tbb.column("Pick_Up_Time", width=100, anchor=CENTER)
        self.user_tbb.column("No_Of_Passenger", width=100, anchor=CENTER)
        self.user_tbb.column( "Destination", width=100, anchor=CENTER)
        self.user_tbb.column( "Pick_Up_Date", width=100, anchor=CENTER)
        self.user_tbb.column("status", width=100, anchor=CENTER)

        self.user_tbb.pack(fill=BOTH, expand=3)
        self.fetch_data01()


        #frame2 and table number 2

        self.frame2 = Frame(self.root, width=700, height=200, bg="red")
        self.frame2.place(x=50, y=50)

        scroll_x = Scrollbar(self.frame2, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame2, orient=VERTICAL)
        self.user_tbb01 = ttk.Treeview(self.frame2, columns=(
        "booking_id", "Pick_Up_Location", "Pick_Up_Time", "No_Of_Passenger", "Destination","Pick_Up_Date", "status",)
                                       , xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_tbb01.xview)
        scroll_y.config(command=self.user_tbb01.yview)
        self.user_tbb01.heading("booking_id", text="booking_id")
        self.user_tbb01.heading("Pick_Up_Location", text="Pickup Location")
        self.user_tbb01.heading("Pick_Up_Time", text="Drop address")
        self.user_tbb01.heading("No_Of_Passenger", text="No Of Passenger")
        self.user_tbb01.heading( "Destination", text= "Destination")
        self.user_tbb01.heading( "Pick_Up_Date", text= "Pick_Up_Date")
        self.user_tbb01.heading("status", text="Status")

        self.user_tbb01['show'] = 'headings'
        self.user_tbb01.column("booking_id", width=100, anchor=CENTER)
        self.user_tbb01.column("Pick_Up_Location", width=100, anchor=CENTER)
        self.user_tbb01.column("Pick_Up_Time", width=100, anchor=CENTER)
        self.user_tbb01.column("No_Of_Passenger", width=100, anchor=CENTER)
        self.user_tbb01.column( "Destination", width=100, anchor=CENTER)
        self.user_tbb01.column( "Pick_Up_Date", width=100, anchor=CENTER)
        self.user_tbb01.column("status", width=100, anchor=CENTER)

        self.user_tbb01.pack(fill=BOTH, expand=3)
        self.fetch_data()


        # Button
    

        self.button = Button(self.root, text="logout", font=('times new roman', 14, 'bold'), command=self.Back)
        self.button.place(x=730, y=0)
        self.button = Button(self.root, text="Trip Completed" ,   font=('times new roman', 14, 'bold'), command=self.complete_data)
        self.button.place(x=0, y=0)

        self.root.mainloop()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
        cursor = conn.cursor()

        cursor.execute("select * from driver where username=%s", (self.username,))
        driver_id = cursor.fetchone()[0]

        cursor.execute("SELECT booking_id, Pick_Up_Location, Pick_Up_Time, No_Of_Passenger, Destination,Pick_Up_Date, status FROM booking  where dri_id =%s and status ='Confirm'", (driver_id,))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.user_tbb01.delete(*self.user_tbb01.get_children())
            for row in rows:
                self.user_tbb01.insert('', END, values=row)
                conn.commit()
        conn.close()

    def fetch_data01(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
        cursor = conn.cursor()

        cursor.execute("select * from driver where username=%s", (self.username,))
        driver_id = cursor.fetchone()[0]

        cursor.execute("SELECT booking_id, Pick_Up_Location, Pick_Up_Time, No_Of_Passenger, Destination,Pick_Up_Date, status  FROM booking  where dri_id =%s and status ='Completed'", (driver_id,))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.user_tbb.delete(*self.user_tbb.get_children())
            for row in rows:
                self.user_tbb.insert('', END, values=row)
                conn.commit()
        conn.close()

    def complete_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
        cursor = conn.cursor()
        selected_item = self.user_tbb01.selection()[0]
        book_id = self.user_tbb01.item(selected_item)['values'][0]
        self.user_tbb01.delete(selected_item)
        cursor.execute("select * from driver where username=%s", (self.username,))
        driver_id = cursor.fetchone()[0]
        cursor.execute("Update driver set status = 'Available' where dri_id = %s", (driver_id,))
        cursor.execute("Update booking set dri_id = %s, status='Completed' where booking_id=%s", (driver_id,book_id,))     
        conn.commit()
        self.fetch_data01()
        messagebox.showinfo("Success", "Booking  Completed Sucessfully")
        conn.close()


    def Back(self):
      self.root.destroy()
      import DriverLogin
      self.new = Toplevel()
      self.obj = DriverLogin.Login(self.new)  