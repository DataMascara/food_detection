import mysql.connector
from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



config = {

     'user': 'root',
     'password': 'sergiocas',
     'host': 'localhost',
     'database': 'project'

}

db = mysql.connector.connect(**config)
cursor = db.cursor()





def add_log(username, email, password, currentweight, goalweight, gender, dateofbirth):   
    sql = ("INSERT INTO users(username, email, password, current_weight, goal_weight, gender, dateofbirth) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (username,email, password, currentweight, goalweight, gender, dateofbirth,))
    db.commit()


def add_diary(username, food, serving, calories, date):   
    sql = ("INSERT INTO diary(username, food, serving, calories, date) VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(sql, (username,food, serving, calories, date,))
    db.commit()





@app.route('/submit2', methods=['POST'])
def submit2():
    if request.method == 'POST':
        return render_template('registration.html')




@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username= request.form['username']
        email= request.form['email']
        password= request.form['password']
        currentweight= request.form['current_weight']
        goalweight= request.form['goal_weight']
        gender = request.form['gender'] 
        dateofbirth = request.form['month'] + " " + request.form['day'] + " " + request.form['year']
        submit.username =username
        result = submit.username
        sql = """SELECT food FROM diary WHERE username = '%s'""" % (submit.username)
        cursor.execute(sql)
        food = cursor.fetchall()
        sql = """SELECT calories FROM diary WHERE username = '%s'""" % (submit.username)
        cursor.execute(sql)
        calories = cursor.fetchall()
        name =[]
        name =calories

        add_log(username,email, password, currentweight, goalweight, gender, dateofbirth)
        return render_template('account2.html', result= result , food =food, calories =name, l1=len(food), l2=len(calories))


@app.route('/submit3', methods=['POST'])
def submit3():
    if request.method == 'POST':
        cursor.execute("SELECT * FROM users")
        #result = cursor.fetchall()

        return render_template('index.html', result=submit.username, flash="True")



@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        return render_template('index.html')





@app.route('/UserInfo/<string:a>/<string:b>', methods=['POST'])
def processUserInfo(a,b):
 
   username = submit.username
   food = json.loads(a)
   calories= json.loads(b)
   serving = "1 serving"
   date= datetime.now()

   add_diary(username,food, serving, calories, date)
   return 'Info recieved successfully'


@app.route('/submit4', methods=['POST'])
def submit4():
    if request.method == 'POST':
        username= request.form['username']
        #password= request.form['password']
        submit.username =username
        result = submit.username
        cursor.execute("SELECT username FROM diary;")
        user = cursor.fetchall()
      
        found ="false"
        for x in user:
                 if x[0] == submit.username:
                     found = "true"
                
                      

        sql = """SELECT food FROM diary WHERE username = '%s'""" % (submit.username)
        cursor.execute(sql)
        food = cursor.fetchall()
        sql = """SELECT calories FROM diary WHERE username = '%s'""" % (submit.username)
        cursor.execute(sql)
        calories = cursor.fetchall()
        name =[]
        name =calories

        if found == "true":
            return render_template('account2.html', result= result , food =food, calories =name, l1=len(food), l2=len(calories), found=found)
        else:
            return render_template('index.html', found=found)

        
    
    
        

   
        

        














if(__name__) == '__main__':
    app.debug = True
    app.run()
