from flask import *
import pymysql
import os

# initialize flask

app=Flask(__name__)
if not os.path.exists("static/images"):
    os.makedirs("static/images")
app.config["UPLOAD_FOLDER"]="static/images"

@app.route("/api/signup", methods=["POST"])
def signup():
    # request user input
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    # create connection to database
    connection=pymysql.connect(host="localhost", user="root", password="", database="tembo_sokogarden_ryxn")

    # create a cursor
    cursor=connection.cursor()

    # create sql statement to insert data
    sql="insert into users(username, email, password, phone) values(%s,%s,%s,%s)"

    # prepare the data
    data=(username, email, password, phone)

    # execute
    cursor.execute(sql,data)
    
    #commit/save
    connection.commit()
    
    
    # response
    return jsonify ({"Message":"Thank you for joining"})
    
# signin API
# signin route/endpoint
@app.route("/api/signin", methods=["POST"])
def signin():

    # request user input
    email=request.form["email"]
    password=request.form["password"]

    # create connection
    connection=pymysql.connect(host="localhost", user="root", password="", database="tembo_sokogarden_ryxn")

    # create a cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # sql to check if user exist
    sql="select * from users where email=%s and password=%s"

    # prepare data
    data=(email,password)

    # execute data
    cursor.execute(sql,data)

    # response
    # if statements and the responses
    if cursor.rowcount==0:
        return jsonify ({"Message":"Login Failed!"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"Message":"Login Successful!", "User":user})
    
 # add product API
@app.route("/api/add_product", methods=["POST"])
def add_product():
    # request user input 
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_cost=request.form["product_cost"]
    product_photo=request.files["product_photo"]

    # extract image name
    filename=product_photo.filename 
    
    photo_path=os.path.join(app.config["UPLOAD_FOLDER"], filename)
    product_photo.save(photo_path)

    # create connection
    connection=pymysql.connect(host="localhost", user="root", password="", database="tembo_sokogarden_ryxn")


    # create cursor
    cursor=connection.cursor()

    # sql statement to insert the records
    sql="insert into products_details(product_name, product_description, product_cost, product_photo)values(%s,%s,%s,%s)"

    # prepare data
    data=(product_name, product_description, product_cost, filename)

    # Execute
    cursor.execute(sql,data)

    # commit/save
    connection.commit()

    # return a response
    return jsonify ({"Message":"Product added successfully"})

@app.route("/api/get_product")
def get_product():
    connection=pymysql.connect(host="localhost", user="root", password="", database="tembo_sokogarden_ryxn")
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    sql="select * from products_details"
    cursor.execute(sql)
    product=cursor.fetchall()
    return jsonify(product)    



    








































app.run(debug=True)