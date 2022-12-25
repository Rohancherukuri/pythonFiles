# Program to check whether a phone number is 
# valid or not 
import phonenumbers as pn

if __name__ == "__main__":
    try:
        # Parsing String to Phone number 
        phone_number = pn.parse("+91987654321") 
        # Validating a phone number 
        valid = pn.is_valid_number(phone_number) 
        # Checking possibility of a number 
        possible = pn.is_possible_number(phone_number) 
        # Printing the output 
        print(valid) 
        print(possible)
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e)) 
