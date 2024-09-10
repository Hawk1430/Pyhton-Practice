username = input("Enter username: ")
length = len(username)
if(len(username) <=12 and username.isalpha()):
    print("Username accepted")
else:
    print("Username not accepted")
