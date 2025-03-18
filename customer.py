from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox






class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")


        #=========variables===========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()



       #=================title===============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
    # ==========logo =========
        img2=Image.open("C:/Users/PARTHIB MANDAL/Downloads/logo.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        # ==================labelFrame============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        #=================labels and entrys========
        #customer ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("times new roman",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)



        #customer name
        cname=Label(labelframeleft,font=("arial",13,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)
       

        #customer mother name
        mothername=Label(labelframeleft,font=("arial",13,"bold"),text="Mother Name:",padx=2,pady=6)
        mothername.grid(row=2,column=0,sticky=W)

        txtmother=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmother.grid(row=2,column=1)

        # gender combo box
        gender_combo=Label(labelframeleft,font=("arial",13,"bold"),text="Gender:",padx=2,pady=6)
        gender_combo.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",13,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Mail","Femail","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


           #customer post code
        postcode=Label(labelframeleft,font=("arial",13,"bold"),text="Pincode:",padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)

        txtpost=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtpost.grid(row=4,column=1)
           #customer mobile
        mobile=Label(labelframeleft,font=("arial",13,"bold"),text="Mobile no:",padx=2,pady=6)
        mobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtmobile.grid(row=5,column=1)
           #customer email
        mail=Label(labelframeleft,font=("arial",13,"bold"),text="Email:",padx=2,pady=6)
        mail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)


        
         # nationality combo box
        nationaliy_combo=Label(labelframeleft,font=("arial",13,"bold"),text="Nationality:",padx=2,pady=6)
        nationaliy_combo.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",13,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("Indian","American","Briten","Rasian")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
         
         # id_type combo box
        id_type=Label(labelframeleft,font=("arial",13,"bold"),text="Id Proof Tupe:",padx=2,pady=6)
        id_type.grid(row=8,column=0,sticky=W)
        combo_id_type=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",13,"bold"),width=27,state="readonly")
        combo_id_type["value"]=("Aadhar card","Pan card","Driving Licence")
        combo_id_type.current(0)
        combo_id_type.grid(row=8,column=1)




        #customer id number
        id_number=Label(labelframeleft,font=("arial",13,"bold"),text="Id Number:",padx=2,pady=6)
        id_number.grid(row=9,column=0,sticky=W)

        txt_id_no=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txt_id_no.grid(row=9,column=1)
        #customer Adress
        adress=Label(labelframeleft,font=("arial",13,"bold"),text="Adress:",padx=2,pady=6)
        adress.grid(row=10,column=0,sticky=W)

        txt_adress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txt_adress.grid(row=10,column=1)


        #=======================btns==============
        btns_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btns_frame.place(x=0,y=400,width=412,height=40)



        btnAdd=Button(btns_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btns_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btns_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btns_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #================tableframe search system==============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2,)
        table_frame.place(x=435,y=50,width=860,height=490)

        lblsearch_by=Label(table_frame,font=("arial",13,"bold"),text="Search By",bg="red",fg="white")
        lblsearch_by.grid(row=0,column=0,sticky=W,padx=2)
         
        self.search_var=StringVar()

        



        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)


        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        
        btnsearch=Button(table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)



       
        btnshowall=Button(table_frame,text="Showall",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)



        # ==========show data table=============
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","adress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)



        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("adress",text="Adress")



        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("adress",width=100)
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
   


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
         try:
            conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.var_ref.get(),
                self.var_cust_name.get(),  # Fixed here
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get()
            ))
            conn.commit()
            self.fetch_data()

            conn.close()
            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
         except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    def fetch_data(self):
       conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="management")
       my_cursor = conn.cursor()
       my_cursor.execute("select * from customer")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
          self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
          for i in rows:
             self.Cust_Details_Table.insert("",END,values=i)
          conn.commit()
       conn.close()
    def get_cuersor(self, event=""): 
       cusrsor_row=self.Cust_Details_Table.focus() 
       content=self.Cust_Details_Table.item(cusrsor_row) 
       row=content["values"] 


       self.var_ref.set(row[0]),
       self.var_cust_name.set(row[1]),
       self.var_mother.set(row[2]),
       self.var_gender.set(row[3]),
       self.var_post.set(row[4]),
       self.var_mobile.set(row[5]),
       self.var_email.set(row[6]),
       self.var_nationality.set(row[7]),
       self.var_id_proof.set(row[8]),
       self.var_id_number.set(row[9]),
       self.var_address.set(row[10])
    def update(self):
       if self.var_mobile.get()=="":
          messagebox.showerror("Error", "Plaease enter mobile number", parent=self.root) 
       else:
          conn=mysql.connector.connect(host="localhost", username="root", password="123456", database="management") 
          my_cursor=conn.cursor() 
          my_cursor.execute("update customer set Name=%s,Mother Name=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Id Proof=%s,Id Number=%s,Adress=%s,where Ref=%s", (
                            
                            self.var_cust_name.get(),  # Fixed here
                            self.var_mother.get(),
                            self.var_gender.get(),
                            self.var_post.get(),
                            self.var_mobile.get(),
                            self.var_email.get(),
                            self.var_nationality.get(),
                            self.var_id_proof.get(),
                            self.var_id_number.get(),
                            self.var_address.get(),
                            self.var_ref.get(),
                            
                                 ) )

          conn.commit() 
          self.fetch_data()
          conn.close() 
          messagebox.showinfo("Update", "customer details has been updated successfully",parent=self.root)
    
    
    
    
    def mDelete(self):
       mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
       if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
          my_cursor=conn.cursor()
          query="delete from customer where Ref=%s"
          value=(self.var_ref.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()
    def reset(self):
       
       #self.var_ref.set(""),
       self.var_cust_name.set(""),
       self.var_mother.set(""),
       #self.var_gender.set(""),
       self.var_post.set(""),
       self.var_mobile.set(""),
       self.var_email.set(""),
       #self.var_nationality.set(""),
       #self.var_id_proof.set(""),
       self.var_id_number.set(""),
       self.var_address.set("")
       
       x=random.randint(1000,9999)
       self.var_ref.set(str(x))
    def search(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
       my_cursor=conn.cursor() 
       my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
       rows=my_cursor.fetchall()
       if len (rows)!=0:
          self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
          for i in rows:
             self.Cust_Details_Table.insert("",END,values=i)
          conn.commit()
       conn.close()



         




         
       

if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()