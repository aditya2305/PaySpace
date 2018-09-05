import datetime
now = datetime.datetime.now()
        
class main(object):
    def __init__(self):
        self.amt1=0
        self.amt2=0
        self.amt3=0
        self.amt4=0
        self.amt5=0
        self.cardno='null'
        self.cardname=""
        self.date=""
        self.cvv=0
        self.bal=0
        self.name=""
        self.username=""
        self.password=""
        self.mob=0
        self.nam=""
        self.comp=""
        self.date=""
        self.amt=0
        self.id=0
        self.board=""
        self.mob=0
    def enter(self,b):#Addmoney
        print""
        while True :
            self.cardno=raw_input("\tEnter Card Number-")
            if len(self.cardno) !=16:
                print"\tWrong input !"
            else:
                break
        self.cardname=str(raw_input("\tEnter Name On Card-"))
        self.date=str(raw_input("\tEnter Card Exp.Date(MM/YY)-"))
        while True :
            self.cvv=input("\tEnter C.V.V no. -")
            if len(str(self.cvv)) !=3:
                print"\tWrong input !"
            else:
                break
        
        self.amt=input("\tEnter Amount-")
        self.bal=b+self.amt
        print""
    def allot(self):
        print
        print"\t\t\tSignUp"
        print""
        self.name=str(raw_input("\t        Enter Your Full Name-"))
        if self.name=="":
            print"Can't Be Null"
            signup()
        self.username=str(raw_input("\t        Enter Username      -"))
        if self.username =="":
            print"\tUsername can't be null !"
            signup()
        self.password=str(raw_input("\t        Enter Password      -"))
        if self.password=="":
            print"\tPassword can't be null !"
            signup()#yahan pe dubara dalne ke lie bolna chie username aur passowrd or agr glti se null ho to maybe use signup dubara krale
        
        print""
        print"\t         Welcome To PAYSPACE !!!!"
        
        
    def enter1(self,b,f):  #prepaidEnter
        if b==0 or b<0:
            print"\tEmpty Pockets,Go Add Some Money"
            menu(f)
        print"\tPrepaid mobile recharge :"
        print""
        self.nam=raw_input("\tEnter your name :")
        while True:
            self.mob=input("\tEnter your mobile number :")
            if len(str(self.mob))!=10:
                print"\tInvalid input !"
            else:
                break
        self.comp=raw_input("\tEnter your service provider (company):")
        self.amt5=input("\tEnter amount of recharge :")
        if self.amt5>b:
            print"\tNot Sufficient Balance,Add More Money"
            menu(f)
        else:
            self.bal=b-self.amt5
    def enter2(self,b,f): #postpaidEnter
        if b==0 or b<0:
            print"\tEmpty Pockets,Go Add Some Money"
            menu(f)
        print"\tPostpaid mobile recharge :"
        print""
        self.nam=raw_input("\tEnter your name :")
        while True:
            self.mob=input("\tEnter your mobile number :")
            if len(str(self.mob)) !=10:
                print"\tInvalid input !"
            else:
                break
        self.comp=raw_input("\tEnter your service provider(company) :")
        
        self.amt4=input("\tEnter amount of recharge :")
        if self.amt4>b:
            print"\tNot Sufficient Balance,Add More Money"
            menu(f)
        else:
            self.bal=b-self.amt4
        
    def enter3(self,b,f):#ElectricityEnter
        if b==0 or b<0:
            print"\tEmpty Pockets,Go Add Some Money"
            menu(f)
        
        while True :
            self.board=str(raw_input("\tEnter Your Current Board (BSES,NHPC,NTPC or OTHERS-)"))
            if self.board=="":
                print"Invalid Input"
            if self.board.isdigit():
                print"Invalid Input"
            else:
                break
        while True:
            try:
                self.id=input("\tEnter Your Consumer Identity-")
                if len(str(self.id))!=9:
                    print"\tInvalid input"
                if self.id=="":
                    print"Invalid Input"
            except NameError:
                print"Invalid Input"
            else:
                break
        while True:
            self.mob=input("\tEnter your mobile number :")
            if len(str(self.mob)) !=10:
                print"\tInvalid input !"
            else:
                break
        while True:
            self.amt1=input("\tEnter Amount To Be Paid-")
            if self.amt1=='null':
                print"Invalid Input"
            else:
                break
                
                
        if self.amt1>b:
            print"\tNot Sufficient Balance,Add More Money"
            menu(f)
        else:
            self.bal=b-self.amt1
                

    def enter4(self,b,f):#GasBillEnter
        if b==0 or b<0:
            print"\tEmpty Pockets,Go Add Some Money"
            menu(f)
        self.board=raw_input("\tEnter Your Natural Gas Provider-(IGL,ONGC,EIL or Other)")
        while True :
            self.id=input("\tEnter Your Consumer Identity-")
            if len(str(self.id))!=9:
                print"\tInvalid input"
            else:
                break
        while True:
            self.mob=input("\tEnter your mobile number :")
            if len(str(self.mob)) !=10:
                print"\tInvalid input !"
            else:
                break
        
        
        self.amt2=input("\tEnter Amount To Be Paid-")
        if self.amt2>b:
            print"\tNot Sufficient Balance,Add More Money"
            menu(f)
        else:
            self.bal=b-self.amt2

    def enter5(self,b,f):#WaterBillEnter
        if b==0 or b<0:
            print"\tEmpty Pockets,Go Add Some Money"
            menu(f)
        self.board=raw_input("\tEnter Your Jal Board-(DJB,BJB,WBJB Or Other)")
        while True :
            self.id=input("\tEnter Your Consumer Identity-")
            if len(str(self.id))!=9:
                print"\tInvalid input"
            else:
                break
        while True:
            self.mob=input("\tEnter your mobile number :")
            if len(str(self.mob)) !=10:
                print"\tInvalid input !"
            else:
                break
        
        self.amt3=input("\tEnter Amount To Be Paid-")
        if self.amt3>b:
            print"\tNot Sufficient Balance,Add More Money"
            menu(f)
        else:
            self.bal=b-self.amt3
        
    def show1(self): #prepaiddetailsShow
        print"\tYour recharge details :"
        print""
        print"Recharge successful on ",self.mob," of amount ",self.amt5
        print""
    def show2(self):#postpaiddetailsShow
        print"\tYour bill details :"
        print""
        print"Recharge successful on ",self.mob," of amount ",self.amt4
        print""
    
    def play(self):#electricityShow
        
        print"_"*45
        print"\t\t  ",self.board
        print"_"*45
        print"\t Consumer Identity-",self.id
        print"\t Name-",self.nam
        print"\t Mobile Number-",self.mob
        print
        print"\tElectricity Bill ",self.amt1," Paid Successfully"
        print"\tMessage send to Mobile."
        print"_"*45
        

    def play1(self):#GasShow
        print"*"*45
        print"_"*45
        print"\t\t  ",self.board
        print"_"*45
        print"\t Consumer Identity-",self.id                             #aur kuch jgh me name khali ara h bill details me
        print"\t Name-",self.nam                                         
        print"\t Mobile Number-",self.mob
        print
        print"    Gas Bill Of",self.amt2,"Paid Successfully"
        print"\tMore Details Sent To Your Mobile"
        print"_"*45
        print"*"*45
    def play2(self):#waterShow
        print"*"*45
        print"_"*45
        print"\t\t  ",self.board
        print"_"*45
        print"\tConsumer Identity-",self.id
        print"\tName-",self.name
        print"\tMobile Number-",self.mob
        print
        print"    Water Bill Of",self.amt3,"Paid Successfully"
        print"\tMore Details Sent To Your Mobile"
        print"_"*45
        print"*"*45
        
    def display(self):#transAddMoney
        if self.amt==0:
            pass
        else:
            print""                                            
            print"\tName On Card-",self.cardname
            print"\tRs.",self.amt,"Added To eWallet"
            print"\tOn : ", (now.strftime("%Y-%m-%d %H:%M"))
        
    def display2(self):#transElectricity
        if self.amt1==0:
            pass
        else:
            print""                                               #aur starting me faltu ka electricity bill paid dikha rha h 
            print"\tElectricity Bill paid to",self.board
            print"\tRs.",self.amt1,"Deducted From Wallet"
            print"\tOn",(now.strftime("%Y-%m-%d %H:%M"))
            print
    def display3(self):#transGas
        if self.amt2==0:
            pass
        else:
            print""
            print"\tGas Bill paid",self.board
            print"\tRs.",self.amt2,"Deducted From Wallet"
            print"\tOn",(now.strftime("%Y-%m-%d %H:%M"))
            print
    def display4(self):#transWater
        if self.amt3==0:
            pass
        else:
            print""
            print"\tWater Bill paid",self.board
            print"\tRs.",self.amt3,"Deducted From Wallet"
            print"\tOn",(now.strftime("%Y-%m-%d %H:%M"))
            print
    def display5(self):#transPrepaid
        if self.amt5==0:
            pass
        else:
            print"\tMobile Recharge Successfull"
            print"\tMobile No-",self.mob
            print"\tRs.",self.amt5,"Added To Your Mobile"
            print"\tOn : ",(now.strftime("%Y-%m-%d %H:%M"))
            print
    def display6(self):#transPostpaid
        if self.amt4==0:
            pass
        else:
            print"\tMobile Bill Paid"
            print"\tMobile No-",self.mob
            print"\tRs.",self.amt4
            print"\tOn :",(now.strftime("%Y-%m-%d %H:%M"))
            print
    

