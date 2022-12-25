# Handling key board interrupt exception in python

import getpass as gp

try:
    userid = input("Enter your UserId: ")
    passwd = gp.getpass("Enter your password: ")

    print("Your UserId is : "+userid)
    print("Your password is: {}".format(len(passwd)*"*"))
    if userid == "Rohan" and passwd == "ch2k1@3863":
        print("You can access this code.")
    else:
        print("Sorry Your username or password was incorrect try typing correctly.")
        exit()
except (KeyboardInterrupt,Exception) as e:
    print("OOPS unable to retrieve information")