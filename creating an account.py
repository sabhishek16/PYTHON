d = {}
while True:
    ch = input("enter 1 for registration\n,enter 2 for login\n,enter 3 for update\n,enter 4 for delete")
    print(d)
    if ch == "1":#registration
        user = input("enter username")
        if user in d.keys():
            print("user already exist")
        else:
            password = input("enter password")
            d[user] = password
        print(d)
    if ch == "2":# login
        user = input("enter username")
        if user in d.keys():
            password = input("enter password")
            if d[user]== password:
                print("success")
            else:
                print("password incorrect")
        else:
            print("regeter yourself")
    elif ch == "3":#update
        print(d)
        user = input("enter the username")
        if user in d.keys():
            password =input("enter the password")
            if d[user] == password:
                npd = input("enter new password")
                d[user]=npd
            else:
                print("incorrect password")
        else:
            print("register  again")
    elif ch == "4":#delete
        print(d)
        user = input("enter the username")
        if user in d.keys():
            password = input("enter the password")
            if d[user] == password:
                del d[user]
                print("account deleted")
            else:
                print("failed")
        else:
                print("register once again")
            
    
        
                
                   
                   
