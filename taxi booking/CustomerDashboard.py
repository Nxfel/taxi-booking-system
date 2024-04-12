from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Customerdashboard:
    def __init__(self,root,username):
        self.root = root
        self.username = username
        self.root.title("Customer DashBoard")
        self.root.geometry("1200x600")
        self.root.resizable(False,False)
  


        viewbooking_btt = Button(self.root, text = " View Booking",command=self.view_book,font=("times new roman", 12, "bold"), bg="Black", fg = "green", bd=3)
        viewbooking_btt.place(x=80, y=10, width=110)


        logout_btt = Button(self.root, text = " Log Out ",command=self.logout,font=("times new roman", 12, "bold"), bg="Black", fg = "green", bd=3)
        logout_btt.place(x=1050, y=10, width=110)

        booking_btt = Button(self.root, text = " Book A Trip ", command=self.book, font=("times new roman", 12, "bold"), bg="Black", fg = "green", bd=3) 
        booking_btt.place(x=520, y=520, width=150)

        self.root.mainloop()

        
        
    def book(self):
      import Booking
      self.new = Toplevel()
      self.obj = Booking.Booking_Page(self.new, username=self.username)
    
    def view_book(self):
      import ViewBooking
      self.new = Toplevel()
      self.obj = ViewBooking.Viewbooking(self.new, username=self.username)
    
    def logout(self):
      
      import LoginPage
      self.root.destroy()
      self.new = Toplevel()
      self.obj = LoginPage.Login(self.new)  
      