from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()




from tkinter import *
from PIL import Image, ImageTk

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load and Resize Image to Match Window Size
        img = Image.open("C:/Users/PARTHIB MANDAL/OneDrive/Desktop/outerinterface.jpg")
        img = img.resize((1550, 800), Image.Resampling.LANCZOS)  # Resize to window dimensions
        self.bg = ImageTk.PhotoImage(img)

        # Set Background
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550, height=800)  # Ensure it fills the entire window
        

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1=Image.open("C:/Users/PARTHIB MANDAL/OneDrive/Desktop/person.jpg")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        

        get_str=Label(frame,text="Get Started",font=("time new roman",20,"bold"),fg="white",bg="black")

        get_str.place(x=95,y=100)

        #==label

        username=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")

        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        
        password=Label(frame,text="Password",font=("time new roman",15,"bold"),fg="white",bg="black")

        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)




        #===icon image===
        
        img2=Image.open("C:/Users/PARTHIB MANDAL/OneDrive/Desktop/person1.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        
        img3=Image.open("C:/Users/PARTHIB MANDAL/OneDrive/Desktop/pass.jpg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)


      #==login button==
        loginbtn=Button(frame,command=self.login,text="Login",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #==register button==

        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("time new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #==forgot==
        
        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("time new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=370,width=160)




    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


   


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            onn = mysql.connector.connect(host="localhost", user="root", password="123456", database="management")
            my_cursor = onn.cursor()

            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                          self.txtuser.get(),
                          self.txtpass.get()
        ))

            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)

            onn.commit()
            onn.close()
    
#====reset pass window===============
    # def reset_pass(self):
    #     if self.combo_security_Q.get()=="select":
    #         messagebox.showerror("Error","Select security question")
    #     elif self.txt_security.get()=="":
    #          messagebox.showerror("Error","Please enter answer")
    #     elif self.txt_newpass.get()=="":
    #          messagebox.showerror("Error","Please enter newpassword")
    #     else:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="management")
    #         my_cursor =conn.cursor()
    #         qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
    #         vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
    #         my_cursor.execute(qury,vlaue)
    #         row=my_cursor.fetchone()

    #         if row==None:
    #             messagebox.showerror("Error","Please enter correct Answer")
    #         else:
    #             qury=("update register set password=%s where email=%s")
    #             value=(self.txt_newpass.get(),self.txtuser.get())
    #             my_cursor.execute(qury,value)


    #             conn.commit()
    #             conn.close()
    #             messagebox.showinfo("Info","Your password has been reset please login with new Password")






    def reset_pass(self):
        if self.combo_security_Q.get() == "select":
            messagebox.showerror("Error", "Select security question",parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="management")
            my_cursor = conn.cursor()
            qury = "select * from register where email=%s and securityQ=%s and securityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())  # Fixed `.get()`
            my_cursor.execute(qury, value)
            row = my_cursor.fetchone()

        if row is None:  # Fixed condition
            messagebox.showerror("Error", "Please enter correct Answer",parent=self.root2)
        else:
            qury = "update register set password=%s where email=%s"
            value = (self.txt_newpass.get(), self.txtuser.get())
            my_cursor.execute(qury, value)

            conn.commit()
            conn.close()
            messagebox.showinfo("Info", "Your password has been reset. Please login with the new password.",parent=self.root2)
            self.root2.destroy()


            
    




    
 #=====forgot pass window==========

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter Email to Reset Password")
        



        else:
             conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="management")
             my_cursor = conn.cursor()
             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()


             if row==None:
                 messagebox.showerror("My Error","Please enter valid user name")
             else:
                 conn.close()
                 self.root2=Toplevel()
                 self.root2.title("Forgot Password")
                 self.root2.geometry("340x450+610+170")


                 l=Label(self.root2,text="Forgot Password",font=("time new roman",20,"bold"),fg="red",bg="white")
                 l.place(x=0,y=10,relwidth=1)     


                        
                 security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")

                 security_Q.place(x=50,y=80)

                 self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                 self.combo_security_Q["values"]=("select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                 self.combo_security_Q.place(x=50,y=110,width=250)

                 self.combo_security_Q.current(0)
                
                 security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")

                 security_A.place(x=50,y=150)


                
                

                 self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                 self.txt_security.place(x=50,y=180,widt=250)



                 new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")

                 new_password.place(x=50,y=220)


                
                

                 self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                 self.txt_newpass.place(x=50,y=250,widt=250)


                 btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                 btn.place(x=100,y=290)






                 
                         



           














class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("register")
        self.root.geometry("1600x900+0+0")

#=====variable===================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        

 #=====backgnd img==========
        self.bg=ImageTk.PhotoImage(file="C:/Users/PARTHIB MANDAL/OneDrive/Desktop/hotelimg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)



          
 #=====left img==========
        self.bg1=ImageTk.PhotoImage(file="C:/Users/PARTHIB MANDAL/OneDrive/Desktop/dog.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
   

   #========main fraim=========

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

#==========label and entry===


#============row1==============
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")

        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)



        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")

        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
#==========row2=================


        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")

        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)


        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")

        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,widt=250)



        #==========row3=================


        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")

        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)

        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")

        security_A.place(x=370,y=240)


        
        

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,widt=250)




        #==========row4=================


        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")

        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)


        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")

        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,widt=250)
   #===check button===============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)

        checkbtn.place(x=50,y=380)

