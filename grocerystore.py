from tkinter import*
import time
import datetime

root=Tk()
root.geometry("2000x8000")
root.title("Grocery Shop Billing System")

myimage = PhotoImage(file='C:\\Users\\Pratik\\Desktop\\GROCERY\\logo4.png')
lable = Label(root,image=myimage)
lable.pack()

text_Input = StringVar()
operator = ""

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=300,height=700,bg="grey20",relief=SUNKEN)     # for calculator
f1.pack(side=LEFT)

f2 = Frame(root,width=800, height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#========================================================================
#                  CALCULATOR
#========================================================================
def btnclick(numbers):
    global operator
    operator =operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f1,font=('arial', 20),fg="White",textvariable=text_Input, bd=30, insertwidth=4, bg="grey20", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f1,padx=16,pady=16, fg="black", font=('arial',20),text="7", bg="White", command=lambda: btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="8", bg="white", command=lambda: btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="9", bg="White", command=lambda: btnclick(9))
btn9.grid(row=2,column=2)
Addition=Button(f1,padx=16,pady=16, fg="blue", font=('arail',20),text="+", bg="White", command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)

btn4=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="4", bg="White", command=lambda: btnclick(4))
btn4.grid(row=3,column=0)
btn5=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="5", bg="White", command=lambda: btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="6", bg="White", command=lambda: btnclick(6))
btn6.grid(row=3,column=2)
Subtraction=Button(f1,padx=20,pady=16, fg="blue", font=('arail',20),text="-", bg="White", command=lambda: btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="1", bg="White", command=lambda: btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="2", bg="White", command=lambda: btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="3", bg="White", command=lambda: btnclick(3))
btn3.grid(row=4,column=2)
Multiply=Button(f1,padx=16,pady=16, fg="blue", font=('arail',20),text="*", bg="White", command=lambda: btnclick("*"))
Multiply.grid(row=4,column=3)

btn0=Button(f1,padx=16,pady=16, fg="black", font=('arail',20),text="0", bg="White", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)
btnClear=Button(f1,padx=16,pady=16, fg="OrangeRed", font=('arail',20),text="C", bg="White", command=btnClearDisplay)
btnClear.grid(row=5,column=1)
btnEquals=Button(f1,padx=16,pady=16, fg="White", font=('arail',20),text="=", bg="DeepSkyBlue3", command=btnEqualsInput)
btnEquals.grid(row=5,column=2)
Division=Button(f1,padx=16,pady=16, fg="blue", font=('arail',20),text="/", bg="White", command=lambda: btnclick("/"))
Division.grid(row=5,column=3)

#========================================================================
#                  PROGRAM
#========================================================================

def Ref():
   # x=random.randint(10908,500876)
   # randomRef=str(x)
   # rand.set(randomRef)

    if (Rice.get()==""):
        CoRice=0
    else:
        CoRice=float(Rice.get())

   
    if (Dal.get()==""):
        CoDal=0
    else:
        CoDal=float(Dal.get())


    if (IceCream.get()==""):
        CoIceCream=0
    else:
        CoIceCream=float(IceCream.get())


    if (Cereals.get()==""):
        CoCereals=0
    else:
        CoCereals=float(Cereals.get())

        
    if (Bread.get()==""):
        CoBread=0
    else:
        CoBread=float(Bread.get())

     
    if (Milk.get()==""):
        CoMilk=0
    else:
        CoMilk=float(Milk.get())

                   
    CostofRice = CoRice * 60
    CostofMilk= CoMilk * 40
    CostofDal = CoDal* 70
    CostofIceCream = CoIceCream * 30
    CostCereals = CoCereals* 50
    CostBread = CoBread * 20


    Central_GST= (((CostofRice+CostofMilk+CostofDal+CostofIceCream+CostCereals+CostBread)* 2.5)/100)

    State_GST =(((CostofRice+CostofMilk+CostofDal+CostofIceCream+CostCereals+CostBread)* 2.5)/100)

    Total_cost = (CostofRice+CostofMilk+CostofDal+CostofIceCream+CostCereals+CostBread)

    CostofMeal= "Rs", str('%.2f' % (CostofRice+CostofMilk+CostofDal+CostofIceCream+CostCereals+CostBread))
    C_gst = "Rs", str ('%.2f' % Central_GST)
    S_gst = "Rs", str ('%.2f' % State_GST)
    OverAllCost ="Rs", str ('%.2f' % (Total_cost+Central_GST+State_GST))


    Sgst.set(S_gst)
    Cost.set(CostofMeal)
    Cgst.set(C_gst)
    Total.set(OverAllCost)


