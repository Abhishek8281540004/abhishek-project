master_pwd = input("what is the master password? ")
def view():
     with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print("user:", user, "password:", passw)
            #rstrip() - used for removing new extra lines in passwords.txt file


def add():
    name=input("accout name: ")
    pwd=input("password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|"+ pwd +"\n")


while True:
    mode=input("would you like to add a new password or view existing ones(view/ add)press q to quit ")
    if mode =="q":
        break
    elif mode=="view":
        view()
    elif mode=="add":
        add()

    else:
        print("invalid mode")
        continue