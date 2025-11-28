from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
from menu import menu_win
from order import order_win
import mysql.connector
#from main import HotelManagementSystem
#import data
from tkinter import messagebox
#from tkinter import ttk



def main():
    win=Tk()
    app=Login_win(win)
    win.mainloop()




class Login_win:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.geometry('1550x800+0+0')
        self.var_email = StringVar()
        self.var_password = StringVar()


        img1 = Image.open("C:\\Users\\ADMIN\\Desktop\\image.jpg")
        img1 = img1.resize((1530, 785), Image.ANTIALIAS)
        root.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(root, image=root.photoimg1,borderwidth=0)
        lbling.place(x=0, y=0, width=1530, height=785)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width='340',height='450')
        img2=Image.open("C:\\Users\\ADMIN\\Desktop\\login.jpeg")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbling = Label(image=self.photoimg2, bg="black", bd=4, relief=RIDGE)
        lbling.place(x=730, y=175, width=100, height=100)

        labelTitle = Label(frame, text='Get Started', font=('arial', 20, 'bold'), fg='white',bd=11, bg='black')
        labelTitle.place(x=78, y=100)
        username = Label(frame, text='User Name', font=('arial', 15, 'bold'), fg='white', bd=11, bg='black')
        username.place(x=60, y=155)
        self.textuser=ttk.Entry(frame, font=('arial', 15, 'bold'))
        self.textuser.place(x=40,y=200,width=270)
        password = Label(frame, text='Password', font=('arial', 15, 'bold'), fg='white', bd=11, bg='black')
        password.place(x=60, y=235)
        self.passwordentry = ttk.Entry(frame, font=('arial', 15, 'bold'))
        self.passwordentry.place(x=40, y=280, width=270)

        img3 = Image.open("C:\\Users\\ADMIN\\Desktop\\login.jpeg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lbling = Label(image=self.photoimage3, bg='black', borderwidth=0)
        lbling.place(x=650, y=335, width=25, height=25)

        img4 = Image.open("C:\\Users\\ADMIN\\Desktop\\password.jpeg")
        img4 = img4.resize((25, 25), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        lbling = Label( image=self.photoimage4, bg='black', borderwidth=0)
        lbling.place(x=650, y=417, width=25, height=25)
        #LoginButton

        login_btn=Button(frame,text="LOGIN",font=('arial', 15, 'bold'),bd=3,relief=RIDGE,command=self.login, fg="white",bg="red", activeforeground="white" ,activebackground="red")
        login_btn.place(x=110,y=325,width=120,height=35)
        #registerbutton
        register_btn = Button(frame, text="New User Register",command=self.Register_window,font=('arial', 10, 'bold'),borderwidth=0, fg="white", bg="black", activeforeground="black", activebackground="black")
        register_btn.place(x=15, y=365, width=160)
        #forgetpassword
        login_btn = Button(frame, text="Forget Password", font=('arial', 10, 'bold'),borderwidth=0,command=self.forget_password_window, fg="white", bg="black", activeforeground="black",activebackground="black")
        login_btn.place(x=10, y=388, width=160)
    def Register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)





###############################################login###################################################
    def login(self):
        if self.textuser.get()=="" or self.passwordentry.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.textuser.get()==""and self.passwordentry.get()=="":
            messagebox.showinfo("success","welcome in restaurant managemeng")
        else:
            jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",auth_plugin="mysql_native_password")
            my_cursor = jyoti.cursor(buffered=True)
            email = self.textuser.get()
            password = self.passwordentry.get()
            sql = "select * from register where email=%s and password=%s"
            my_cursor.execute(sql, [(email), (password)])
            results = my_cursor.fetchone()
            if results==None:
                messagebox.showerror("error", "invalid username &password")
            else:
                open_main = messagebox.askyesno("yesno", "access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app =HotelManagementSystem (self.new_window )
                else:
                    if not open_main:
                        return
                jyoti.commit()
                jyoti.close()



#################################### reset password ##############################################


    def reset_pass(self):
        if self.combo_securityQ.get()=="select":
            messagebox.showerror("Error","select the security question")
        elif self.txt_securityA.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",auth_plugin="mysql_native_password")
            my_cursor = jyoti.cursor(buffered=True)
            Query=("select *from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.combo_securityQ.get(),self.txt_securityA.get(),)
            my_cursor.execute(Query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter the correct answer",parent=self.root2)
            else:
                Query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.textuser.get())
                my_cursor.execute(Query,value)
                jyoti.commit()
                jyoti.close()
                messagebox.showinfo("info","your password has been reset , please login new password",parent=self.root2)
                self.root2.destroy()

######################forget password####################################################################

    def forget_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","please enter the email adress to reset password")
        else:
            jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",auth_plugin="mysql_native_password")
            my_cursor = jyoti.cursor(buffered=True)
            Query=("select * from register where email =%s")
            value=(self.textuser.get(),)
            my_cursor.execute(Query,value)
            row=my_cursor.fetchone()
            #print(row)'
            if row== None:
                messagebox.showerror("my error","please enter the valid user name")
            else:
                jyoti.close()
                self.root2=Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password", font=('arial', 20, 'bold'),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                securityQ = Label(self.root2, text="Select Security Quetions", font=('arial', 15, 'bold'), bg="black",fg="white")
                securityQ.place(x=50, y=80)
                self.combo_securityQ = ttk.Combobox(self.root2,  font=('arial', 15, 'bold'),state="readonly")
                self.combo_securityQ["values"] = ("Select", "Your Birth Place", "Your Fav Colour", "Your Pet Name")
                self.combo_securityQ.place(x=50, y=110, width=250)
                self.combo_securityQ.current(0)

                securityA = Label(self.root2, text="Security Answer", font=('arial', 15, 'bold'), bg="black", fg="white")
                securityA.place(x=50, y=150)
                self.txt_securityA = ttk.Entry(self.root2, font=('arial', 15, 'bold'))
                self.txt_securityA.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="new password", font=('arial', 15, 'bold'), bg="black",fg="white")
                new_password .place(x=50, y=220)
                self.txt_new_password = ttk.Entry(self.root2, font=('arial', 15, 'bold'))
                self.txt_new_password .place(x=50, y=250, width=250)
                btn=Button(self.root2,text="Reset",command= self.reset_pass,font=('arial', 15, 'bold'),bg="green",fg="white")
                btn.place(x=100,y=290)


############################ register ######################################################################################

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
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("error", "All fields required")
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_checkbutton.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions", parent=self.root)
        else:
            jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",
                                            auth_plugin="mysql_native_password")
            my_cursor = jyoti.cursor(buffered=True)
            Query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(Query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already Exist,please try another email")
            else:
                my_cursor.execute(
                    "insert into register(fname,lnname,contact,email,securityQ,securityA,password,confirm_password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
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


############################################# main ##################################################################

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("RESTAURANT MANAGEMENT SYSTEM")
        self.root.geometry('1550x800+0+0')



        # =======img1=======
        img1 = Image.open("C:\\Users\\ADMIN\\Desktop\\Screenshot (303).png")
        img1 = img1.resize((1530,190), Image.ANTIALIAS)
        root.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(root, image=root.photoimg1, bd=4, relief=RIDGE)
        lbling.place(x=0, y=0, width=1530, height=190)

        # =======logo1=========
        img2 = Image.open("C:\\Users\\ADMIN\\Desktop\\ice.jpg")
        img2 = img2.resize((150, 325), Image.ANTIALIAS)
        root.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(root, image=root.photoimg2, bd=4, relief=RIDGE)
        lbling.place(x=1, y=1, width=150, height=325)

        # =========title========

        lbl_title = Label(root, text=" RESTAURANT  MANAGEMENT SYSTEM", font=('times new roman', 40, 'bold'), bg='black',fg='gold', bd=5, relief=RIDGE)
        lbl_title.place(x=1, y=165, width=1530, height=55)

        # ==========frame===========

        main_frame = Frame(root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=213, width=1550, height=1050)
        # ==========lbl==========

        lbl_menu = Label(main_frame, text="WELCOME", font=('times new roman', 20, 'bold'), bg='black', fg='gold', bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ==========lbl==========

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=450)

        cust_btn = Button(btn_frame, text='Menu', command=self.menu_win, width=22, font=('times new roman', 14, 'bold'),bg='black', fg='gold', bd=0, cursor='hand1')
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text='Order', command=self.order_win, width=22,font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, cursor='hand1')
        room_btn.grid(row=1, column=0, pady=1)

        '''bill_btn = Button(btn_frame, text='Bill', command='', width=22, font=('times new roman', 14, 'bold'),bg='black', fg='gold', bd=0, cursor='hand1')
        bill_btn.grid(row=2, column=0, pady=1)'''

        exit_btn = Button(btn_frame, text='Exit', command='', width=22, font=('times new roman', 14, 'bold'),bg='black', fg='gold', bd=0, cursor='hand1')
        exit_btn.grid(row=2, column=0, pady=1)


        # ============right side image=-=========

        img3 = Image.open("C:\\Users\\ADMIN\\Desktop\\roti.jpg")
        img3 = img3.resize((1300, 569), Image.ANTIALIAS)
        root.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=root.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1300, height=569)

        # ============down img1=======

        img4 = Image.open("C:\\Users\\ADMIN\\Desktop\\cake.jpg")
        img4 = img4.resize((230, 280), Image.ANTIALIAS)
        root.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame, image=root.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=150, width=230, height=280)

        # ============down img2=======

        img5 = Image.open("C:\\Users\\ADMIN\\Desktop\\ice.jpg")
        img5 = img5.resize((230, 280), Image.ANTIALIAS)
        root.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame, image=root.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=350, width=230, height=280)

    def menu_win(self):
        self.new_window=Toplevel(self.root)
        self.app=menu_win(self.new_window)
    def order_win(self):
        self.new_window=Toplevel(self.root)
        self.app=order_win(self.new_window)


if __name__ == '__main__':
    main()
