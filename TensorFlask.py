# Creating a flask app and two tensors
from torch import tensor
from flask import Flask

app = Flask(__name__)
@app.route("/sum/<int:n1>/<int:n2>",methods = ["GET","POST"])
def tensorSum(n1,n2):
    n3 = n1 + n2
    return "The Sum is: "+str(n3)
@app.route("/tensor",methods = ["GET","POST"])
def returnTensor():
    t1 = tensor([1,2,3,4,5])
    t2 = tensor([1,2,3,4,5])
    t3 = t1 + t2
    return "The Sum of two tensors is : "+str(t3)
if __name__ == "__main__":
    app.run(debug = True)
