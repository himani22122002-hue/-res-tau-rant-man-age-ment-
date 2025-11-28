from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image

class menu_win:
    def __init__(self,root):
        self.root=root
        self.root.title('MENU FOR RESTAURANT')
        self.root.geometry('700x450+230+245')
        '''root = Tk()
        root.geometry('510x360+0+0')
        root.resizable(0, 0)
        root.title('MENU')'''
        root.config(bg='black')
        topframe = Frame(root, bd=12, relief=RIDGE, bg='Yellow')
        topframe.pack(side=TOP)
        labeltitle = Label(topframe, text='MENU FOR RESTAURANT', font=('arial', 18), fg='yellow', bg='black', bd=10,
                           width=47)
        labeltitle.grid(row=0, column=0)
        menuframe = Frame(root, bd=12, relief=RIDGE, bg='yellow')
        menuframe.pack()
        '''img3 = Image.open("C:\\Users\\91875\\Desktop\\roti.jpg")
        img3 = img3.resize((1300, 1000), Image.ANTIALIAS)
        root.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(menuframe, image=root.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1300, height=1000)'''

        foodframe = LabelFrame(menuframe, text='Food', font=('arial', 18, 'bold'), bd=10, relief=RIDGE,width=100,height=150,bg='black',fg='white')
        foodframe.pack(side=LEFT)

        drinkframe = LabelFrame(menuframe, text='Drinks', font=('arial', 18, 'bold'), bd=10, relief=RIDGE,width=100,height=150,bg='black',fg='white')
        drinkframe.pack(side=LEFT)

        cakesframe = LabelFrame(menuframe, text='Cakes', font=('arial', 18, 'bold'), bd=10, relief=RIDGE,width=100,bg='black',fg='white')
        cakesframe.pack(side=LEFT)

        roti = Label(foodframe, text='Roti-10 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        roti.grid(row=0, column=0, sticky=W)
        daal = Label(foodframe, text='Daal-60 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        daal.grid(row=1, column=0, sticky=W)
        fish = Label(foodframe, text='Fish-100 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        fish.grid(row=2, column=0, sticky=W)
        sabji = Label(foodframe, text='Sabji-50 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        sabji.grid(row=3, column=0, sticky=W)
        Kabab = Label(foodframe, text='Kabab-40 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        Kabab.grid(row=4, column=0, sticky=W)
        chawal = Label(foodframe, text='Chawal-30 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        chawal.grid(row=5, column=0, sticky=W)
        mutton = Label(foodframe, text='Mutton-120 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        mutton.grid(row=6, column=0, sticky=W)
        paneer = Label(foodframe, text='Paneer-100 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        paneer.grid(row=7, column=0, sticky=W)
        chicken = Label(foodframe, text='Chicken-120 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        chicken.grid(row=8, column=0, sticky=W)
        lassi = Label(drinkframe, text='Lassi-100 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        lassi.grid(row=9, column=0, sticky=W)
        coffee = Label(drinkframe, text='Coffee-40 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        coffee.grid(row=10, column=0, sticky=W)
        faluda = Label(drinkframe, text='Faluda-80 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        faluda.grid(row=11, column=0, sticky=W)
        shikanji = Label(drinkframe, text='Shikanji-30 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        shikanji.grid(row=12, column=0, sticky=W)
        jaljeera = Label(drinkframe, text='Jaljeera-40 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        jaljeera.grid(row=13, column=0, sticky=W)

        roohafza = Label(drinkframe, text='Roohafza-60 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        roohafza.grid(row=0, column=0, sticky=W)
        masalatea = Label(drinkframe, text='Masala Tea-20 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        masalatea.grid(row=1, column=0, sticky=W)
        badammilk = Label(drinkframe, text='Badam Milk-50 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        badammilk.grid(row=2, column=0, sticky=W)
        colddrink = Label(drinkframe, text='Cold Drink-80 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        colddrink.grid(row=3, column=0, sticky=W)
        # entry fields for drinks items

        # cakes
        oreo = Label(cakesframe, text='Oreo-400 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        oreo.grid(row=4, column=0, sticky=W)
        apple = Label(cakesframe, text='Apple-300 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        apple.grid(row=5, column=0, sticky=W)
        kitkat = Label(cakesframe, text='Kitkat-500 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        kitkat.grid(row=6, column=0, sticky=W)
        vanila = Label(cakesframe, text='Vanila-550 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        vanila.grid(row=7, column=0, sticky=W)
        banana = Label(cakesframe, text='Banana-450 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        banana.grid(row=8, column=0, sticky=W)
        browny = Label(cakesframe, text='Brownie-800 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        browny.grid(row=10, column=0, sticky=W)
        pineapple = Label(cakesframe, text='Pineapple-620 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        pineapple.grid(row=11, column=0, sticky=W)
        choclate = Label(cakesframe, text='Chocolate-700 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        choclate.grid(row=12, column=0, sticky=W)
        blackforest = Label(cakesframe, text='Black Forest-550 RS', font=('arial', 18, 'bold'),bg='black',fg='white')
        blackforest.grid(row=13, column=0, sticky=W)

if __name__ == '__main__':
    root=Tk()
    obj=menu_win(root)
    root.mainloop()

