import mysql.connector
# GLOBAL VARIABLES DECLARATION
myConnnection =""
cursor=""
userName="ENTER_YOUR_USERNAME"    #don't forget to add your username before execution !!!
password ="ENTER_YOUR_MySQL_PASSWORD_HERE"    #don't forget to add your Password before execution !!!
cid=""
#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck ():
 
 global myConnection
 global userName
 global password
 
 myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password , 
auth_plugin='mysql_native_password' )
 if myConnection:
     print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
     cursor=myConnection.cursor()
     cursor.execute("CREATE DATABASE IF NOT EXISTS ATM")
     cursor.execute("COMMIT")
     cursor.close()
     return myConnection
 else:
     print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")
 
#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection ():
    global userName
    global password
    global myConnection
    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password ,database="ATM" , auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()
# MODULE TO CREATE NEW CUSTOMER
def newCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        createTable =("CREATE TABLE IF NOT EXISTS CUSTOMER(CID INT(10) PRIMARY KEY ,CNAME VARCHAR(30) NOT NULL,ADDRESS VARCHAR(30)NOT NULL ,PHONE VARCHAR(55) NOT NULL);")
        cursor.execute(createTable)
        cursor.execute("COMMIT")
        print("table is created")
        print("\nPlease Fill All The Information Carefully !")
        cid=input("Please Enter Customer ID : ")
        cname=input("Please Enter Customer Name : ")
        address=input("Please Enter Customer Address : ")
        phone=input("Please Enter Customer Contact No. : ")
        sql=('INSERT INTO CUSTOMER(cid,cname,address,phone) values(%s,%s,%s,%s);')
        values=(cid,cname,address,phone)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nNew Customer Added Successfully !")
 
# MODULE TO DISPLAY CUSTOMER INFORMATION :
def displayAllCustomer():
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("SELECT * FROM CUSTOMER;")
        data = cursor.fetchall()
        if data:
            print("\n*****DETAILS OF ALL CUSTOMER*****")
            data=pd.DataFrame(data,columns=['Customer_ID','Name','Address','Phone'])
            print(data)
        else:
            print("Sorry ! No Record Found , Please Try Again ! ")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
 
# MODULE TO SEARCH A CUSTOMER 
def searchCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("Please Enter Customer ID : ")
        sql=("SELECT * FROM CUSTOMER WHERE CID =%s")
        values=(cid,)
        data=cursor.execute(sql,values)
        data = cursor.fetchall()
        if data:
            print("\n*****CUSTOMER DETAILS*****")
            data=pd.DataFrame(data,columns=['Customer_ID','Name','Address','Phone'])
            print(data)
        else:
            print("Sorry , Customer NOT Found , Please Try Again ! ")
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")
 
# MODULE TO OPEN A NEW ACCOUNT
def newAccount():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("Please Enter Customer ID : ")
        sql=("SELECT * FROM CUSTOMER WHERE CID =%s")
        values=(cid,)
        data=cursor.execute(sql,values)
        data = cursor.fetchall()
        if data:
            createTable =("CREATE TABLE IF NOT EXISTS ACCOUNT(CID INT(60),ACCOUNT_NO INT(20) PRIMARY KEY,ACCOUNT_TYPE VARCHAR(90) NOT NULL ,AMOUNT INT(99) NOT NULL , PIN INT(44) NOT NULL UNIQUE);")
            cursor.execute(createTable)
            account_no=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: ")) 
            account_type=input("PLEASE ENTER THE ACCOUNT TYPE [ S-SAVING / C - CURRENT : ") 
            amount=int(input("PLEASE ENTER THE AMOUNT TO DEPOSIT : "))
            pin=int(input("PLEASE ENTER THE ATM PIN [ FOUR DIGITIS ONLY ] : "))
            sql=('INSERT INTO ACCOUNT (cid,account_no,account_type,amount ,pin) values(%s,%s,%s,%s,%s);')
            values= (cid,account_no,account_type,amount,pin)
            cursor.execute(sql,values)

            cursor.execute("COMMIT")
            cursor.close()
            print("\nNew Account Added Successfully !")



        else:
            print("Sorry ! Customer NOT Found , Please Try Again ! ")
    else:
        print("\nSomthing Went Wrong ,Please Try Again !") 
# MODULE TO DISPLAY ALL ACCOUNTS
import pandas as pd
def displayAllAccounts():
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("SELECT * FROM ACCOUNT")
        data = cursor.fetchall()
        if data:
            print("\n*****DETAILS OF ALL CUSTOMER*****")
            data=pd.DataFrame(data,columns=['Customer_ID','Account_No','Account_type','Amount','Pin'])
            print(data)
        else:
            print("Sorry ! No Account Information , Please Try Again ! ")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
 
 
