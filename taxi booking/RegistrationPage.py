from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector    

class Registration:

    def __init__(self, root ):
        self.root = root 
        self.root.title("Login Page")
        self.root.geometry("1000x500")
        self.root.resizable(False,False)
        


        # Creating Frame 
        frm_rgt = Frame(self.root, bg = "Black")
        frm_rgt.place( height=500, width=1000)

        # Creating Button     
        back_btn_register = Button(self.root, text = " Back " ,command=self.back,font=("times new roman", 12), bg="Black", fg = "white", bd=4)
        back_btn_register.place(x=8 , y=10, width=100)

        title = Label(frm_rgt, text= "Registration Page ", font=("Impack", 24), fg="White", bg="Black").place(x=380,y=10)

       
        lb_name = Label(frm_rgt, text= " Name :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=55,y=120)
        self.hh_name = Entry(frm_rgt, font= ("times new roman", 14), fg="Black", bg="White")
        self.hh_name.place(x=150,y=122, width=280)  

        lb_email = Label(frm_rgt, text= " Email :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=566,y=120)
        self.hh_email = Entry(frm_rgt, font= ("times new roman", 14), fg="Black", bg="White")
        self.hh_email.place(x=656,y=122, width=280)

        lb_address = Label(frm_rgt, text= " Address :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=34,y=180)
        self.hh_address = Entry(frm_rgt, font= ("times new roman", 14), fg="Black", bg="White")
        self.hh_address.place(x=150,y=182, width=280)

        lb_gender = Label(frm_rgt, text= " Gender :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=546,y=180)
        self.hh_gender = ttk.Combobox(frm_rgt,font=("times new roman",14),foreground="black",state='readonly',justify=CENTER)
        self.hh_gender['values'] = ("Male","Female","Others")
        self.hh_gender.place(x=656,y=182, width=280)
        self.hh_gender.current(0)

        lb_contact = Label(frm_rgt, text= " Contact :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=40,y=240)
        self.hh_contact = Entry(frm_rgt, font= ("times new roman", 14), fg="Black", bg="White")
        self.hh_contact.place(x=150,y=242, width=280)

        lb_username = Label(frm_rgt, text= " Username :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=524,y=240)
        self.hh_username = Entry(frm_rgt, font= ("times new roman", 14), fg="Black", bg="White")
        self.hh_username.place(x=656,y=242, width=280)

        lb_password = Label(frm_rgt, text= " Password :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=20 ,y=300)
        self.hh_password = Entry(frm_rgt, font= ("times new roman", 14), show="*",fg="Black", bg="White")
        self.hh_password.place(x=150,y=302, width=280)
 
        lb_confirmpassword = Label(frm_rgt, text= " Confirm Password :  ", font=("times new roman ", 14), fg="White", bg="Black").place(x=450,y=300)
        self.hh_cpasssword = Entry(frm_rgt, font= ("times new roman", 14),show="*", fg="Black", bg="White")
        self.hh_cpasssword.place(x=656,y=302, width=280)

        

        regis_bt = Button(frm_rgt, text = " Register ",command = self.register_data, font=("times new roman", 11, "bold"), bg="Black", fg = "skyBlue", bd=4)
        regis_bt.place(x=450, y=420, width=100)

    def register(self):
         import LoginPage
         self.new = Toplevel()
         self.obj = LoginPage.Login(self.new)  
     
    def back(self):
        import LoginPage
        self.root.withdraw()
        self.new = Toplevel()
        self.obj = LoginPage.Login(self.new) 

    def register_data(self):
         
         if self.hh_name.get()=="" or self.hh_address.get()=="" or self.hh_contact.get()=="" or self.hh_email=="" or self.hh_password.get()=="" or self.hh_cpasssword.get()=="":
              messagebox.showerror("Error", "All Field must be filled", parent = self.root)

         elif self.hh_password.get() != self.hh_cpasssword.get():
              messagebox.showerror("Error", "Passwords does not match", parent = self.root)

         else:
              
              try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
                    cursor = conn.cursor()
     
                    cursor.execute("select * from customer where email=%s", (self.hh_email.get(),)) 
                     
                    one = cursor.fetchone()
                    
                    
                    if one!=None:   
                         messagebox.showerror("Error", "User already exist. Please user another email ! ", parent = self.root)

                    else:

                         statement = ("INSERT INTO customer (name, email, address, gender, contact, username, password, confirm) values (%s,%s,%s,%s,%s,%s,%s,%s)")
                              
                         values =  (    self.hh_name.get(),
                                        self.hh_email.get(),
                                        self.hh_address.get(),
                                        self.hh_gender.get(),
                                        self.hh_contact.get(),
                                        self.hh_username.get(),
                                        self.hh_password.get(),
                                        self.hh_cpasssword.get()
                                                  
                                        )
                         cursor.execute(statement, values) 
                                                  
                         conn.commit()
                         conn.close()
                         messagebox.showinfo("Welcome", " Registered Successfully !", parent = self.root)
                         self.register()
               

              except Exception as es:

                    messagebox.showerror("Error", f"Error due to: {str(es)}") 
             
     
        

if __name__=="__main__":
    root=Tk()
    obj = Registration(root)
    root.mainloop()
    
