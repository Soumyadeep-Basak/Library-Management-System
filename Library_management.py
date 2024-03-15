simport MySQLdb,time,sys
from getpass import getpass
from tabulate import tabulate
from easygui import passwordbox
conn = MySQLdb.connect(host='localhost', user='root', password='deep@4790')
cursor = conn.cursor()
str2 = "create database if not exists pr"
cursor.execute(str2)
cursor.close()
conn.close()
conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
cursor = conn.cursor()
str3 = "create table if not exists library(Id int primary key, Name varchar(20),Author varchar(20),Availibilty varchar(10),issue_name varchar(20))"
str4 = "create table if not exists admin(Username varchar(20) primary key,Password varchar(20))"
cursor.execute(str3)
cursor.execute(str4)
cursor.close()
conn.close()
try:
    conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
    cursor = conn.cursor()
    str567="insert into admin values('deep','4790')"
    cursor.execute(str567)
    conn.commit()
    cursor.close()
    conn.close()
    print("ok")
except:
   print("error")

de=0
str9="Opening Library Management System..."+"\n"
if de!=1:
    dict1={"deep":"4790","srijan":"1234"}
else:
    dict1=dict2
for i in str9:
    print(i,end='')
    time.sleep(0.15)
print("Choose your identity\n1.Librarian \n2.User")
ad=""
ch33=int(input("Enter your choice:"))
if ch33==1:
    username=input("Enter your username: ")
    #password = getpass()
    password=input("Enter your password: ")
    #password =getpass.getpass('Password :: ',sys.stderr)
    #password = passwordbox("Enter password:")
    #print(password)
    try:
        for i in range(1,4):
            if dict1[username]==password:
                str22="Welcome Admin "+username+"\n"
                for i in str22:
                    print(i,end='')
                    time.sleep(0.1)
                print("\n")
                ad="a"
                break
            else:
                print("WRONG PASSWORD!!\nYou have "+str(4-i)+" tries left")
#                username=input("Enter your username: ")
                password=input("Enter your password: ")
    except:
        print("Username is invalid")
        sys.exit()
if ad!="a":
    str23="Welcome User"
    for i in str23:
        print(i,end='')
        time.sleep(0.1)
    print("\n")
