import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry('500x400')
root.option_add('*Font','Tahoma 12')
root.title('ยินดีต้อนรับสู่ร้านค้า')
myinput=StringVar()
numberinput=IntVar()
mylist = StringVar()
listprice=[]
listE=[]
q=0
nuberprice=IntVar()
listitem = []
PriceE=DoubleVar()
priceE=IntVar()
listprice=[]
inputnum=IntVar()

def loginuser():
    inputuser=myinput.get()

    loop = True

    while loop:

        if len(inputuser) == 0 :
            messagebox.showerror("เกิดข้อผิดพลาด!", "โปรดกรอก ชื่อ")
            
            loop = False

        else:
            loop = False
    
            

            menu = Toplevel(root)
            menu.option_add('*Font','Tahoma 12')
            menu.geometry("500x400")
            lbct=Label(menu,text='รายการสินค้า',fg="white",bg="purple",width=20)
            lbct.place(x=90,y=53)
            filepath = "listitem.csv"
            with open(filepath, "r", encoding="utf-8") as infile:
                rd = csv.reader(infile)
                listitem = list(rd)

            print(listitem)
            #combolist = ['นํ้าดื่มสิงค์','นํ้าดื่มทิพย์', 'มาม่าหมูสับ', 'มาม่าต้มยำกุ้ง' ,'เลย์','เทสโต้']
            
            combo = ttk.Combobox(menu, textvariable=mylist, values=listitem)
            combo.place(x=50,y=100)
            #combo.current(3)

            boto = Button(menu,command=obtener,text="summit").place(x=100,y=150)
            etiqueta = Label(menu).place(x=40,y=200)
            btpo=Button(menu,text='ยกเลิกการทำรายการ',width=20,font=('bold',10),command=menu.destroy)
            btpo.place(x=280,y=250)

    


    
            menu.mainloop()
    

def obtener():
    my = mylist.get()
    print(my)
    
    
    
    filepath = 'menu.csv'
    
    menu2 = Toplevel(root)
    menu2.option_add('*Font','Tahoma 12')
    menu2.geometry("500x400")
    filepath = 'price.csv'
    with open(filepath, "r", encoding="utf-8") as infile:
        rd = csv.reader(infile)
        price = list(rd)
        print(price)
    
    lbct=Label(menu2,text='รายการสินค้า',fg="white",bg="purple",width=10)
    lbct.place(x=40,y=20)
    wares=Label(menu2,text=my,fg="black",bg="violet",width=10)
    wares.place(x=40,y=60)
    number=Entry(menu2,textvariable=numberinput)
    number.place(x=140,y=60)
    print(my)
    if my==('WaterBrandCrystal'):
        lb=Label(menu2,text='ชิ้นละ',fg="black",bg="cyan",width=10)
        lb.place(x=40,y=90)
        Price=price[0],'บาท'
        lb=Label(menu2,text=Price,fg="black",bg="cyan",width=10)
        lb.place(x=140,y=90)
        priceE=price[0]
        for item in price[0]:
            listE.append(int(item))
        print(listE)
       
    elif my==('WaterBrandNamthip'):
        lb=Label(menu2,text='ชิ้นละ',fg="black",bg="cyan",width=10)
        lb.place(x=40,y=90)
        Price=price[1],'บาท'
        lb=Label(menu2,text=Price,fg="black",bg="cyan",width=10)
        lb.place(x=140,y=90)
        priceE=price[1]
        for item in price[1]:
            listE.append(int(item))
        print(listE)
      
        
        
        
    elif my==('MamaPorkFlavour'):
        lb=Label(menu2,text='ชิ้นละ',fg="black",bg="cyan",width=10)
        lb.place(x=40,y=90)
        Price=price[2],'บาท'
        lb=Label(menu2,text=Price,fg="black",bg="cyan",width=10)
        lb.place(x=140,y=90)
        priceE=price[2]
        for item in price[2]:
            listE.append(int(item))
        print(listE)
        
    elif my==('MamaPorkTomYam'):
        lb=Label(menu2,text='ชิ้นละ',fg="black",bg="cyan",width=10)
        lb.place(x=40,y=90)
        Price=price[3],'บาท'
        lb=Label(menu2,text=Price,fg="black",bg="cyan",width=10)
        lb.place(x=140,y=90)
        priceE=price[3]
        for item in price[3]:
            listE.append(int(item))
        print(listE)
       
    elif my==("Lay's"):
        lb=Label(menu2,text='ชิ้นละ',fg="black",bg="cyan",width=10)
        lb.place(x=40,y=90)
        Price=price[4],'บาท'
        lb=Label(menu2,text=Price,fg="black",bg="cyan",width=10)
        lb.place(x=140,y=90)
        priceE=price[4]
        for item in price[4]:
            listE.append(int(item))
        print(listE)
      
    elif my==('Testo'):
        lb=Label(menu2,text='ชิ้นละ',fg="black",bg="cyan",width=10)
        lb.place(x=40,y=90)
        Price=price[5],'บาท'
        lb=Label(menu2,text=Price,fg="black",bg="cyan",width=10)
        lb.place(x=140,y=90)
        priceE=price[5]
        for item in price[5]:
            listE.append(int(item))
        print(listE)
        
       
    OKbt=Button(menu2,text='ชำระเงิน',command=pay)
    OKbt.place(x=20,y=300)
    btpo=Button(menu2,text='ยกเลิกการทำรายการ',width=20,font=('bold',10),command=menu2.destroy)
    btpo.place(x=280,y=250)

    
        
