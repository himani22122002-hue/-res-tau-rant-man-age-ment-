from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import ttk ,messagebox;
import mysql.connector


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #variable
        self.var_fname=StringVar()
        self.var_lnname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_checkbutton = StringVar()



        img1 = Image.open("C:\\Users\\ADMIN\Desktop\\background.jpg")
        img1 = img1.resize((1530, 785), Image.ANTIALIAS)
        root.photoimg1 = ImageTk.PhotoImage(img1)
        lbling = Label(root, image=root.photoimg1, borderwidth=0)
        lbling.place(x=0, y=0, width=1530, height=785)

        img2 = Image.open("C:\\Users\\ADMIN\\Desktop\\welcome.jpg")
        img2 = img2.resize((470, 550), Image.ANTIALIAS)
        root.photoimg2=ImageTk.PhotoImage(img2)
        lbling = Label(root, image=root.photoimg2)
        lbling.place(x=50, y=100, width=470, height=550)

        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=100,width=800,height=550)
        register_lbl=Label(frame,text="REGISTER HERE",font=('arial', 20, 'bold'),fg="Yellow",bg="black")
        register_lbl.place(x=20,y=20)
        #lable Entry
        fname=Label(frame,text="First Name",font=('arial', 15, 'bold'),bg="black",fg="white")
        fname.place(x=50, y=100)
        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=('arial', 15, 'bold'))
        self.txt_fname.place(x=50,y=140,width=250)

        lnname = Label(frame, text="Last Name", font=('arial', 15, 'bold'), bg="black", fg="white")
        lnname.place(x=370, y=100)
        self.txt_lnname = ttk.Entry(frame,textvariable=self.var_lnname, font=('arial', 15, 'bold'))
        self.txt_lnname.place(x=370, y=140, width=250)

        contact = Label(frame, text="Contact No", font=('arial', 15, 'bold'), bg="black", fg="white")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=('arial', 15, 'bold'))
        self.txt_contact.place(x=50, y=200, width=250)


        email= Label(frame, text="Email", font=('arial', 15, 'bold'), bg="black", fg="white")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=('arial', 15, 'bold'))
        self.txt_email.place(x=370, y=200, width=250)


        securityQ = Label(frame, text="Select Security Quetions", font=('arial', 15, 'bold'), bg="black", fg="white")
        securityQ.place(x=50, y=240)
        combo_securityQ=ttk.Combobox(frame,textvariable=self.var_securityQ,font=('arial', 15, 'bold'),state="readonly")
        combo_securityQ["values"]=("Select","Your Birth Place","Your Fav Colour","Your Pet Name")
        combo_securityQ.place(x=50,y=270,width=250)
        combo_securityQ.current(0)


        securityA = Label(frame, text="Security Answer", font=('arial', 15, 'bold'), bg="black", fg="white")
        securityA.place(x=370, y=240)
        self.txt_securityA = ttk.Entry(frame,textvariable=self.var_securityA, font=('arial', 15, 'bold'))
        self.txt_securityA.place(x=370, y=270, width=250)

        password = Label(frame, text="Password", font=('arial', 15, 'bold'), bg="black", fg="white")
        password .place(x=50, y=310)
        self.txt_password = ttk.Entry(frame,textvariable=self.var_password, font=('arial', 15, 'bold'))
        self.txt_password.place(x=50, y=340, width=250)

        confirm_password = Label(frame, text="Confirm Password", font=('arial', 15, 'bold'), bg="black", fg="white")
        confirm_password.place(x=370, y=310)
        self.txt_confirm_password = ttk.Entry(frame,textvariable=self.var_confirm_password, font=('arial', 15, 'bold'))
        self.txt_confirm_password .place(x=370, y=340, width=250)
        #Chechbutton
        txt_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_checkbutton,text="I Agree The Terms and Conditions",font=('arial', 12, 'bold'),onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=380)
        #button
        img=Image.open("C:\\Users\\ADMIN\\Desktop\\regis.jpeg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=('arial', 12, 'bold'))
        b1.place(x=250,y=420,width=200)


        #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("error","All fields required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        elif self.var_checkbutton.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",auth_plugin="mysql_native_password")
            my_cursor = jyoti.cursor(buffered=True)
            Query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(Query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already Exist,please try another email")
            else:
                my_cursor.execute("insert into register(fname,lnname,contact,email,securityQ,securityA,password,confirm_password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.var_fname.get(),
                                      self.var_lnname.get(),
                                      self.var_contact.get(),
                                      self.var_email.get(),
                                      self.var_securityQ.get(),
                                      self.var_securityA.get(),
                                      self.var_password.get(),
                                      self.var_confirm_password.get(),
                                  ))
            jyoti.commit()
            jyoti.close()
            messagebox.showinfo("Success", "Register Successfully", parent=self.root)
            self.root.destroy()



if __name__ == '__main__':
    root = Tk()
    obj = register(root)
    root.mainloop()