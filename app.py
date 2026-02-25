from flask import *
import pymysql

# initialize flask

app=Flask(__name__)

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



    








































app.run(debug=True)