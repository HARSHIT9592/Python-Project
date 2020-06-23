from tkinter import *

import tkinter.messagebox
import math 



window=Tk()

window.title('SCIENTIFIC CALCULATOR')


window.configure(background='maroon')

window.resizable(width= False , height= False)

window.geometry('480x568+0+0')



calc=Frame(window)

calc.grid()

menubar=Menu(calc)

#=====================================DEFINING VALUES TO THE OPERATION PERFORMING BUTTONS VIA UNDERNEATH CLASS AND ITS FUNCTIONS=====================================

class Calc():

#--------------------------------------------------------------------------------------------------------------------------------------------

    
    def __init__(self):    #====== CONSTRUCTOR =======

        self.sum= 0          #================= WHICH RETAINS TOTAL VALUE THAT HAS BEEN GIVEN AS AN INPUT(S)=====================

        self.present=''     #======================== INITIALLY NO VALUE IS THERE ============================

        self.input=True     #=============== CONVEYING THE INSERTED VALUE AS A VALID INPUT =============================== 

        self.verify=False   #==================== CHECKING THE VALUES ==========================

        self.operate=''       #================= FOR CALLING THE OPERATION i.e. INITIALLY NO COMPUTATION IS PERFORMED ======================

        self.final=False      #===================== FINAL RESULT =========================


#---------------------------------------------------------------------------------------------------------------------------------------------

    def Number(self,digit):     #================= FUNCTION CREATED FOR INPUTTING VALUES ==================

        self.final = False

        first = TXT.get()

        second = digit

        if  self.input:

            self.present=second

            self.input = False

        else:

            if second == ".":

                if second in first:

                    return

            self.present=first+second

        self.display(self.present)


#--------------------------------------------------------------------------------------------------------------------------------------------


    def SUM(self):     #=========== BACK END FOR 'EQUAL TO' BUTTON ================

        self.final=True

        self.present=float(self.present)

        if self.verify==True:

            self.Is_valid()

        else:
            self.sum=float(TXT.get())

#---------------------------------------------------------------------------------------------------------------------------------------------

            

    def display(self,obtain):  #

        TXT.delete(0,END)

        TXT.insert(0,obtain) 


#---------------------------------------------------------------------------------------------------------------------------------------------
        

    def  Is_valid(self):  #==========FUNCTION CREATED FOR WORKING OF DMAS OPERATIONS ===========

        if self.operate=='Add':
            
            self.sum+=self.present

        if self.operate=='Sub':
            
            self.sum-=self.present

        if self.operate=='Mul':
            
            self.sum*=self.present

        if self.operate=='Div':
            
            self.sum/=self.present

        if self.operate=='mod':
            
            self.sum%=self.present


        self.input=True

        self.verify=False

        self.display(self.sum)

#--------------------------------------------------------------------------------------------------------------------------------------------


    def operator(self ,operate):

        self.present=float(self.present)

        if self.verify:
            
            self.Is_valid()

        elif not self.final:

            self.sum=self.present

            self.input=True

        self.verify=True

        self.operate=operate

        self.final=False




    def CLR(self):

        self.final=False

        self.present='0'

        self.display(0)

        self.input=True



    def CLRALL(self):

        self.CLR()

        self.final=0



    def PlusMinus(self):

        self.final=False

        self.present=-(float(TXT.get()))

        self.display(self.present)



    def log(self):

        self.final=False

        self.present=math.log(float(TXT.get()))

        self.display(self.present)


    def log10(self):

        self.final=False

        self.present=math.log10(float(TXT.get()))

        self.display(self.present)



    def ceil(self):

        self.final=False

        self.present=math.ceil(float(TXT.get()))

        self.display(self.present)


    def sin(self):

        self.final=False

        self.present=math.sin(float(TXT.get()))

        self.display(self.present)



    def cos(self):

        self.final=False

        self.present=math.cos(float(TXT.get()))

        self.display(self.present)



    def pi(self):

        self.final=False

        self.present= math.pi

        self.display(self.present)

        

    def sin(self):
       
        self.final=False

        self.present=math.sin(float(TXT.get()))
        
        self.display(self.present)      

         

    def cos(self):
       
        self.final=False

        self.present=math.cos(float(TXT.get()))
        
        self.display(self.present)



    def tan(self):
       
        self.final=False

        self.present=math.tan(float(TXT.get()))
        
        self.display(self.present)



    def asinh(self):
       
        self.final=False

        self.present=math.asinh(float(TXT.get()))
        
        self.display(self.present)



    def acosh(self):
       
        self.final=False

        self.present=math.acosh(float(TXT.get()))
        
        self.display(self.present)



    def atanh(self):

        self.final=False

        self.present=math.acosh(float(TXT.get()))

        self.display(self.present)
        

    def exp(self):
       
        self.final=False

        self.present=math.e
        
        self.display(self.present)



    def sqrt(self):
       
        self.final=False

        self.present=math.sqrt(float(TXT.get()))
        
        self.display(self.present)



    def fact(self):
       
        self.final=False

        self.present=math.factorial(float(TXT.get()))
        
        self.display(self.present)



    def floor(self):
       
        self.final=False

        self.present=math.floor(float(TXT.get()))
        
        self.display(self.present)



    def RAD(self):
       
        self.final=False

        self.present=math.radians(float(TXT.get()))
        
        self.display(self.present)



    def deg(self):

        self.final=False

        self.present=math.degrees(float(TXT.get()))

        self.display(self.present)



    def FAB(self):
        
        self.final=False

        self.present=math.fabs(float(TXT.get()))

        self.display(self.present)



    def log2(self):

        self.final=False

        self.present=math.log2(float(TXT.get()))

        self.display(self.present)


    def lgamma(self):

        self.final=False

        self.present=math.lgamma(float(TXT.get()))

        self.display(self.present)



    def gamma(self):

        self.final=False

        self.present=math.gamma(float(TXT.get()))

        self.display(self.present)
   






