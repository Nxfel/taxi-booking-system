from cProfile import label
from cgitb import text
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
#import PIL.ImageTk

class Admindashboard:
        def __init__(self,root,username):
                self.root=root
                self.username = username
                self.root.geometry("1550x800")
                self.ffm=Frame(root,bg="black")
                self.ffm.place(x=10,y=200,height=500,width=600)

                self.ffm2=Frame(root,bg="black")
                self.ffm2.place(x=620,y=200,height=500,width=900)

                self.name = StringVar()
                self.pick = StringVar()
                self.time = StringVar()
                self.passenger = StringVar()
                self.drop = StringVar()
                self.date = StringVar()
                self.driverlist = []
                self.fetchdriver()

                
                




                #Assign Trip Button 
                booking_btt = Button(self.root, text = " Assign Trip ", command=self.assign,font=("times new roman", 13, "bold"), bg="Black", fg = "skyBlue", bd=4) 
                booking_btt.place(x=1050, y=20, width=150, height=45)




                #LogOut Button
                logout_btt = Button(self.root, text = " Log Out ",command=self.Back,font=("times new roman", 13, "bold"), bg="Black", fg = "skyBlue", bd=4)
                logout_btt.place(x=40, y=20, width=150, height=45)

                # Creating Frame 
                
                lbl_pickuplocation = Label(self.ffm, text= " Pick Up Location :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=120)
                self.gg_pickuplocation = Entry(self.ffm,font= ("times new roman", 16), textvariable=self.pick, fg="Black", bg="White").place(x=220,y=122, width=280)

                lbl_pickuptime = Label(self.ffm, text= " Pick Up Time :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=180)
                self.gg_pickuptime = Entry(self.ffm,font= ("times new roman", 16), textvariable=self.time, fg="Black", bg="White").place(x=220,y=182, width=280)

                lbl_numofpassenger = Label(self.ffm, text= " No of Passenger :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=240)
                self.gg_numofpassenger = Entry(self.ffm, font= ("times new roman", 16), textvariable=self.passenger, fg="Black", bg="White").place(x=220,y=242, width=280)

                lbl_destination = Label(self.ffm, text= " Destination :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=300)
                self.gg_destination = Entry(self.ffm, font= ("times new roman", 16), textvariable=self.drop, fg="Black", bg="White").place(x=220,y=306, width=280)

                lbl_pickupdate = Label(self.ffm, text= " Pick Up Date :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=360)
                self.gg_pickupdate = Entry(self.ffm, font= ("times new roman", 16), textvariable=self.date, fg="Black", bg="White").place(x=220,y=368, width=280)
                
                lbl_dname = Label(self.ffm, text= " Driver Name :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=420)
                self.dname = ttk.Combobox(self.ffm, font= ("times new roman", 16), textvariable=self.name, values = self.driverlist, state='readonly', foreground='black', background='white').place(x=220,y=428, width=280)
                
                
                scroll_x = Scrollbar(self.ffm2, orient=HORIZONTAL)
                scroll_y = Scrollbar(self.ffm2, orient=VERTICAL)
                self.Booking_table = ttk.Treeview(self.ffm2,
                                  columns=(
                                      "Bookingid", "customer name", "email", "gender", "contact", "pickup location", "pickup time",
                                      "no of passenger","destination","pickup date")
                                      ,
                                  xscrollcommand=scroll_y, yscrollcommand=scroll_x)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)

                scroll_x.config(command=self.Booking_table.xview)
                scroll_y.config(command=self.Booking_table.yview)

                self.Booking_table.heading("Bookingid", text="Booking Id", anchor=W)
                self.Booking_table.heading("customer name", text="customer Name", anchor=W)
                self.Booking_table.heading("email", text="email", anchor=W)
                self.Booking_table.heading("gender", text="gender", anchor=W)
                self.Booking_table.heading("contact", text="contact", anchor=W)
                self.Booking_table.heading("pickup location", text="pickup location", anchor=W)
                self.Booking_table.heading("pickup time", text="pickup time", anchor=W)
                self.Booking_table.heading("no of passenger", text="no of passenger", anchor=W)
                self.Booking_table.heading("destination", text="destination", anchor=W)
                self.Booking_table.heading("pickup date", text="Pickup date", anchor=W)

                self.Booking_table['show'] = 'headings'
                self.Booking_table.column("Bookingid", width=50, anchor=W)
                self.Booking_table.column("customer name", width=50, anchor=W)
                self.Booking_table.column("email", width=50, anchor=W)
                self.Booking_table.column("gender", width=50, anchor=W)
                self.Booking_table.column("contact", width=50, anchor=W)
                self.Booking_table.column("pickup location", width=50, anchor=W)
                self.Booking_table.column("pickup time", width=50, anchor=W)
                self.Booking_table.column("no of passenger", width=50, anchor=W)
                self.Booking_table.column("destination", width=50, anchor=W)
                self.Booking_table.column("pickup date", width=50, anchor=W)
                self.Booking_table.bind("<ButtonRelease-1>", self.gettabledata)

                self.Booking_table.pack(fill=BOTH, expand=1)
                self.fetch_data()

                self.root.mainloop()

   
        def Back(self):
         self.root.destroy()
         import LoginPage
         self.new = Toplevel()
         self.obj = LoginPage.Login(self.new) 

        def fetch_data(self):
                try:
                        connection = mysql.connector.connect(host='localhost',
                                                        user='root',
                                                        database='taxi_booking',
                                                        password='')

                        cursor = connection.cursor()

                        

                        cursor.execute(
                        "select b.booking_id,c.name,c.email,c.gender,c.contact,b.Pick_Up_Location,b.Pick_Up_Time,b.No_Of_Passenger,b.Destination,b.Pick_Up_Date from customer c join booking b on c.cus_id=b.cus_id")
                        rows = cursor.fetchall()
                        if len(rows) != 0:
                                self.Booking_table.delete(*self.Booking_table.get_children())
                                for i in rows:
                                        self.Booking_table.insert('', END, values=i)
                                        connection.commit()
                        connection.close()
                except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}")
        def gettabledata(self,ev):
                s = self.Booking_table.focus()
                content = (self.Booking_table.item(s))
                row = content['values']

                self.date.set(row[9]),
                self.pick.set(row[5]),
                self.time.set(row[6]),
                self.drop.set(row[8]),
                self.passenger.set(row[7])

        def fetchdriver(self):
                self.driverlist.append("Empty")
                connection = mysql.connector.connect(host='localhost',
                                                        user='root',
                                                        database='taxi_booking',
                                                        password='')

                cursor = connection.cursor()
                try:
                        cursor.execute("select name from driver where status='Available'")
                        driver = cursor.fetchall()
                        if len(driver)>0:
                                self.driverlist[:]
                                self.driverlist.append("select")
                                for i in driver:
                                        self.driverlist.append(i[0])
                   
                except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}")       


        def assign(self):
                try:
                        connection = mysql.connector.connect(host='localhost',
                                                        user='root',
                                                        database='taxi_booking',
                                                        password='')

                        cursor = connection.cursor()
                        select_item = self.Booking_table.selection()[0]
                        booking_id = self.Booking_table.item(select_item)['values'][0]

                        cursor.execute("select dri_id from driver where name=%s", (self.name.get(),))
                        dri_id = cursor.fetchone()[0]

                        

                        cursor.execute("update driver set status='not available' where dri_id=%s", (dri_id,))
                        cursor.execute("update booking set dri_id=%s, status='confirm' where booking_id=%s", (dri_id, booking_id,))
                        connection.commit()
                        messagebox.showinfo("successfully", "driver assigned successfully", parent=self.root)
                
                except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}")

 