# 6--MODULE TO SEARCH AN ACCOUNT 
def searchAccount():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("PLEASE ENTER CUSTOMER ID : ")
        account_no=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
        sql="SELECT * FROM ACCOUNT WHERE CID = %s AND ACCOUNT_NO =%s"
        values=(cid,account_no)
        data=cursor.execute(sql,values)
        data = cursor.fetchall()
        data=pd.DataFrame(data,columns=['Customer_ID','Account_No','Account_type','Amount','Pin'])
        print(data)
        if data:
            print("\n*****CUSTOMER ACCOUNT DETAILS*****")
        else:
            print("Sorry ! Account Infromation NOT Found , Please Try Again ! ")
    else:
        print("Somthing Went Wrong ,Please Try Again !") 
# MODULE TO WITHDRAW AMOUNT 
def withdrawAmount():
    count =3
    if myConnection:
        cursor=myConnection.cursor()
        account_no=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
        sql="SELECT * FROM ACCOUNT WHERE ACCOUNT_NO =%s"
        values=(account_no,)
        data=cursor.execute(sql,values)
        data = cursor.fetchone()
        if data:
            while True:
                balance = data[3]
                PIN=int(input("PLEASE ENTER THE ATM PIN - ONLY 3 ATTEMPTS ARE ALLOWED : ")) 
                sql=('SELECT * FROM ACCOUNT WHERE PIN = %s')
                values=(PIN,)
                cursor.execute(sql,values)
                data = cursor.fetchone()
                if data:
                    amount=int(input("PLEASE ENTER AMOUNT TO WITHDRAW : "))
                    if amount>balance:
                        print("NOT ENOUGH DEPOSIT !")
                    else:
                        sql=('UPDATE ACCOUNT SET AMOUNT = AMOUNT - %s')
                        cursor.execute(sql ,(amount,))
                        cursor.execute("COMMIT")
                        print("******* TRANSACTION SUCCESSFULLY COMPLETED ! *******")
                        print("***** PLEASE TAKE THE MONEY AND REMOVE YOUR CARD ! *****")
                        break
                else:
                    print("Wrong Pin ! Please enter a Valid PIN")
                    count=count-1
                    print("You are left with only ",count ,"Attempts")
                    if count == 0:
                        print("Your Card has been Blocked , Please Visit the Branch to activate it")
                        break

                    else:
                        print("Sorry ! Account Infromation NOT Found , Please Try Again ! ")
 
#MODULE TO PROVIDE HELP FOR USER 
def helpMe():
    print("Please, Visit The Offcial Website Of our Bank !!!")
 
# MAIN SCREEN
print("*******************ATM MANAGEMENT*****************") 
#STARTING POINT OF THE SYSTEM
myConnection = MYSQLconnectionCheck ()
if myConnection:
    MYSQLconnection()
    while(1):
        print("\n!=========================*************=======================!")
        print("! PLEASE ENTER 1 FOR NEW USER !")
        print("! PLEASE ENTER 2 TO DISPLAY ALL CUSTOMERS !")
        print("! PLEASE ENTER 3 TO SEARCH A CUSTOMER !")
        print("! PLEASE ENTER 4 TO OPEN NEW ACCOUNT !")
        print("! PLEASE ENTER 5 TO DISPLAY ALL ACCOUNTS !")
        print("! PLEASE ENTER 6 TO SEARCH AN ACCOUNT !")
        print("! PLEASE ENTER 7 TO WITHDRAW AMOUNT !")
        print("! PLEASE ENTER 8 TO EXIT !")
        print("! PLEASE ENTER 0 FOR HELP !")
        print("\n!============================*****END*****====================!")
        choice = int(input("\n Please Enter Your Choice : "))
        if choice == 1:
            newCustomer()
        elif choice == 2:
            displayAllCustomer()
        elif choice == 3:
            searchCustomer()
        elif choice == 4:
            newAccount()
        elif choice==5:
            displayAllAccounts()
        elif choice==6:
            searchAccount()
        elif choice==7:
            withdrawAmount()
        elif choice==8:
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(" T T H H A A N N K K ")
            print(" T T H H A A N N K K ")
            print(" T T H H A A N N K K K Y Y O O U U ")
            print(" T T H H A A N N K K Y Y O O U U ")
            print(" T T H H A A N N K K O O U U ")
            print(" Y O O U U ")
            print(" Y OOOO UUUU ")
            print("\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600","\U0001f600")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 
            print("END OF THE PROJECT")
            print("*****PLEASE RATE US!!!*****")
            y=input("enter your name :")
            print("1,2,3,4 or 5")
            x=int(input("RATE US : "))

            
            if x <= 3:
                print("Hello",y,"THANK YOU FOR YOUR FEEDBACK,WE WILL TRY TO SOLVE THIS ISSUE AS SOON AS POSSIBLE,THANK YOU.")
            else:
                print("THANK YOU",y,"!!!","\U0001f600","\U0001f600","\U0001f600")
            break
        elif choice==0:
            helpMe()
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("Check Your MYSQL Connection And Try Again !!! ")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(" T T H H A A N N K K ")
    print(" T T H H A A N N K K ")
    print(" T T H H A A N N K K K Y Y O O U U ")
    print(" T T H H A A N N K K Y Y O O U U ")
    print(" T T H H A A N N K K O O U U ")
    print(" Y O O U U ")
    print(" Y OOOO UUUU ")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 
    print("END OF THE PROJECT")