#============buttons===================
        img=Image.open("C:/Users/PARTHIB MANDAL/OneDrive/Desktop/register.jpg")
        img=img.resize((200,50), Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)


        img1=Image.open("C:/Users/PARTHIB MANDAL/OneDrive/Desktop/login.jpg")
        img1=img1.resize((200,50), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=200)

        #=======function declaration====
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
    
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be the same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="management")
            my_cursor = conn.cursor()  

            query = "SELECT * FROM register WHERE email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)

            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, try another Email")
            else:
                my_cursor.execute("INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                                                                             self.var_fname.get(),
                                                                             self.var_lname.get(),
                                                                             self.var_contact.get(),
                                                                             self.var_email.get(),
                                                                             self.var_securityQ.get(),
                                                                             self.var_securityA.get(),
                                                                             self.var_pass.get()
        )) 

            conn.commit()  
            conn.close() 
            messagebox.showinfo("Success", "Registered Successfully")  








    def return_login(self):
        self.root.destroy()

     
# class HotelManagementSystem:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Hospital Management System")
#         self.root.geometry("1550x800+0+0")
#            # ======= 1st image =======
#         img1=Image.open("C:/Users/PARTHIB MANDAL/Downloads/open_interface.jpg")
#         img1=img1.resize((1550,140),Image.LANCZOS)
#         self.photoimg1=ImageTk.PhotoImage(img1)
#         lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
#         lblimg.place(x=0,y=0,width=1550,height=140)

#         # ==========logo =========
#         img2=Image.open("C:/Users/PARTHIB MANDAL/Downloads/logo.png")
#         img2=img2.resize((230,140),Image.LANCZOS)
#         self.photoimg2=ImageTk.PhotoImage(img2)
#         lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
#         lblimg.place(x=0,y=0,width=230,height=140)
           
#         # ==========title ===============
#         lbl_title=Label(self.root,text="PARTHIB's HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
#         lbl_title.place(x=0,y=140,width=1550,height=50)

#         # ==========main frame==========
#         main_frame=Frame(self.root,bd=4,relief=RIDGE)
#         main_frame.place(x=0,y=190,width=1550,height=620)
#         # ==========menu==========
#         lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
#         lbl_menu.place(x=0,y=0,width=230)

#         # ==========btn frame==========
#         btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
#         btn_frame.place(x=0,y=35,width=228,height=190)

#         cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
#         cust_btn.grid(row=0,column=0)

#         room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
#         room_btn.grid(row=1,column=0,pady=1)

#         details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
#         details_btn.grid(row=2,column=0,pady=1)

#         report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
#         report_btn.grid(row=3,column=0,pady=1)


#         logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
#         logout_btn.grid(row=4,column=0,pady=1)





#         #===============right side image=============

#         img3=Image.open("C:/Users/PARTHIB MANDAL/Downloads/inside.jpg")
#         img3=img3.resize((1310,590),Image.LANCZOS)
#         self.photoimg3=ImageTk.PhotoImage(img3)
#         lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
#         lblimg1.place(x=225,y=0,width=1310,height=590)



#         #================down image============

#         img4=Image.open("C:/Users/PARTHIB MANDAL/Downloads/hotel.jpg")
#         img4=img4.resize((230,210),Image.LANCZOS)
#         self.photoimg4=ImageTk.PhotoImage(img4)
#         lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
#         lblimg1.place(x=0,y=225,width=230,height=210)



#         img5=Image.open("C:/Users/PARTHIB MANDAL/Downloads/food.jpg")
#         img5=img5.resize((230,190),Image.LANCZOS)
#         self.photoimg5=ImageTk.PhotoImage(img5)
#         lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
#         lblimg1.place(x=0,y=420,width=230,height=190)


#     def cust_details(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Cust_win(self.new_window)


#     def roombooking(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Roombooking(self.new_window)
        

#     def details_room(self):
#         self.new_window=Toplevel(self.root)
#         self.app=DetailsRoom(self.new_window)


   

        






if __name__ == "__main__":
    main()