def signup():
    t=main()
    t.allot()
    global name
    name=t.username+".dat"
    ofile=open(name,"ab")
    pickle.dump(t,ofile)
    ofile.close()
    print
    p=str(raw_input("\t     Do You Want To Sign In?(Y/N)-"))
    if p=="y" or p=="Y":
        signin()
    else:
        demo()
        
def signin():
    print
    print"\t\t\tSignIn"
    print""
    w=str(raw_input("\t        Enter Username      -"))
    b=str(raw_input("\t        Enter Password      -"))
    p=w+".dat"
    try:
        ifile=open(p,"r")
    except IOError:
        print
        print"\t        You Must Signup First"
        print
        demo()
        
    d=0
    while True:
        try:
            s=pickle.load(ifile)
            if s.username==w and s.password==b:
                d=1
                print"\tLogged In"
                print""
                menu(p)
            else:
                print""
                print "\tIncorrect Username Or Password"
                print""
                p=str(raw_input("\tDo You Want To Sign In?(Y/N)-"))
                if p=="y" or p=="Y":
                    signin()
                else:
                    p=str(raw_input("\tDo You Want To Sign Up?(Y/N)-"))
                    if p=="y" or p=="Y" :
                        signup()
                    else :
                        pass
                break
        
        except EOFError:
            print""
            print "\tIncorrect Username Or Password"
            break
        
        
            
        
