# Using python logging module
import logging
import time as tm
start_time = tm.time()
logging.basicConfig(filename = "student.log",level = logging.INFO)

class Student:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        logging.info("Created Student: {} {}".format(self.fullname,self.email))
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first_name,self.last_name)
    @property
    def fullname(self):
        return "{} {}".format(self.first_name,self.last_name)
if __name__ == "__main__":
    try:
        s1 = Student("Rohan","Cherukuri")
        s2 = Student("Srinivas","Chella")
        s3 = Student("Abhishek","Mittapalli")
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
        
    finally:
        print("Finished in: {} sec".format(tm.time() - start_time))
        
