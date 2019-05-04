#def detail gives the details of the books 
def detail(book_choose):
    detail="Name of book: "+ book_choose[0]+"\nWriter name: "+book_choose[1]+"\nquantity we have in stock: "+ book_choose[2]+"\nprice: "+book_choose[3]
    return detail
#def book_pick gives the books you can pick from list
def book_picked(items):
    print("\nHere are the list of books for borrowing:\n")
    for i in range (len(items)):
        print(i+l," ",items[i][0],"by",items[i][1])
    print("####***********************************************####")
    ans="y"
    while ans.upper()=="Y":
        book_num = int(input("which number book do you want to borrow?(1 ,2 , 3):"))
    if book_num.upper == 1:
        print ("Book Info:\nTitle : ",list1[0][0],"\nAuthor : ",list1 [0][1],"\nQuantity : ",list1[0][2],"\nPrice : ",list1[0][3],"\n")
        price = list1[0][3].replace("$"," ")
        book_picked[list1[0][0]]=float(price)
        ans="n"
    elif book_num.upper == 2:
        print ("Book Info:\nTitle : ",list1[1][0],"\nAuthor : ",list1 [1][1],"\nQuantity : ",list1[1][2],"\nPrice : ",list1[1][3],"\n")
        price = list1[1][3].replace("$"," ")
        book_picked[list1[1][0]]=float(price)
        ans="n"
    elif book_num.upper == 3:
        print ("Book Info:\nTitle : ",list1[2][0],"\nAuthor : ",list1 [2][1],"\nQuantity : ",list1[2][2],"\nPrice : ",list1[2][3],"\n")
        price = list1[2][3].replace("$"," ")
        book_picked[list1[2][0]]=float(price)
        ans="n"
    else:
        print ("Given Book Number Invalid\n ")
    print("####**********************************************####")
def item(file_name):
    list2=[]
    file = open(file_name,'r')
    item=file.readlines()
    for content in item:
        list1=[]
        detail=content.replace("\n","").split(",")
        for i in detail:
            list1.append(i)
        list2.append(list1)
    file.close()
    return list2
def write (file_name,items):
    file=open(file_name,"w")
    for i in items:
        line=",".join(i)
        file.write(line+"\n")
    return
def valid_date(date):
    date_day=[]
    for day in range(1,32):
        date_day.append(str(day))
    date_month=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    date=date.split("/")
    while date[0] in date_day and date[1].upper()in date_month:
        valid= True
    else:
        valid=False
    return valid


print("                   Welcome To Libary              ")
books_borrowed=[]
name=input("Enter your Name: ")
ans=input("Do you want to borrow a book?(y/n): ")
while ans == "y":
    book_choosen=book_picked(items)
    print(details(book_choosen))
    confirmed = input("Are you sure you want borrow this book from libary?(y/n): ")
    while confirmed!='y' and confirmed!='n':
        confirmed=input("Please enter either y or n for above asked question: ")
    if confirmed =='y':
        while confirmed.upper=="Y":
            num = int(input("How many books do you want to borrow : "))
            list3.append(num)
            if book_num.upper()== 1 and num <=int(list1[0][2]):
                list1[0][2]=str(int(list[0][2])-num)
                list2.append(num*book_picked[list1[0][0]])
                total_price = price*num
                grand_total=grand_total+total_price
                print("total price =  $", total_price)
                print("grand total =  $", grand_total)
            elif book_num.upper()== 2 and num <=int(list1[1][2]):
                list1[1][2]=str(int(list[1][2])-num)
                list2.append(num*book_picked[list1[1][0]])
                total_price = price*num
                grand_total=grand_total+total_price
                print("total price =  $", total_price)
                print("grand total =  $", grand_total)
            elif book_num.upper()== 3 and num <=int(list1[2][2]):
                list1[0][2]=str(int(list[0][2])-num)
                list2.append(num*book_picked[list1[2][0]])
                total_price = price*num
                grand_total=grand_total+total_price
                print("total price =  $", total_price)
                print("grand total =  $", grand_total)
            else:
                print("The Book you want to borrow is out of stock ,Please come after some days.")


    ans=input("\n Do you want to borrow next book?(y/n): ")
    #Date
    #Return
    #Write2Dlist
                
        
    
        
            
   
    















    