def Reset():
    Bread.set("")
    Rice.set("")
    Dal.set("")
    IceCream.set("")
    Cereals.set("")
    Milk.set("")

   # rand.set("")

    Total.set("")
    Sgst.set("")
    Cgst.set("")
    Cost.set("")
    
#========================================================================
#                  RESTAURANT MENU
#========================================================================
Bread=StringVar()
Rice=StringVar()
Dal=StringVar()
IceCream=StringVar()
Cereals=StringVar()
Milk=StringVar()
Cost=StringVar()
Sgst=StringVar()
Cgst=StringVar()
Total=StringVar()


lblBread= Label(f2, font=('arial', 16, 'bold'),text="Bread",bd=16,anchor="w")
lblBread.grid(row=0, column=0)
lblBread=Entry(f2, font=('arial',16,'bold'),textvariable=Bread,bd=10,insertwidth=4,bg="white",justify='right')
lblBread.grid(row=0,column=1)

lblMilk= Label(f2, font=('arial', 16, 'bold'),text="Milk",bd=16,anchor="w")
lblMilk.grid(row=1, column=0)
txtMilk=Entry(f2, font=('arial',16,'bold'),textvariable=Milk,bd=10,insertwidth=4,bg="white",justify='right')
txtMilk.grid(row=1,column=1)

lblIceCream= Label(f2, font=('arial', 16, 'bold'),text="Ice-Cream",bd=16,anchor="w")
lblIceCream.grid(row=2, column=0)
lblIceCream=Entry(f2, font=('arial',16,'bold'),textvariable=IceCream,bd=10,insertwidth=4,bg="white",justify='right')
lblIceCream.grid(row=2,column=1)

lblRice= Label(f2, font=('arial', 16, 'bold'),text="Rice",bd=16,anchor="w")
lblRice.grid(row=3, column=0)
txtRice=Entry(f2, font=('arial',16,'bold'),textvariable=Rice,bd=10,insertwidth=4,bg="white",justify='right')
txtRice.grid(row=3,column=1)

lblDal= Label(f2, font=('arial', 16, 'bold'),text="Dal",bd=16,anchor="w")
lblDal.grid(row=4, column=0)
txtDal=Entry(f2, font=('arial',16,'bold'),textvariable=Dal,bd=10,insertwidth=4,bg="white",justify='right')
txtDal.grid(row=4,column=1)

lblCereals= Label(f2, font=('arial', 16, 'bold'),text="Cereals",bd=16,anchor="w")
lblCereals.grid(row=5, column=0)
txtCereals=Entry(f2, font=('arial',16,'bold'),textvariable=Cereals,bd=10,insertwidth=4,bg="white",justify='right')
txtCereals.grid(row=5,column=1)


#========================================================================
#                  RESTAURANT BILL INFO
#========================================================================


lblCost= Label(f2, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=0, column=2)
txtCost=Entry(f2, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="White",justify='right')
txtCost.grid(row=0,column=3)


lblSgst= Label(f2, font=('arial', 16, 'bold'),text="SGST",bd=16,anchor="w")
lblSgst.grid(row=1, column=2)
txtSgst=Entry(f2, font=('arial',16,'bold'),textvariable=Sgst,bd=10,insertwidth=4,bg="White",justify='right')
txtSgst.grid(row=1,column=3)


lblCgst= Label(f2, font=('arial', 16, 'bold'),text="CGST",bd=16,anchor="w")
lblCgst.grid(row=2, column=2)
txtCgst=Entry(f2, font=('arial',16,'bold'),textvariable=Cgst,bd=10,insertwidth=4,bg="White",justify='right')
txtCgst.grid(row=2,column=3)

lblTotalCost= Label(f2, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=3, column=2)
txtTotalCost=Entry(f2, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="White",justify='right')
txtTotalCost.grid(row=3,column=3)


#========================================================================
#                  BUTTONS
#========================================================================
btnTotal=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="OrangeRed",command=Ref).grid(row=5,column=2)

btnReset=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="OrangeRed",command=Reset).grid(row=5,column=3)

root.mainloop()

