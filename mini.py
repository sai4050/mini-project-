from datetime import datetime
name=input("enter your name")
lists= '''
Rice= 1kg/70rs
wheat=1kg/50rs
sugar=1kg/40rs
salt= 1kg/30rs
tomato=1kg/20rs
onoin=20rsvg 

'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
items={'rice':20,'wheat':20,'tomoto':30,'sugar':20,'salt':30,'tomato':20,'onion':20}
option=int(input("for list of items enter 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if  you want to buy press1"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items")
        quanity=int(input("enter how much you want  "))
        if item in items.keys():
            price=quanity*(items[item])
            pricelist.append((item,quanity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quanity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice  
        else:
            print("not availble")    
    else:
        print("wrong num") 
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        pass
    if finalamount!=0:
        print(25*"=""emart",25*"=")
        print(28*",""kadapa")
        print("Name:",30*" ","Date:",datetime.now())
        print(75*"-") 
        print("sno",8*" ",'items',8*" " ,'qunaity' ,3*" ","price")  
        for i in range(len(pricelist)):
            print(i,ilist[i],qlist[i],plist[i])
        print(75*"_")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print("gst amount",50*" ",'Rs',gst)
        print(50*" ",'finalAmount:','Rs',finalamount)
        print(75*"_")
        print(50*" ","thanks")
        print(75*"-")