#=========================================== CREATING AREA  FOR INPUTTING VALUES =============================================


Value_added = Calc()
TXT = Entry(calc,font=('arial', 20 , 'bold' ,) ,bg='white' , bd=25 , width=29 , justify = RIGHT)
TXT.grid(row=0,column=0 , columnspan = 4 , pady = 0.8)
TXT.insert(0,'0')

#------------------------------------------------------------------------------------------------------------------

#=================================================CREATING NUMERIC BUTTONS ===================================================


NUMBER='123456789'

i=0

btn=[]

for j in range(2,5):   #=========== FOR ROW ================

    for k in range(3): #=========== FOR COLUMN =============

        btn.append(Button(calc , width = 5 , height = 2 , font=('garamond' , 20 , 'bold' ) , bd = 4 , bg = 'brown' ,

                          text = NUMBER[i] , activebackground= 'magenta' , state = 'normal' ))

        btn[i].grid(row = j , column = k ,pady = 0.8)

        btn[i]["command"]=lambda entity = NUMBER[i]:Value_added.Number(entity) #============= VALID FOR ONLY  ONE EXPRESSION =======================  

        i+=1



#==================------------------------------------------------------------------------------------------------------------


#================================================= FOR CREATING OPERATION PERFORMING BUTTONS ====================================


btnC = Button(calc , text = chr(67) ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.CLR)

btnC.grid(row = 1 , column = 0 , pady = 1)


btnCE = Button(calc , text = chr(67)+ chr(69) , width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.CLRALL)

btnCE.grid(row = 1 , column = 1 , pady = 1)



btnSqrt = Button(calc , text = 'sqrt' , width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.sqrt)

btnSqrt.grid(row = 1 , column = 2 , pady = 1)


btnAdd = Button(calc , text = '+' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command=lambda : Value_added.operator('Add'))

btnAdd.grid(row = 1 , column = 3 , pady = 1)

   

btnSub = Button(calc , text = '-' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command=lambda : Value_added.operator('Sub'))

btnSub.grid(row = 2 , column = 3 , pady = 1)



btnMul = Button(calc , text = '*' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command=lambda : Value_added.operator('Mul'))

btnMul.grid(row = 3 , column = 3 , pady = 1)



btnDiv = Button(calc , text = '/' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command=lambda : Value_added.operator('Div'))

btnDiv.grid(row = 4 , column = 3 , pady = 1)



