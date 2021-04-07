import mysql.connector
from flask import Flask, render_template, request

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

def add_log(username, email, password, currentweight, goalweight, gender):   
    sql = ("INSERT INTO users(username, email, password, current_weight, goal_weight, gender) VALUES (%s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (username,email, password, currentweight, goalweight, gender,))
    db.commit()


@app.route('/submit2', methods=['POST'])
def submit2():
    if request.method == 'POST':
        return render_template('registration.html')

#rows = []
#cursor.execute("SELECT * FROM users")
#result = cursor.fetchall()
#for row in result:
   # rows.append(row[1])


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username= request.form['username']
        email= request.form['email']
        password= request.form['password']
        currentweight= request.form['current_weight']
        goalweight= request.form['goal_weight']
        gender = request.form['gender'] 
        

         
        #print(firstname)
        add_log(username,email, password, currentweight, goalweight, gender)
        return render_template('account2.html')





#cursor.execute("SELECT * FROM users")
#result = cursor.fetchall()
#for row in result:
    #print(row[2])








#def update_log(id, firstname):
    #sql = ("UPDATE users SET last_name = %s WHERE id = %s")
    #cursor.execute(sql, (firstname, id))
    #db.commit()
    #print("Log updated")


#update_log(3, 'Smith')


if(__name__) == '__main__':
    app.debug = True
    app.run()
