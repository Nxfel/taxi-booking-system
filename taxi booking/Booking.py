 
from tkinter import *
from tkinter import messagebox
import mysql.connector

 


class Booking_Page:

    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Booking Page")
        self.root.geometry("1200x550")
        self.root.resizable(False,False)


        self.one=StringVar()
        self.two=StringVar()
        self.three=StringVar()
        self.four=StringVar()
        self.five=StringVar()

        # Creating Frame 
        frm_bkng = Frame(self.root, bg = "Black", highlightbackground="green", highlightthickness=5)
        frm_bkng.place(x=50,y=100, height=450, width=1100)

        lbl_booking = Label(self.root, text=" Book a Trip ", font=("times new roman", 28), fg="white", bg="Black")
        lbl_booking.place(x=460,y=20)

        back_btn_booking = Button(self.root, text = " Back " ,command=self.back ,font=("times new roman", 12), bg="Black", fg = "white", bd=4)
        back_btn_booking.place(x=15 , y=35, width=100)

        
        
        lbl_pickuplocation = Label(frm_bkng, text= " Pick Up Location :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=120)
        self.tf_pickuplocation = Entry(frm_bkng, textvariable=self.one,font= ("times new roman", 16), fg="Black", bg="White").place(x=220,y=122, width=280)

        lbl_pickuptime = Label(frm_bkng, text= " Pick Up Time :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=180)
        self.tf_pickuptime = Entry(frm_bkng, textvariable=self.two,font= ("times new roman", 16), fg="Black", bg="White").place(x=220,y=182, width=280)

        lbl_numofpassenger = Label(frm_bkng, text= " No of Passenger :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=30,y=240)
        self.tf_numofpassenger = Entry(frm_bkng,textvariable=self.three, font= ("times new roman", 16), fg="Black", bg="White").place(x=220,y=242, width=280)

        lbl_destination = Label(frm_bkng, text= " Destination :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=566,y=120)
        self.tf_destination = Entry(frm_bkng, textvariable=self.four,font= ("times new roman", 16), fg="Black", bg="White").place(x=730,y=122, width=280)

        lbl_pickupdate = Label(frm_bkng, text= " Pick Up Date :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=566,y=180)
        self.tf_pickupdate = Entry(frm_bkng,textvariable=self.five, font= ("times new roman", 16), fg="Black", bg="White").place(x=730,y=182, width=280)
        

        confirm_btn = Button(frm_bkng, text = " Confirm ", command=self.confirm,font=("times new roman", 12, "bold"), bg="Black", fg = "green", bd=4)
        confirm_btn.place(x=870, y=350, width=130)


                   
        self.root.mainloop()
    
    def back(self):
        
        self.root.destroy()



    def confirm(self):

            if self.one.get()== ""or self.two.get()==""or self.three.get()==""or   self.four.get()==""or   self.five.get()=="":
                messagebox.showerror("Error", "All Field must be filled", parent = self.root)

            else:

                try:
                    
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
                    cursor = conn.cursor()

                    cursor.execute("select cus_id from customer where username=%s", (self.username,)) 
                        
                    customerid = cursor.fetchone()[0]
                    statement = ("Insert into booking (Pick_Up_Location, Pick_Up_Time, No_Of_Passenger, Destination, Pick_Up_Date,status,cus_id) values (%s,%s,%s,%s,%s,%s,%s)")
                    values = (
                        self.one.get(),
                        self.two.get(),
                        self.three.get(),
                        self.four.get(),
                        self.five.get(),
                        'pending',
                        customerid

                    )
                    cursor.execute(statement,values)
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Successful","Successfully booked!",parent=self.root)

                except Exception as es:

                    messagebox.showerror("Error", f"Error due to: {str(es)}")





