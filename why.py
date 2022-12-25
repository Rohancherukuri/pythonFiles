from time import time
from flask import Flask


app = Flask(__name__)

def main():
    app.run(debug = True)

@app.route("/home/<int:id>/<float:unqno>")
def func1(id,unqno):
    return "Your ID is: "+str(id)+" and your unique number is: "+str(unqno)+"\n"

@app.route("/home/<string:msg>")
def func2(msg):
    return "Hello "+msg+" welcome to my webpage!\n"


if __name__ == "__main__":
    try:
        t1 = time()
        main()
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
        
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")