##################################################

    


def transactions(f):
    while True:
        try:
            ifile=open(f,"rb")
            d=0
            while True:
                try:
                    s=pickle.load(ifile)
                    d=1
                    s.display()
                    s.display2()
                    s.display3()
                    s.display4()
                    s.display5()
                    s.display6()
                except EOFError:
                    ifile.close()
                    break
            break
        except NameError:
            print""
            print"\tNo Transactions Made"
            break
    
    print
    menu(f)

            
def demo():
    print"\t\t\t1)Signup"
    print"\t\t\t2)SignIn"
    print"\t\t\t3)Exit"
    print""
    try:
        a=input("\t\t     Enter Choice-")
    except SyntaxError:
        print"\t\tNO Input"
        demo()
    except NameError:
        print"Invalid Input"
        demo()
        
    if a==1:
        signup()
        
    if a==2:
        signin()
    
    if a==3:
        print"\t\t Bye..........."
    
    if a!=1 or a!=2 or a!=3:
        print"Invalid Input"
        demo()
        
def addmoney(f):
    ofile=open(f,"ab+")
    m=0
    while True:
        try:
            m=pickle.load(ofile).bal
        except EOFError:
            break
    s=main()
    s.enter(m)
    print"\tCurrent Balance-",s.bal
    print""
    pickle.dump(s,ofile)
    ofile.close()
    p=str(raw_input("\tWant To Add More?(Y/N)-"))
    if p=="y":
        addmoney(f)
    else:
        menu(f)


#------------------------------------------------------------------------------------------------

  
    

def payspace():
    print""
    print"________________________________________________________________"
    print"           ____              _____                              "
    print"          / __ \____ ___  __/ ___/____  ____ _________          "
    print"         / /_/ / __ `/ / / /\__ \/ __ \/ __ `/ ___/ _ \         "
    print"        / ____/ /_/ / /_/ /___/ / /_/ / /_/ / /__/  __/         "
    print"       /_/    \__,_/\__, //____/ .___/\__,_/\___/\___/          "
    print"                   /____/     /_/                               "  
    print"________________________________________________________________"
    print""
    
