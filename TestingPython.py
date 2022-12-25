def hi(msg = ""):
    return "Hi"+" "+msg

message = hi
msg = input("Enter a message to be sent to the function: ")
print(message(msg))   