btnzero = Button(calc , text = '0' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green', command=lambda : Value_added.Number(0))

btnzero.grid(row = 5 , column = 0 , pady = 1)




btndot = Button(calc , text = '.' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command=lambda : Value_added.Number('.'))

btndot.grid(row = 5 , column = 1 , pady = 1)



btn1 = Button(calc , text = '+-' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.PlusMinus)

btn1.grid(row = 5 , column = 2 , pady = 1)




btneql = Button(calc , text = '=' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.SUM)

btneql.grid(row = 5 , column = 3 , pady = 1)


#_----------------------------------------------------------------------------------------------------------------------------------------



btnrad = Button(calc , text = 'RAD' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.RAD)

btnrad.grid(row = 1 , column = 4 , pady = 1)





btnsin = Button(calc , text = 'sin' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.sin)

btnsin.grid(row = 1 , column = 5 , pady = 1)



btncos = Button(calc , text = 'cos' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.cos)

btncos.grid(row = 1 , column = 6 , pady = 1)



btntan = Button(calc , text = 'tan' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.tan)

btntan.grid(row = 1 , column = 7 , pady = 1)



btnCei = Button(calc , text = 'CEIL' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.ceil)

btnCei.grid(row = 2 , column = 4 , pady = 1)



btnexp = Button(calc , text = 'exp' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.exp)

btnexp.grid(row = 2 , column = 5 , pady = 1)



btnlog = Button(calc , text = 'log10' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.log10)

btnlog.grid(row = 2 , column = 6 , pady = 1)



btndeg = Button(calc , text = 'DEG' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.deg)

btndeg.grid(row = 2 , column = 7 , pady = 1)



btnmod = Button(calc , text = '%' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command=lambda : Value_added.operator('mod'))

btnmod.grid(row = 3 , column = 4 , pady = 1)



btnPi = Button(calc , text = 'pi' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.pi)

btnPi.grid(row = 3 , column = 5 , pady = 1)



btnfact = Button(calc , text = 'n!' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.fact)

btnfact.grid(row = 3 , column = 6 , pady = 1)



btnfloor = Button(calc , text = 'floor' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.floor)

btnfloor.grid(row = 3 , column = 7 , pady = 1)



btnlnx = Button(calc , text = 'lnx' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.log)

btnlnx.grid(row = 4 , column = 4 , pady = 1)




btnasinh = Button(calc , text = 'asinh' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.asinh)

btnasinh.grid(row = 4 , column = 5 , pady = 1)



btnacosh = Button(calc , text = 'acosh' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.acosh)

btnacosh.grid(row = 4 , column = 6 , pady = 1)





btnatanh = Button(calc , text = 'atanh' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.atanh)

btnatanh.grid(row = 4 , column = 7 , pady = 1)


btnfab = Button(calc , text = 'ABS' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command = Value_added.FAB)

btnfab.grid(row = 5 , column = 4 , pady = 1)




btnlog2 = Button(calc , text = 'log2' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'grey' , command = Value_added.log2)

btnlog2.grid(row = 5 , column = 5 , pady = 1)



btnlgamma = Button(calc , text = 'Lgam' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green' , command = Value_added.lgamma)

btnlgamma.grid(row = 5 , column = 6 , pady = 1)



btnextra = Button(calc , text = 'gam' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'violet' , command =Value_added.gamma)

btnextra.grid(row = 5 , column = 7 , pady = 1)




"""btnath = Button(calc , text = 'atanh' ,width = 5  , height = 2 , font = ('arial' , 20 , 'bold' ) , bd = 5 , bg = 'sea green')

btnath.grid(row = 7 , column = 4 , pady = 1)"""
#----------------------------------------------------------------------------------------------------------------------------------------------


    



#================================EXIT FUNCTION  HAS BEEN  DEFINED =======================================


def EXIT():

    EXIT=tkinter.messagebox.askyesno('SCIENTIFIC CALCULATOR' ,'ARE YOU SURE YOU WANT TO EXIT ?')

    if EXIT>0:

        window.destroy()

        return


#--------------------------------------------------------------------------------------------------------



#=============================== FUNCTION FOR WORKING OF  SCIENTIFIC MENU================================



def SCIEN():

    window.resizable(width=False , height=False)

    window.geometry('900x568+0+0')

"""   TXT1 = Entry(calc,font=('arial', 20 , 'bold' ,) ,bg = 'white' , bd = 30 , width = 56 , justify = RIGHT)

    TXT1.grid(row=0,column=0 , columnspan = 10 , pady = 1)

    TXT1.insert(0,'0') """

   
#-------------------------------------------------------------------------------------------------------


def STAN():
    
    window.resizable(width=False , height=False)

    window.geometry('480x568+0+0')

"""  TXT = Entry(calc,font=('arial', 20 , 'bold' ,) ,bg='white' , bd=25 , width=29 , justify = RIGHT)

    TXT.grid(row=0,column=0 , columnspan = 4 , pady = 0.8)

    TXT.insert(0,'0')"""
     


    

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


filemenu=Menu(menubar,tearoff=0)


menubar.add_cascade(label='File', menu=filemenu)  #============================== TO CREATE FILE MENU IN MENUBAR  =============================


filemenu.add_command(label='scientific' , command= SCIEN) #======================== TO CREATE SUB-MENU i.e. 'SCIENTIFIC'  IN FILE OPTION =========================


filemenu.add_command(label='standard', command=STAN)  #================= SUB-MENU IN FILE OPTION ===================


filemenu.add_separator() # to separate between dropdown menu 


filemenu.add_command(label='Exit',command=EXIT)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



editmenu=Menu(menubar,tearoff=1)


menubar.add_cascade(label='Edit',menu=editmenu)


editmenu.add_command(label='cut')


editmenu.add_command(label='copy')


editmenu.add_separator() 


editmenu.add_command(label='paste')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



othermenu=Menu(menubar,tearoff=0)


menubar.add_cascade(label='Help',menu=othermenu)


othermenu.add_command(label='About')


othermenu.add_separator()


othermenu.add_command(label='Calculator Help (Tutorial)')


othermenu.add_command(label='Terms and Conditions')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


window.config(menu=menubar)


window.mainloop()
