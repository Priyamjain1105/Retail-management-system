#newbill
from playsound import playsound
from datetime import date
import mine.newbill as v
today = date.today()
d2 = today.strftime("%B %d, %Y")
import time
o = time.localtime()
ct = time.strftime("%H:%M:%S", o)
print(d2,ct)
print()
name = ""
gm = ""

#functions
def code():
    global name
    global gm
    playsound('e:\\bill\\intro.wav')
    print("WELCOME TO ADARSH VASTRA BHANDAR")
    playsound('e:\\bill\\welACS.mp3')
    time.sleep(2)
    playsound('e:\\bill\\name.mp3')
    name1 = input("Please enter your name:")
    name = name+name1
    playsound('e:\\bill\\gm.mp3')
    gm = input("Please Enter your gmail:")
    
    print("\n\nHEY "+name.upper()+" CHOOSE THE OPTION BELOW")
    menu()
    
prods = []

def menu():
    print('''PRESS 1 FOR BUYING
PRESS 2 FOR CHECKING YOUR LAST PURCHASE''')
    playsound("e:\\bill\\fch.mp3")
    ch = int(input("Please enter your chooise:"))
    if ch == 1:
       buy()
    elif ch == 2:
        checking()
    else:
        print("wrong chooise\n\n_________________________________")
        menu()

product = ""

def buy():
    global product
    sz = 0
    p = 100
    print("\n\n    BUYING")
    print("CHOOSE THE OPTION BELOW")
    print('''PRESS 1 FOR SHIRT
PRESS 2 FOR PENT
PRESS 3 FOR COURT
PRESS 4 FOR JACKET
PRESS 5 FOR SAREE''')
    playsound('e:\\bill\\cata.mp3')
    time.sleep(1)
    playsound('e:\\bill\\ch.mp3')
    
    ch = int(input("Enter you chooise:"))
    if ch == 1:
       product = "shirt"
    elif ch == 2:
       product = "pent"
    elif ch == 3:
       product = "court"
    elif ch == 4:
       product = "jacket"
    elif ch == 5:
       product = "saree"
    elif ch == 6:
       product = "dhoti"
    else:
       print("WRONG CHOICE\n\n\n_________________")
    buying(product)   
    
l = {"shirt":(1.25,1.75,1.50,2.00),"pent":(1,2),"court":(1,2,3),"jacket":(1,4),"saree":(1,2,3),"dhoti":(1,2,3)}
tot = 0


def buying(pro):
    global tot
    c = 1
    p = 100
    global l
    global prods
    
    print("\n\n   "+pro.upper())
    print("\nplease choose your size")
    
    key = l[pro]
    for i in key:
        print("PRESS "+str(c)+" for "+str(i)+ " Meter")
        c=c+1
    print("Press 0 for custom")
    playsound('e:\\bill\\size.mp3')
    time.sleep(1)
    playsound('e:\\bill\\ch.mp3')
    ch = int(input("Enter your chooise:"))
    if ch == 0:
        sz = eval(input("ENTER CUSTOM SIZE"))
    else:    
        sz = l[pro][ch-1]
    print(sz)
    price = p*sz
    tot = tot + price
    prods.append([pro,sz,price])
    print(prods)
    k = True
    while k:
         playsound('e:\\bill\\end.mp3')
         q = input("do you want to continue buying y/n")
         if q == "y":
            buy()
         elif q == "n":
             
            playsound("e:\\bill\\thank.mp3")
            bill()
           
            k = False
            break
         else:
            print("worng choise")
        

def bill():
    global name,prods,tot,d2,ct
    print("THANK YOU FOR SHOPING FROM ADARSH VASTRA BHANDAR")
    v.append(name,prods,tot,d2,ct,gm)
    playsound('e:\\bill\\billsend.mp3')
    print("YOU WILL GET THE BILL ON YOUR GMAIL")
        
        

        

        

        
    

def checking():
    print("menu")
    print('''press 1 for Searching
press 2 for deleting
press 3 for updating
press 4 for reading all bill''')
    ch = int(input("enter your choise:"))
    if ch == 1:
       v.search()
    elif ch>1 and ch<5:
        pw = input("ENTER PASSWORD:")
        if pw == "priyam":
              if ch == 2:
                 v.delete()
              elif ch == 3:
                  v.update()
              elif ch == 4:
                  v.read()
              print("________________________________")    
              menu()    
        else:
            print("wrong password")
            

def custombillsend():
    v.custommailsend()


        
    
        
def newbill():            
    while True:
          code()
          print("-----------------------------------------------thank you-------------------------------------------------"+"\n"*10)
          print("                                              RESTARTING")
          time.sleep(5)
          for i in range(50):
             print("")

newbill()
