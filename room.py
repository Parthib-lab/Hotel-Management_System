from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")




            # =====varibales===== 

        self.var_conatct=StringVar() 
        self.var_checkin=StringVar() 
        self.var_checkout=StringVar() 
        self.var_roomtype=StringVar() 
        self.var_roomavailable=StringVar() 

        self.var_meal=StringVar() 
        self.var_noofdays=StringVar() 
        self.var_paidtax=StringVar() 
        self.var_actualtotal=StringVar() 
        self.var_total=StringVar() 



















     
        
       #=================title===============
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
    # ==========logo =========
        img2=Image.open("C:/Users/PARTHIB MANDAL/Downloads/logo.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
    # ==================labelFrame============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        

         #=================labels and entrys========
        #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_conatct,font=("times new roman",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)


        #============fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=323,y=4)

        #customer check in
        lbl_cust_checkin=Label(labelframeleft,text="Check_in Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_checkin.grid(row=1,column=0,sticky=W)

        enty_checkin=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("times new roman",13,"bold"))
        enty_checkin.grid(row=1,column=1)
        #customer check out
        lbl_cust_checkout=Label(labelframeleft,text="Check_out Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_checkout.grid(row=2,column=0,sticky=W)

        enty_checkout=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("times new roman",13,"bold"))
        enty_checkout.grid(row=2,column=1)

        # room type como box
        room_type_combo=Label(labelframeleft,font=("arial",13,"bold"),text="Room Type:",padx=2,pady=6)
        room_type_combo.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()


        combo_room_type=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",13,"bold"),width=27,state="readonly")
        combo_room_type["value"]=ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)
        #avaible room
        lbl_cust_avaibleroom=Label(labelframeleft,text="Avaible Room:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_avaibleroom.grid(row=4,column=0,sticky=W)

      #   enty_avaibleroom=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable,font=("times new roman",13,"bold"))
      #   enty_avaibleroom.grid(row=4,column=1)
        conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()


        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        #customer meal
        lbl_cust_meal=Label(labelframeleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_meal.grid(row=5,column=0,sticky=W)

        enty_meal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("times new roman",13,"bold"))
        enty_meal.grid(row=5,column=1)
        #customer no of days
        lbl_cust_no_of_days=Label(labelframeleft,text="No Of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_no_of_days.grid(row=6,column=0,sticky=W)

        enty_no_of_days=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("times new roman",13,"bold"))
        enty_no_of_days.grid(row=6,column=1)
        #customer paidtax
        lbl_cust_paidtax=Label(labelframeleft,text="Paid Tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_paidtax.grid(row=7,column=0,sticky=W)

        enty_paidtax=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("times new roman",13,"bold"))
        enty_paidtax.grid(row=7,column=1)
        #customer subtotal
        lbl_cust_subtotal=Label(labelframeleft,text="Sub Total:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_subtotal.grid(row=8,column=0,sticky=W)

        enty_subtotal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("times new roman",13,"bold"))
        enty_subtotal.grid(row=8,column=1)
        #customer total cost
        lbl_cust_totalcost=Label(labelframeleft,text="Total Cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_totalcost.grid(row=9,column=0,sticky=W)

        enty_totalcost=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("times new roman",13,"bold"))
        enty_totalcost.grid(row=9,column=1)


        #bill button


        
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)








        
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



        #=====Right side image=============




        img3=Image.open("C:/Users/PARTHIB MANDAL/Downloads/bedroom.jpg")
        img3=img3.resize((520,330),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=530,height=330)







        #================tableframe search system==============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2,)
        table_frame.place(x=435,y=280,width=860,height=260)

        lblsearch_by=Label(table_frame,font=("arial",13,"bold"),text="Search By",bg="red",fg="white")
        lblsearch_by.grid(row=0,column=0,sticky=W,padx=2)
         
        self.search_var=StringVar()

        



        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
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
        details_table.place(x=0,y=50,width=860,height=180)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfDays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)



        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfDays",text="NoOfDays")




        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfDays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    #============add data===================
    def add_data(self):
        if self.var_conatct.get() == "" or self.var_checkin.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
         try:
            conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into room values(%s, %s, %s, %s, %s, %s, %s)", (



                                                                                             self.var_conatct.get(), 
                                                                                             self.var_checkin.get(), 
                                                                                             self.var_checkout.get(), 
                                                                                             self.var_roomtype.get(), 
                                                                                             self.var_roomavailable.get(), 

                                                                                             self.var_meal.get(), 
                                                                                             self.var_noofdays.get() 
                                                                                             
            ))
            conn.commit()
            self.fetch_data()

            conn.close()
            messagebox.showinfo("Success", "Room Booked", parent=self.root)
         except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
       
    
      #================fetch data====================
    def fetch_data(self):
       conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="management")
       my_cursor = conn.cursor()
       my_cursor.execute("select * from room")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
             self.room_table.insert("",END,values=i)
          conn.commit()
       conn.close()


   #================get cursor=============
    def get_cuersor(self, event=""): 
       cusrsor_row=self.room_table.focus() 
       content=self.room_table.item(cusrsor_row) 
       row=content["values"] 


       
       self.var_conatct.set(row[0])
       self.var_checkin.set(row[1])
       self.var_checkout.set(row[2])
       self.var_roomtype.set(row[3])
       self.var_roomavailable.set(row[4])

       self.var_meal.set(row[5])
       self.var_noofdays.set(row[6])


  #====update function======
    def update(self):
       if self.var_conatct.get()=="":
          messagebox.showerror("Error", "Plaease enter mobile number", parent=self.root) 
       else:
          conn=mysql.connector.connect(host="localhost", username="root", password="123456", database="management") 
          my_cursor=conn.cursor() 
          my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s", (
                            
                            self.var_checkin.get(),  # Fixed here
                            self.var_checkout.get(),
                            self.var_roomtype.get(),
                            self.var_roomavailable.get(),
                            self.var_meal.get(),
                            self.var_noofdays.get(),
                            self.var_conatct.get(),
                            
                                 ) )

          conn.commit() 
          self.fetch_data()
          conn.close() 
          messagebox.showinfo("Update", "Room details has been updated successfully",parent=self.root)
    
    
    
    #========delete===========
    def mDelete(self):
       mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
       if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management")
          my_cursor=conn.cursor()
          query="delete from room where Contact=%s"
          value=(self.var_conatct.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()



    def reset(self):
       
       self.var_conatct.set("")
       self.var_checkin.set("")
       self.var_checkout.set("")
       self.var_roomtype.set("")
       self.var_roomavailable.set("")

       self.var_meal.set("")
       self.var_noofdays.set("")
       self.var_paidtax.set("") 
       self.var_actualtotal.set("") 
       self.var_total.set("") 












      #=========================All data fetch========


    
    def Fetch_contact(self):
        if self.var_conatct.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
            my_cursor=conn.cursor() 
            query=("select Name from customer where Mobile=%s")
            value=(self.var_conatct.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)


                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)


                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)



                        #===========Gender==========
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
                my_cursor=conn.cursor() 
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()




                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)


                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
 
                 #=============email=============


                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
                my_cursor=conn.cursor() 
                query=("select Email from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()




                
                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)


                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                 #=============Nationality=============


                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
                my_cursor=conn.cursor() 
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)
                 #=============phone=============


                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
                my_cursor=conn.cursor() 
                query=("select Mobile from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblIdNumber=Label(showDataframe,text="Number:",font=("arial",12,"bold"))
                lblIdNumber.place(x=0,y=120)
                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
                 #=============adress=============


                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
                my_cursor=conn.cursor() 
                query=("select Adress from customer where Mobile=%s")
                value=(self.var_conatct.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblIdNumber=Label(showDataframe,text="Adress:",font=("arial",12,"bold"))
                lblIdNumber.place(x=0,y=150)
                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=150)
    
    #====search system==========
    def search(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="management") 
       my_cursor=conn.cursor() 
       my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
       rows=my_cursor.fetchall()
       if len (rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
             self.room_table.insert("",END,values=i)
          conn.commit()
       conn.close()







    def total(self):
       inDate=self.var_checkin.get()
       outDate=self.var_checkout.get()
       inDate=datetime.strptime(inDate,"%d/%m/%Y")
       outDate=datetime.strptime(outDate,"%d/%m/%Y")
       self.var_noofdays.set(abs(outDate-inDate).days)

       if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxory"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.1))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)



       elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxory"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.3))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.3)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

       elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxory"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)


       if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Ac"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.1))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)



       elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Ac"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.3))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.3)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

       elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Ac"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)



       if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="NonAc"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.1))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)



       elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="NonAc"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.3))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.3)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

       elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="NonAc"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)





       elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Duplex"):
          q1=float(500)
          q2=float(100)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)



       elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Duplex"):
          q1=float(500)
          q2=float(100)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)
       elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
          q1=float(500)
          q2=float(100)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)
       else:
          q1=float(500)
          q2=float(100)
          q3=float(self.var_noofdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.5))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.5)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)
          






            


        

        





if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