print("Main menu: ")
while True:
    print("1.Add Book(Only for librarian) \n2.Remove book(Only for librarian) \n3.Display books \n4.Issue Book \n5.Return Book \n6.Search Book \n7.Management(Only for librarian)")
    ch1=int(input("Enter your choice:"))

    if ch1==1:           
        def insert_rows(a,b,c,d,e=" "):
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            a=str(a)
            str1="insert into library values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"')"
            cursor.execute(str1)
            conn.commit()
            cursor.close()
            conn.close()

        if ad=="a":
            n = int(input('No. of books to be added :'))
            for i in range(0,n):
                x = int(input('Enter id: '))
                y = input('Enter Name: ')
                z = input('Enter Author: ')
                w = input('Availability: ')
                p = input('Issuename: ')
                insert_rows(x,y,z,w,p)
            print(str(n)+"books added")
        else:
            print("WARNING!!\nUser cannot perform this task")

        
    elif ch1==2:
        
        def delete_row(d):
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            str4 = "delete from library where Id='"+d+"'"
            cursor.execute(str4)
            conn.commit()
            print("Book with id '"+d+"' has been removed")
            cursor.close()
            conn.close()

        if ad=="a":
            x=input("enter id")
            delete_row(x)
        else:
            print("WARNING!!\nUser cannot perform this task")





    elif ch1==3:
        print("1.Display all books in alphabetical order \n2.Display issued books \n3.Display available books")
        q=int(input("Enter your choice:"))
        s=""
        l1=[]
        head=["Id","Name","Author","Available","Issue_name"]
        if q==1:
            str10="Displaying all books in alphabetical order\n"
            for i in str10:
                print(i,end='')
                time.sleep(0.1)
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            cursor.execute("select * from library order by Name")
            data = cursor.fetchall()
            for p in data:
                l1.append(p)
            cursor.close()
            conn.close()
            t=(tabulate(l1,headers=head,tablefmt="grid"))
            print(t)
        elif q==2:
            str11="Displaying all issued books\n "
            for i in str11:
                print(i,end='')
                time.sleep(0.1)
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            cursor.execute("select * from library where Availibilty ='I' ")
            data = cursor.fetchall()
            for p in data:
                l1.append(p)
            cursor.close()
            conn.close()
            t=(tabulate(l1,headers=head,tablefmt="grid"))
            print(t)
        elif q==3:
            str12="Displaying all available books\n "
            for i in str12:
                print(i,end='')
                time.sleep(0.1)
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            cursor.execute("select * from library where Availibilty ='A' ")
            data = cursor.fetchall()
            for p in data:
               l1.append(p)
            cursor.close()
            conn.close()
            t=(tabulate(l1,headers=head,tablefmt="grid"))
            print(t)


    elif ch1==4:
        def issue(id1,p):
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            str5 = "update library set Availibilty ='I' where id = '"+str(id1)+"' "
            cursor.execute(str5)
            conn.commit()
            str6="update library set issue_name ='"+p+"' where id = '"+str(id1)+"'"    
            cursor.execute(str6)
            conn.commit()
            cursor.close()
            conn.close()
            print("Book with id '"+str(id1)+"'issued by'"+p+"'")

            
        x = int(input('Enter id: '))
        p=input("Enter issue_name :")
        issue(x,p)

    elif ch1==5:
        def return1(id):
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            str5 = "update library set Availibilty ='A' where id = '"+str(id)+"'"
            cursor.execute(str5)
            conn.commit()
            str6="update library set issue_name = ' ' where id = '"+str(id)+"'"    
            cursor.execute(str6)
            conn.commit()
            cursor.close()
            conn.close()
            print("Book with id '"+str(id)+"' returned")
            
        x = int(input('Enter id: '))
        return1(x)        

    elif ch1==6:
        def search_n():

            l1=[]
            l=[]
            str889=input("Enter the name of the book you want to search :")
            head=["Id","Name","Author","Available","Issue_name"]
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            cursor.execute("select * from library ")
            data = cursor.fetchall()
            str13="Searching...\n"
            for i in str13:
                print(i,end='')
                time.sleep(0.1)
            for p in data:
                l1.append(p)
            cursor.close()
            conn.close()
            for i in l1:
                if str889==i[1]:
                    l.append(i)
            t=(tabulate(l,headers=head,tablefmt="grid"))
            print(t)
        def search_id():
            l1=[]
            l=[]
            str889=int(input("Enter the id of the book you want to search :"))
            head=["Id","Name","Author","Available","Issue_name"]
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            cursor.execute("select * from library ")
            data = cursor.fetchall()
            str13="Searching...\n"
            for i in str13:
                print(i,end='')
                time.sleep(0.1)
            for p in data:
                l1.append(p)
            cursor.close()
            conn.close()
            for i in l1:
                if str889==i[0]:
                    l.append(i)
            t=(tabulate(l,headers=head,tablefmt="grid"))
            print(t)
        def search_au():
            l1=[]
            l=[]
            str889=input("Enter the name of the author whose books you want to search:")
            head=["Id","Name","Author","Available","Issue_name"]
            conn = MySQLdb.connect(host='localhost', database='pr', user='root', password='deep@4790')
            cursor = conn.cursor()
            cursor.execute("select * from library ")
            data = cursor.fetchall()
            str13="Searching...\n"
            for i in str13:
                print(i,end='')
                time.sleep(0.1)
            for p in data:
                l1.append(p)
            cursor.close()
            conn.close()
            for i in l1:
                if str889==i[2]:
                    l.append(i)
            t=(tabulate(l,headers=head,tablefmt="grid"))
            print(t)
        print("1.Search by Book name \n2.Search by ID \n3.Search by Authors name ")
        ch=int(input("Enter your choice :"))
        if ch==1:
            search_n()
        elif ch==2:
            search_id()
        elif ch==3:
            search_au()
    elif ch1==7:
        if ad=="a":
            print("Management menu:")
            print("1.Add Librarian \n2.Change Password \n3.Logout ")
            ch=int(input("Enter your choice :"))
            def logout():
                print("After logging out , you will enter as user for next loop!!!!")
                str14="Logging out...\n"
                for i in str14:
                    print(i,end='')
                    time.sleep(0.1)
                global ad
                ad=""
            def changepassword(d):

                global dict2
                dict2=dict1
                op=input("Enter your old password:")
                if dict2[username]==op:
                    np=input("Enter your new password:")
                    dict2[username]=np
                    print("Your old password "+op+" has been changed to new password "+np)
            def addlib():
                print("a")  

            if ch==1:
                addlib()
            elif ch==2:
                de=1
                changepassword(dict1)
            elif ch==3:
                logout()
        else:
            print("WARNING!!\nUser cannot perform this task")
    ch2=int(input("Press: \n1. to exit \n2. to continue"))
    if ch2==1:
        break