def pay():
    num=numberinput.get()
    if num ==0:
         messagebox.showerror('เกิดข้อผิดพลาด',"โปรดกรอกจำนวน")
         obtener()
    else:
         
        
        bill = Toplevel(root)
        bill.option_add('*Font','Tahoma 12')
        bill.geometry("500x400")
    
        PriceEE=sum(listE)
        Num=PriceEE*num
        listprice.append(Num)
        lw=Label(bill,text='ชำระเงิน',width=20,font=('bold',20))
        lw.place(x=90,y=53)
        text1='ราคา', Num,'บาท'
        lw2=Label(bill,text=text1,width=20,font=('bold',15))
        lw2.place(x=60,y=130)
    
        entry = Entry(bill,textvariable=nuberprice)
        entry.place(x=240,y=130)
        entry.focus()
   
    
        btpp=Button(bill,text='ชำระเงิน',width=20,font=('bold',10),command=Finish)
        btpp.place(x=40,y=250)
        btpo=Button(bill,text='ยกเลิกการทำรายการ',width=20,font=('bold',10),command=root.destroy)
        btpo.place(x=280,y=250)
    
    
def Finish():
    inputuser=myinput.get()
    my = mylist.get()
    Sumnumber=numberinput.get()
    Inprice=nuberprice.get()
    Outprice=sum(listprice)
    root3=Toplevel(root)
    root3.minsize(500,300)
    try:
        Inprice=nuberprice.get()
        Outprice=sum(listprice)
    except:
        print("Error numprice eror!")
    print(Outprice)    
    if Outprice==Inprice:
        filepath = 'bill.csv'
        with open(filepath,'w',encoding='utf-8')as outfile:
            writer = csv.writer(outfile)
            writer.writerow([inputuser,my,Sumnumber,'Sum','success'])
        lb=Label(root3,text='ขอบคุณที่ใช้บริการ',width=20,font=('bold',20))
        lb.place(x=90,y=53)
        btpo=Button(root3,text='ทำรายการเสร็จสิ้น',width=20,font=('bold',10),command=root.destroy)
        btpo.place(x=280,y=250)   
            
        loop = False

    elif Outprice<Inprice:
        loop = False
        messagebox.showerror('เกิดข้อผิดพลาด',"ชำระเงินเกิน")
        root4=Toplevel(root)
        root4.minsize(100,100)
        outin=Outprice
        out='โปรดชำระให้','=',outin,'บาท'
        lb=Label(root4,text=out,width=20,font=('bold',20))
        lb.place(x=10,y=10)
        number=Entry(root4,textvariable=inputnum)
        number.place(x=30,y=50)
        bt1=Button(root4,text='ชำระเงินใหม่',command=Finish2,width=20,font=('bold',10))
        bt1.place(x=90,y=90)
        
    else:
        messagebox.showerror('เกิดข้อผิดพลาด',"ชำระเงินไม่ครบ")
        root4=Toplevel(root)
        root4.minsize(100,100)
        outin=Outprice
        out='โปรดชำระให้','=',outin,'บาท'
        lb=Label(root4,text=out,width=20,font=('bold',20))
        lb.place(x=10,y=10)
        number=Entry(root4,textvariable=inputnum)
        number.place(x=30,y=50)
        bt1=Button(root4,text='ชำระเงินใหม่',command=Finish2,width=20,font=('bold',10))
        bt1.place(x=90,y=90)
def Finish2():
    inputuser=myinput.get()
    my = mylist.get()
    Sumnumber=inputnum.get()
    Inprice=nuberprice.get()
    Outprice=sum(listprice)
    root5=Toplevel(root)
    root5.minsize(500,300)
    try:
        Inprice=inputnum.get()
        Outprice=sum(listprice)
    except:
        print("Error numprice eror!")
    print(Outprice)
    print(Inprice)
    if Outprice==Inprice:
        filepath = 'bill.csv'
        with open(filepath,'w',encoding='utf-8')as outfile:
            writer = csv.writer(outfile)
            writer.writerow([inputuser,my,Sumnumber,'Sum','success'])
        lb=Label(root5,text='ขอบคุณที่ใช้บริการ',width=20,font=('bold',20))
        lb.place(x=90,y=53)
        btpo=Button(root5,text='ทำรายการเสร็จสิ้น',width=20,font=('bold',10),command=root.destroy)
        btpo.place(x=280,y=250)   
            
        
        
    

        
    

    print('end')

listw1=[]
lb=Label(root,text='user',width=15)
lb.place(x=10,y=13)
user=Entry(root,textvariable=myinput)
user.place(x=150,y=13)

bt=Button(root,text='เข้าระบบ',command=loginuser)
bt.place(x=50,y=50)
btpo=Button(root,text='ยกเลิกการทำรายการ',width=20,font=('bold',10),command=root.destroy)
btpo.place(x=280,y=250)
root.mainloop()


