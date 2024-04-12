from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector    

class DRegistration():

    def __init__(self, root ):
        self.root = root 
        self.root.title("Login Page")
        self.root.geometry("1000x600")
        self.root.resizable(False,False)
        
 
        Frm_registtn = Frame(self.root, bg = "Black")
        Frm_registtn.place(height=700, width=1000)

        # Creating Button     
        bck_btn = Button(self.root, text = " Back " ,command=self.back,font=("times new roman", 12), bg="Black", fg = "white", bd=4)
        bck_btn.place(x=8 , y=10, width=100)

        #Creating frames

        title = Label(Frm_registtn, text= " Registration Page ", font=("Impack", 24), fg="White", bg="Black").place(x=380,y=10)

     

        lb_name = Label(Frm_registtn, text= " Name :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=55,y=120)
        self.df_name = Entry(Frm_registtn, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_name.place(x=150,y=122, width=280)  

        lb_email = Label(Frm_registtn, text= " Email :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=566,y=120)
        self.df_email = Entry(Frm_registtn, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_email.place(x=656,y=122, width=280)

        lb_address = Label(Frm_registtn, text= " Address :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=34,y=180)
        self.df_address = Entry(Frm_registtn, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_address.place(x=150,y=182, width=280)

        lb_gender = Label(Frm_registtn, text= " Gender :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=546,y=180)
        self.df_gender = ttk.Combobox(Frm_registtn,font=("times new roman",16),foreground="black",state='readonly',justify=CENTER)
        self.df_gender['values'] = ("Male","Female","Others")
        self.df_gender.place(x=656,y=182, width=280)
        self.df_gender.current(0)


        lb_contact = Label(Frm_registtn, text= " Contact :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=40,y=240)
        self.df_contact = Entry(Frm_registtn, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_contact.place(x=150,y=242, width=280)

        lb_username = Label(Frm_registtn, text= " Username :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=524,y=240)
        self.df_username = Entry(Frm_registtn, font= ("times new roman", 16), fg="Black", bg="White")
        self.df_username.place(x=656,y=242, width=280)

        lb_password = Label(Frm_registtn, text= " Password :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=20 ,y=300)
        self.df_password = Entry(Frm_registtn, font= ("times new roman", 16), show="*",fg="Black", bg="White")
        self.df_password.place(x=150,y=302, width=280)
 
        lb_confirmpassword = Label(Frm_registtn, text= " Confirm Password :  ", font=("times new roman ", 16), fg="White", bg="Black").place(x=450,y=300)
        self.df_cpassword = Entry(Frm_registtn, font= ("times new roman", 16),show="*", fg="Black", bg="White")
        self.df_cpassword.place(x=656,y=302, width=280)

        

        register_btn = Button(Frm_registtn, text = " Register ",command = self.dregister_data, font=("times new roman", 12, "bold"), bg="Black", fg = "skyBlue", bd=4)
        register_btn.place(x=450, y=420, width=100)
  

    def dregister_data(self):

         
         if self.df_name.get()=="" or self.df_address.get()=="" or self.df_contact.get()=="" or self.df_email=="" or self.df_password.get()=="" or self.df_cpassword.get()=="":
              messagebox.showerror("Error", "All Field must be filled", parent = self.root)

         elif self.df_password.get() != self.df_cpassword.get():
              messagebox.showerror("Error", "Passwords does not match", parent = self.root)

         else:
              
              try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxi_booking")
                    cursor = conn.cursor()
     
                    cursor.execute("select * from driver where email=%s", (self.df_email.get(),)) 
                     
                    one = cursor.fetchone()
                    
                    
                    if one!=None:   
                         messagebox.showerror("Error", "User already exist. Please user another email ! ", parent = self.root)

                    else:

                         statement = ("INSERT INTO driver (name, email, address, gender, contact, username, password, confirm,status) values (%s,%s,%s,%s,%s,%s,%s,%s,'Available')")
                              
                         values =  (    self.df_name.get(),
                                        self.df_email.get(),
                                        self.df_address.get(),
                                        self.df_gender.get(),
                                        self.df_contact.get(),
                                        self.df_username.get(),
                                        self.df_password.get(),
                                        self.df_cpassword.get()
                                                  
                                        )
                         cursor.execute(statement, values) 
                                                  
                         conn.commit()
                         conn.close()
                         messagebox.showinfo("Welcome", " Registered Successfully !", parent = self.root)
               

              except Exception as es:

                    messagebox.showerror("Error", f"Error due to: {str(es)}") 
                    
                    # root.destroy()
                    # import LoginPage
    
    def back(self):
       self.root.destroy()
       import DriverLogin
       self.new = Toplevel()
       self.obj = DriverLogin.Login(self.new)      
        

if __name__=="__main__":
    root=Tk()
    obj = DRegistration(root)
    root.mainloop()
    
