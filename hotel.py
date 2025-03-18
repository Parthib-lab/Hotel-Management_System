from tkinter import* 
from PIL import Image,ImageTk #pip install pillow
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom
import sys  # Add this at the top of your file
import os

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")
           # ======= 1st image =======
        img1=Image.open("C:/Users/PARTHIB MANDAL/Downloads/open_interface.jpg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # ==========logo =========
        img2=Image.open("C:/Users/PARTHIB MANDAL/Downloads/logo.png")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
           
        # ==========title ===============
        lbl_title=Label(self.root,text="IMPERIAL ORCHIRD",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ==========main frame==========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        # ==========menu==========
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        # ==========btn frame==========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="Scanner",command=self.show_image,width=22,font=("times new roman",14,"bold"),bg="blue",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)


        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="red",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="red",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=5,column=0,pady=1)


        #===============right side image=============

        img3=Image.open("C:/Users/PARTHIB MANDAL/Downloads/inside.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)



        #================down image============

        img4=Image.open("C:/Users/PARTHIB MANDAL/Downloads/hotel.jpg")
        img4=img4.resize((240,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=230,width=230,height=240)





        
# # Open the image
#         img4 = Image.open("C:/Users/PARTHIB MANDAL/Downloads/hotel.jpg")

# # Crop from the top (adjust values as needed)
#         crop_height = 50  # Change this value to crop more or less
#         img4 = img4.crop((0, crop_height, img4.width, img4.height))  

# # Resize the cropped image
#         img4 = img4.resize((240, 210), Image.LANCZOS)

# # Convert to Tkinter-compatible format
#         photoimg4 = ImageTk.PhotoImage(img4)

# # Create and place the label
#         lblimg1 = Label(main_frame, image=photoimg4, bd=4, relief=RIDGE)
#         lblimg1.place(x=0, y=230, width=230, height=240)



        img5=Image.open("C:/Users/PARTHIB MANDAL/Downloads/food.jpg")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
    


    

    def logout(self):
        self.root.destroy()  # Close the hotel management window
        os.system("python login.py")  # Reopen login window

    


    def show_image(self):
        image_path = "C:/Users/PARTHIB MANDAL/OneDrive/Desktop/my_scanner.jpg"

        if not os.path.exists(image_path):
            print("Error: Image file not found!")
            return
   

        img_window = Toplevel(self.root)
        img_window.title("Image Viewer")
        img_window.geometry("600x500")

        # Load and display the image
        img = Image.open(image_path)
        img = img.resize((500, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        img_label = Label(img_window, image=photo)
        img_label.image = photo  # Keep reference to avoid garbage collection
        img_label.pack(pady=10)





if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
