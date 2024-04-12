from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox, ttk
#from PIL import ImageTk 
#from tkcalendar import DateEntry 
import mysql.connector

class Assign_trip:

    def __init__(self,root,username):
        self.root=root
        self.username = username
        self.level = None
        self.assign_trip_body()

    def assign_trip_body(self) :
        self.level = Toplevel()
        self.level.title("Assign Trip")
        self.level.geometry("1800x789")
        self.level.resizable(False,False)
    
        #==================================== BackGround Image ============================#
        #self.bg = ImageTk.PhotoImage(file="1.jpg")  
        #self.bg_image = Label(self.level, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Creating Frame
        Frame_viewbooking_table = Frame(self.level, bg = "Black", highlightbackground="skyblue", highlightthickness=3)
        Frame_viewbooking_table.place(x=130,y=640, height=400, width=1650)

        #Creating Frame for data entery 
        Frame_viewbooking = Frame(self.level, bg = "Black", highlightbackground="skyblue", highlightthickness=3)
        Frame_viewbooking.place(x=315,y=150, height=400, width=1300)


        #Creating Lable
        lbl_viewbooking = Label(self.level, text=" Your Up Comming Trips ", font=("times new roman", 36), fg="white", bg="Black")
        lbl_viewbooking.place(x=710,y=20)

        
        #Creating Lable for Driver Name

        self.driver_list = []
        self.available_driver()
        # self.text_driver_name = StringVar()

        lbl_driverid = Label(Frame_viewbooking, text=" Driver Name : ",font=("times new roman", 18), fg="white", bg="Black")
        lbl_driverid.place(x=75,y=30)
        self.tf_driverid = ttk.Combobox(Frame_viewbooking,values=self.driver_list,state="readonly",font= ("times new roman", 15), justify=CENTER)
        self.tf_driverid.place(x=250,y=33, width=330)


        #Creating Lable for Customer Name
        self.text_Customername = StringVar()
        # text_Customername.set(customername_variable)
        lbl_CustomerName = Label(Frame_viewbooking, text=" Customer Name : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_CustomerName.place(x=700,y=30)
        self.tf_CustomerName = Entry(Frame_viewbooking,textvariable=self.text_Customername,state="readonly", font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_CustomerName.place(x=900,y=33, width=330)

        #Creating Lable for Pickup Location 
        self.text_pickuplocation = StringVar()
        lbl_pickup_location = Label(Frame_viewbooking, text=" Pickup Location : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_pickup_location.place(x=40,y=120)
        self.tf_pickup_location = Entry(Frame_viewbooking,textvariable=self.text_pickuplocation,state="readonly", font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_pickup_location.place(x=250,y=123, width=330)

        #Creating Lable for Destination 
        self.text_destination= StringVar()
        lbl_destination = Label(Frame_viewbooking, text=" Destination : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_destination.place(x=745,y=120)
        self.tf_destination = Entry(Frame_viewbooking,textvariable=self.text_destination,state="readonly", font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_destination.place(x=900,y=123, width=330)

        #Creating Lable for Pickup Date
        self.text_pickupdate= StringVar()
        lbl_pickup_date = Label(Frame_viewbooking, text="Pickup Date : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_pickup_date.place(x=83,y=210)
        self.tf_pickup_date = Entry(Frame_viewbooking,textvariable=self.text_pickupdate,state="readonly", font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_pickup_date.place(x=250,y=213, width=330)

        #Creating Lable for Pickup Time
        self.text_pickuptime= StringVar()
        lbl_pickup_time = Label(Frame_viewbooking, text=" Pickup Time : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_pickup_time.place(x=732,y=210)
        self.tf_pickup_time = Entry(Frame_viewbooking,textvariable=self.text_pickuptime,state="readonly", font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_pickup_time.place(x=900,y=213, width=330)

        #Creating Lable for Cost
        self.text_cost= StringVar()
        lbl_cost = Label(Frame_viewbooking, text=" Cost : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_cost.place(x=150,y=300)
        self.tf_cost = Entry(Frame_viewbooking,textvariable=self.text_cost,state="readonly", font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_cost.place(x=250,y=303, width=330)

        # Creating Lable for Status
        self.text_status= StringVar()
        lbl_status = Label(Frame_viewbooking, text=" Status : ", font=("times new roman", 18), fg="white", bg="Black")
        lbl_status.place(x=794,y=300)
        self.tf_status = Entry(Frame_viewbooking,textvariable=self.text_status,state="readonly",  font= ("times new roman", 15), fg="Black", bg="White")
        self.tf_status.place(x=900,y=303, width=330)
    

        #Creating Back Button
        back_btn_viewbooking = Button(self.level, text = " Back " ,command=self.dash,font=("times new roman", 12), bg="Black", fg = "white", bd=4)
        back_btn_viewbooking.place(x=20 , y=35, width=100)  

        #Creating Assign Button
        assign_btn = Button(self.level, text = " Assign ",command=self.assing_driver_data,font=("times new roman", 13, "bold"), bg="Black", fg = "skyBlue", bd=4)
        assign_btn.place(x=1200, y=580, width=150, height=45)

        #Creating Cancel Button
        assign_btn = Button(self.level, text = " Cancel ",command=self.cancel_data,font=("times new roman", 13, "bold"), bg="Black", fg = "skyBlue", bd=4)
        assign_btn.place(x=550, y=580, width=150, height=45)

        

    