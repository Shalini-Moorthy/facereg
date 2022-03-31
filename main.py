from flask import Flask,render_template,request
import pymysql.cursors
import cv2
import collectsample
import recognizer
import sendMail
import train
UserID=3
connection=pymysql.connect(host="localhost",user="root",port=3306,password="root",db="secureot",cursorclass=pymysql.cursors.DictCursor)
app=Flask(__name__)
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/form_welcome',methods=['post','get'])
def welcome():
    email=request.form['email']
    password=request.form['password']
    with connection.cursor() as cursor:
        sqlQuerys = "select * from userdetails"
        cursor.execute(sqlQuerys)
        result = cursor.fetchall()
        connection.commit()
        print(result)
        emaillist=[]
        for i in result:
            emaillist.append(i['email'])
        print(emaillist)

        if email in emaillist:
            a=emaillist.index(email)
            print(emaillist,a,result[a]['password'],result[a]['email'])
            name=result[a]['name']
            if password==result[a]['password']:

               return render_template("Welcome.html",name=name)
               connection.close()
            else:
                return render_template("login.html",message="Invalid password")
        else:
            return render_template("login.html",message="User doesn't exist")



@app.route('/form_gotosignup',methods=['post','get'])
def signup():
    return render_template("SignUp.html")

@app.route('/form_signupdetails',methods=['post','get'])
def insertDetailsIntoDB():
    name= request.form['username']
    email=request.form['email']
    password=request.form['password']
    try:
        with connection.cursor() as cursor:

            sqlQuery = "insert into userdetails (name,email,password) VALUES (%s,%s,%s)"
            cursor.execute(sqlQuery, ( name,email, password))
            sqlQuerys = "select * from userdetails"
            cursor.execute(sqlQuerys)
            result = cursor.fetchall()
            emaillist = []
            for i in result:
                emaillist.append(i['email'])
            print(emaillist)

            if email in emaillist:
                a = emaillist.index(email)
                UserID = result[a]['id']
                print(UserID)
            connection.commit()
    finally:
        connection.close()

    return render_template("NewUserWelcome.html",name=name)
@app.route('/form_collectsampless',methods=['post','get'])
def collectt():

    collectsample.collect(43)
    train.trainfun(43)
    return render_template("MessageSampleCollected.html")
@app.route('/form_gotowelcomepage',methods=['post','get'])
def backtowelcome():
    return render_template("Welcome.html")
@app.route('/form_recognition',methods=['post','get'])
def recognition():
    confidence=recognizer.recognize(43)
    if confidence>80:
        sendMail.email_alert('shalini1152001@gmail.com','yes')
        return render_template("recognized.html")
    else:
        sendMail.email_alert('shalini1152001@gmail.com','no')
        return render_template("notrecognized.html")

@app.route('/form_recognizeagain',methods=['post','get'])
def tryagain():
    return render_template("welcome.html")
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
