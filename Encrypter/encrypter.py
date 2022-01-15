from cryptography.fernet import Fernet
run=True

key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt(site, pw):
    encMessage = fernet.encrypt(pw.encode())
    file=open("Data/"+site+".txt",'wb')
    file.write(encMessage)
    print("Encrypted password successfully!")

def decrypt(site):
    with open("Data/"+site+".txt", "rb") as file:
       data = file.readlines()
       for line in data:
        print(fernet.decrypt(line).decode())
               
while(run):
    print("~~~~~Password Encrypter~~~~~~~~")
    print("Enter your choice")
    x=int(input("1.Add password \n2.View password \n"))
    if(x==1):
        site=input("Enter Site: ")
        pw=input("Enter password: ")
        encrypt(site,pw)
    else:
        if(x==2):
            site=input("Enter Site: ")
            decrypt(site)
            
    v=input("Do you want to continue y/n : ")
    if(v!="y"):
        break




    