def recharge(f):
    print"\t   Prepaid Recharge"
    while True:
        try:
            ofile=open(f,"ab+")
            m=0
            while True:
                try:
                    m=pickle.load(ofile).bal
                except EOFError:
                    break
            s=main()
            s.enter1(m,f)
            s.show1()
            print"\tCurrent Balance-",s.bal
            print""
            pickle.dump(s,ofile)
            ofile.close()
            menu(f)
            break
        except AttributeError:
            menu(f)
    else:
        print"\tInvalid Input"
        menu(f)


def bill(f):
    print"\t  a)Electricity Bill"
    print"\t  b)Gas Bill"
    print"\t  c)Water Bill"
    print"\t  d)PostPaid Bill"
    print"\t  e)Back"
    try:
        ch1=str(raw_input("\tEnter Category Of Bill-"))
        if ch1.isdigit():
            print"Invalid Input"
        if ch1=="null":
            print"Invalid Input"
    except SyntaxError:
        print"Invalid Input"
        bill(f)
    except NameError:
        print"Invalid Input"
        bill(f)
    except ValueError:
        print"Invalid Input"
        bill(f)
    if ch1=="a":
        while True:
            try:
                ofile=open(f,"ab+")
                m=0
                while True:
                    try:
                        m=pickle.load(ofile).bal
                    except EOFError:
                        break
                s=main()
                s.enter3(m,f)
                s.play()
                print"\tCurrent Balance-",s.bal
                print""
                pickle.dump(s,ofile)
                ofile.close()
                menu(f)
                break
            except AttributeError:
                menu(f)
        
    if ch1=="b":
        while True:
            try:
                ofile=open(f,"ab+")
                m=0
                while True:
                    try:
                        m=pickle.load(ofile).bal
                    except EOFError:
                        break
                s=main()
                s.enter4(m,f)
                s.play1()
                print"\tCurrent Balance-",s.bal
                print""
                pickle.dump(s,ofile)
                ofile.close()
                menu(f)
                break
            except AttributeError:
                menu(f)
        
    if ch1=="c":
        while True:
            try:
                ofile=open(f,"ab+")
                m=0
                while True:
                    try:
                        m=pickle.load(ofile).bal
                    except EOFError:
                        break
                s=main()
                s.enter5(m,f)
                s.play2()
                print"\tCurrent Balance-",s.bal
                print""
                pickle.dump(s,ofile)
                ofile.close()
                menu(f)
                break
            except AttributeError:
                menu(f)
    if ch1=="d":
        while True:
            try:
                ofile=open(f,"ab+")
                m=0
                while True:
                    try:
                        m=pickle.load(ofile).bal
                    except EOFError:
                        break
                s=main()
                s.enter2(m,f)
                s.show2()
                print"\tCurrent Balance-",s.bal
                print""
                pickle.dump(s,ofile)
                ofile.close()
                menu(f)
                break
            except AttributeError:
                menu(f)
        
    if ch1=="e":
        menu(f)
    
      






    




import pickle
def menu(f):
    ofile=open(f,"ab+")
    while True:
        try:
            m=pickle.load(ofile).bal
        except EOFError:
            break
    print""
    print"________________________________________________________________"
    print"________________________________________________________________"
    print"\t\tOPTIONS AVAIALABLE :","\t Balance-",m
    print""
    print"\t\t1)ADD MONEY TO ACCOUNT"
    print"\t\t2)PAY BILLS "
    print"\t\t3)RECHARGE MOBILE"
    print"\t\t4)SEE TRANSACTIONS"
    print"\t\t5)EXIT"
    print"________________________________________________________________"
    print"________________________________________________________________"
    
    try:
        z=int(raw_input("\t\tEnter your choice :"))
    except ValueError:
        print"Invalid Input"
    except UnboundLocalError:
        print"Invalid Input"
    if z=="":
        print"Invalid Input"
    
    
    
    if z==1:
        addmoney(f)
    if z==2:
        bill(f)      
    if z==3:
        recharge(f)
    if z==4:
        transactions(f)
    if z==5:
        print"\t\tLogged Out"
        demo()
payspace()
demo()
'''
print"                 ****************************"
    print"                 |                          |"
    print"                 |         WELCOME          |"
    print"                 |            TO            |"
    print"                 |         PAYSPACE !!      |"
    print"                 |                          |"
    print"                 |                          |"
    print"                 |                          |"
    print"                 ============================"
    print"                 |            <o>           |"
    print"                 ============================"
    print"                              ||            "
    print"                    __________||__________"
    print""
    print"________________________________________________________________"
    print""

'''
