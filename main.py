from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
#from recept import recept_class
from menu import menu_win
from order import order_win

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



        exit_btn = Button(btn_frame, text='Exit', command=self.exit, width=22, font=('times new roman', 14, 'bold'),bg='black', fg='gold', bd=0, cursor='hand1')
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
    def exit(self):
        self.root.destroy()




if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
