
import json

d = {}

with open("reg_login_update_delete.json","w")as fb:
    fb.write(json.dumps(d,indent=4))

while True:
    ch = input("enter choice:\n 1 -reg,\n2-login,\n3-update,\n4-delete\n")

    
    if ch == "1":   #REGISTRATION
        ID = input("enter userID")
        with open("reg_login_update_delete.json","r")as fb:
            y = fb.read()
            m = json.loads(y)
            if ID in m.keys():
                print("userID already exists,select another ID")
            else:
                pwd = input("enter password")
                d[ID] = pwd
            print(d)
            with open("reg_login_update_delete.json","w")as fb:
                fb.write(json.dumps(d,indent=4))
                
    elif ch == "2": #LOGIN
        ID = input("enter userID")
        with open("reg_login_update_delete.json","r")as fb:
            y = fb.read()
            m = json.loads(y)
            if ID in m.keys():
                pwd = input("enter password")
                if m[ID] == pwd:
                    print("success")
                else:
                    print("incorrect password")
            else:
                print("register  yourself")
    elif ch == "3":  #UPDATE
        ID = input("enter userID")
        with open("reg_login_update_delete.json","r")as fb:
            y = fb.read()
            m = json.loads(y)
            if ID in m.keys():
                pwd = input("enter password")
                if m[ID] == pwd:
                    print("success")
                    npwd = input("enter new password")
                    m[ID] = npwd
                    with open("reg_login_update_delete.json","w")as fb:
                        fb.write(json.dumps(m,indent=4))
                        print(m)
                else:
                    print("incorrect password")
            else:
                print("go to registration")
    elif ch == "4":   # DELETE
        ID = input("enter userID")
        with open("reg_login_update_delete.json","r")as fb:
            y = fb.read()
            m = json.loads(y)
            if ID in m.keys():
                pwd = input("enter password")
                if m[ID] == pwd:
                    print("success")
                    m.pop(ID)
                    with open("reg_login_update_delete.json","w")as fb:
                        fb.write(json.dumps(m,indent=4))
                        print(m)
                else:
                    print("incorrect password")
            else:
                print("go to registration")
        
            
        
