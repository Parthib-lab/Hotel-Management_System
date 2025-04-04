from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
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






if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()