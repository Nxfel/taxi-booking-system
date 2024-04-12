
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox

import mysql.connector

class Login:
    def __init__(self, root ):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("440x500")
        self.root.resizable(False,False)
        
 
        

        # Creating Frame 
        frame_ll = Frame(self.root, bg = "Black")
        frame_ll.place(height=550, width=450)

        title = Label(frame_ll, text= "Log In ", font=("Impack", 33), fg="White", bg="Black").place(x=10,y=10)

        self.lb_usename = Label(frame_ll, text= " Username :  ", font=("Impack", 16), fg="White", bg="Black").place(x=10,y=200)
        self.df_usename = Entry(frame_ll, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_usename.place(x=138,y=200, width=240)

        lb_pwd = Label(frame_ll, text= " Password :  ", font=("Impack", 16), fg="White", bg="Black").place(x=10,y=260)
        self.df_passwrd = Entry(frame_ll, font= ("times new roman", 16),show="*", fg="black", bg="White")
        self.df_passwrd .place(x=138,y=260, width=240)

        lg_bt = Button(frame_ll,text = "LogIn ",font=("Impack", 16),command=self.login_function, bg="gray", fg = "Black" , bd=1)
        lg_bt.place(x=165, y=330, height=30, width=75)

        lg_bt = Button(frame_ll,text = "Driver LogIn ",font=("Impack", 16),command=self.driverlgn, bg="gray", fg = "Black" , bd=1)
        lg_bt.place(x=25, y=100, height=30, width=150)

        

        lb_su = Label(frame_ll, text="No account?  Signup here", bg="Black", fg="White", font=("times new roman", 12))
        lb_su.place(x=110,y=380)

        signup_butn = Button(frame_ll, text = " SignUp " ,command=self.signup,  font=("times new roman", 12), bg="Black", fg = "green", bd=1)
        signup_butn.place(x=150, y=400)

        
    
    
    def signup(self):
        import RegistrationPage
        self.root.withdraw()
        self.new = Toplevel()
        self.obj = RegistrationPage.Registration(self.new) 

    def driverlgn(self):
        import DriverLogin
        self.root.withdraw()
        self.new = Toplevel()
        self.obj =DriverLogin.Login(self.new) 

    def log(self, username):
        import CustomerDashboard
        self.root.withdraw()
        self.new = Toplevel()
        self.obj = CustomerDashboard.Customerdashboard(self.new,username) 


    def admin(self,username):
        import AdminDashboard
        self.root.withdraw()
        self.new = Toplevel()
        self.obj = AdminDashboard.Admindashboard(self.new,username) 

    def dash(self,username):
        import DriverDashboard
        self.root.withdraw()
        self.new = Toplevel()
        self.obj = DriverDashboard.Driver_Dashboard(self.new,username)        
    


    def login_function(self):
        username = self.df_usename.get()
        password = self.df_passwrd.get()


        if self.df_usename.get()=="" or self.df_passwrd.get()=="":
            messagebox.showerror("Error"," All fields should be filled", parent=self.root)
            
        elif username=="admin" and password=="admin":
            self.admin(username)

            
        

        else:

            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
                cursor = conn.cursor()
     
                cursor.execute("select * from customer where username=%s and password = %s", (self.df_usename.get(),self.df_passwrd.get(),)) 
                
                     
                row = cursor.fetchone()
                    
                    
                

            
                if row:
                    messagebox.showinfo("Welcome", f"Welcome to our application,{self.df_usename.get()}\n") 
                    self.log(username)
                        # dash = Toplevel()      
                        # Customerdashboard(dash) 
                else:
                    messagebox.showerror('Error','email and password does not match')
                    


            except Exception as es:

                messagebox.showerror("Error", f"Error due to: {str(es)}") 

            
#MainMethod      
if __name__=="__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()