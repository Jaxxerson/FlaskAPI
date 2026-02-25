from flask import *

# initialize the flask application
app=Flask(__name__)

# define the route

@app.route("/api/home")
def home():
    return jsonify({"Message":"Welcome to Home API"})

#create a route for products
@app.route("/api/product")
def product():
    return jsonify({"Message":"Welcome to Product API"})

# create a route for services
@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to Our Services API"})

# creating a route to accept user input
@app.route("/api/calc", methods=["POST"])
def calc():
    num1=int(request.form["num1"])
    num2=int(request.form["num2"])

    sum=num1+num2
    
    return jsonify ({"answer":sum})

@app.route("/api/multi", methods=["POST"])
def multi():
    number1=int(request.form["number1"])
    number2=int(request.form["number2"])

    prod=number1*number2

    return jsonify({"Product":prod})

@app.route("/api/floor", methods=["POST"])
def floor():
    no1=int(request.form("no1"))
    no2=int(request.form("no2"))

    floor=no1//no2
    
    return jsonify({"Answer":floor})

app.run(debug=True)
