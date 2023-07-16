#nbill.py
#functions
import smtplib
from email.mime.text import MIMEText
import pickle
import os
found = False

def append(name,product,total,date,time,gm):
    f = open("f:\\binaryfiles\\newbill.dat","ab")
    billno = billcr("newbill")
    billcup("newbill")
    rec = [billno,name,product,total,date,time,gm]
    pickle.dump(rec,f)
    f.close()
    fgm(billno,name,product,total,date,time,gm)


def fgm(billno,name,product,total,date,time,gm):
    subject = "| ADARSH CLOTH STORE |"
    msg1 = "Customer name "+ name.capitalize()+",\n\n"
    dati = "DATE: "+date+"\n\nTIME: "+time+"\nBILL NO: "+str(billno)
    
    desc = "\n\nS.no\tDESCRIPTION\t Meter\t   Price\n"
    
    l = len(product)
    spro =""
    for i in range(l):
        spro = spro + str(i+1)+"\t\t"+product[i][0]+'\t\t'+str(product[i][1])+'\t\t'+str(product[i][2])+"\n"
    
    
    msgtot ="\nTOTAL PAYMENT "+str(total)
    thk = "\n\nTHANKYOU FOR VISITING OUR STORE"
    body = msg1+dati+desc+spro+msgtot+thk
    sender = "adarshvastrabhandar1@gmail.com"
    recipients = ["adarshvastrabhandar1@gmail.com",gm]
    password = "ptnhivaibrykoxrl"
    send_email(subject, body, sender, recipients, password)
    

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()    

def custommailsend():
    f = open("f:\\binaryfiles\\newbill.dat","rb")
    bno = int(input("Enter bill no "))
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if bno == rec[0]:
                found = True
                print(rec)
                ch = print("press enter to send the bill to email")
                fgm(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6])
               
                
    except EOFError:
        f.close()
        if found == False:
            print("record not found")
    
def read():
    f = open("f:\\binaryfiles\\newbill.dat","rb")
    try: 
        while True:
              rec = pickle.load(f)
              print(rec)
    except EOFError:
        print("bills printed succesfully")
        f.close()
        
def search():
    f = open("f:\\binaryfiles\\newbill.dat","rb")
    bno = int(input("Enter bill no "))
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if bno in rec[0]:
                found = True
                print(rec)
                c = input("PRESS ENTER WHEN YOU HAVE DONE")
    except EOFError:
        f.close()
        if found == False:
            print("record not found")
            
def update():
    f = open("f:\\binaryfiles\\newbill.dat","rb")
    f2 = open("f:\\temp.dat","ab")
    bno = int(input("enter bill no you want to update"))
    found = False
    try:
        while True:
           rec =  pickle.load(f)
           if rec[0]==bno:
               found = True
               name = imput("enter customer name")
               product = eval(input("enter list of products"))
               total = int(input("enter total pay"))
               nrec = [name,product,total,r[3],r[4]]
               ngm = input("Enter new gmail")
               pickle.dump(nrec,f2)
           else:
               pickle.dump(rec,f2)
    except EOFError:
        f.close()
        f2.close()
        if found == True:
            print("updated succesfully")
        else:
            print("bill not found")
        os.remove("f:\\binaryfiles\\newbill.dat")
        os.rename("f:\\temp.dat","f:\\binaryfiles\\newbill.dat")
        
def delete():
     f = open("f:\\binaryfiles\\newbill.dat","rb")
     f1 = open("f:\\temp.dat","ab")
     bno = int(input("Enter bill no:"))
     found = False
     try:
        while True:
             rec = pickle.load(f)
             if rec[0] == bno:
                 found = True
                 continue
             else:
                pickle.dump(rec,f1)
     except EOFError:
          f.close()
          f1.close()
          if found == True:
              print("Record deleted Succesfull")
          else:
              print("record not found")
          os.remove("f:\\binaryfiles\\newbill.dat")
          os.rename("f:\\temp.dat","f:\\binaryfiles\\newbill.dat")
          
        
            
            
#functions related to bill counting            
def billcapp():
    f = open("e:\\desktop\\billc.dat","ab")
    billname = input("enter bill name")
    rec = [billname,0]
    pickle.dump(rec,f)
    f.close()
    
def billcup(billname):
    f1 = open("e:\\desktop\\billc.dat","rb")
    f2 = open("e:\\desktop\\temp.dat","ab")
    bill = billname
    found = False
    try:
      while True:
           rec = pickle.load(f1)
           if rec[0] == bill:
              found = True
              newc = rec[1] + 1
              rec1 = [bill,newc]
              pickle.dump(rec1,f2)
           else:
               pickle.dump(rec,f2)
    except EOFError:
        if found == True:
            print("__________")
    f1.close()
    f2.close()
    
    os.remove(r"e:/desktop/billc.dat")
    os.rename(r"e:/desktop/temp.dat",r"e:/desktop/billc.dat")
    if found == True:
       print("count updated")
        
def billcr(billname):
    f1 = open("e:\\desktop\\billc.dat","rb")
    try:
         while True:
               rec = pickle.load(f1)
               if rec[0] == billname:
                  f1.close()
                  return rec[1]
    except EOFError:
         print("bill not found")
            
    
def control():
    
    print("Press 1 see all bills")
    print("press 2 to update any record")
    print("press _ for stop reduntancy")
    print("press 5 t")
    print("press 3 to backup the data")
    if ch == 1:
        search()
    elif ch == 2:
        update()
    elif ch == 3:
         os.rename('f:binaryfiles\\temp.dat','f:binaryfiles\\newbill.dat')
         print("DATA BACKEDUP")
        
        
  
    

              
    
            
    

#display
#delete
#update
