
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
        Frm_li = Frame(self.root, bg = "Black")
        Frm_li.place(height=550, width=450)

        title = Label(Frm_li, text= "Driver Log In ", font=("Impack", 33), fg="White", bg="Black").place(x=10,y=10)

        self.lb_usename = Label(Frm_li, text= " Username :  ", font=("Impack", 16), fg="White", bg="Black").place(x=10,y=200)
        self.df_usename = Entry(Frm_li, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_usename.place(x=138,y=200, width=240)

        lb_pwd = Label(Frm_li, text= " Password :  ", font=("Impack", 16), fg="White", bg="Black").place(x=10,y=260)
        self.df_passwrd = Entry(Frm_li, font= ("times new roman", 16),show="*", fg="black", bg="White")
        self.df_passwrd .place(x=138,y=260, width=240)

        lg_bt = Button(Frm_li,text = "LogIn ",font=("Impack", 16),command=self.login_function, bg="gray", fg = "Black" , bd=1)
        lg_bt.place(x=165, y=330, height=30, width=75)

        back_bt = Button(Frm_li,text = "Back",font=("Impack", 16),command=self.Back, bg="gray", fg = "Black" , bd=1)
        back_bt.place(x=45, y=330, height=30, width=75)

        

        lb_su = Label(Frm_li, text="No account?  Signup here", bg="Black", fg="White", font=("times new roman", 12))
        lb_su.place(x=110,y=380)

        signup_butn = Button(Frm_li, text = " SignUp " ,command=self.signup,  font=("times new roman", 12), bg="Black", fg = "skyBlue", bd=0)
        signup_butn.place(x=150, y=400)

    def signup(self):
        import Dregistration
        self.root.withdraw()
        self.new = Toplevel()
        self.obj =Dregistration.DRegistration(self.new) 


    def Back(self):
      self.root.destroy()
      import LoginPage
      self.new = Toplevel()
      self.obj = LoginPage.Login(self.new)  

  

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


            
        

        else:


            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
                cursor = conn.cursor()
     
                cursor.execute("select * from driver where username=%s and password = %s", (self.df_usename.get(),self.df_passwrd.get(),)) 
                
                     
                row = cursor.fetchone()
                    
                    
                
 

            

                messagebox.showinfo("Welcome", f"Welcome to our application,{self.df_usename.get()}\n") 
                self.dash(username)
                    # dash = Toplevel()      
                    # Customerdashboard(dash) 
                    


            except Exception as es:

                messagebox.showerror("Error", f"Error due to: {str(es)}") 

    
#MainMethod      
if __name__=="__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()