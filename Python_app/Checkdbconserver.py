from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/index')

def index_page():
        return render_template('index.html')


@app.route('/showsignup')

def signup_page():
        return render_template('signup.html')


@app.route('/register',methods=["GET","POST"])
def register_page():

    app.config['MYSQL_HOST'] = '10.0.0.3'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'watha'
    app.config['MYSQL_DB'] = 'Skytap'
    mysql = MySQL(app)

#    conn = (host = "10.0.0.3",
#            user = "root",
#            passwd = "watha",
#            db = "Skytap")
    print('connected')
    try:
        c = conn.cursor()
        return("okay")
    except Exception as e:
        return(str(e))



if __name__ == "__main__":
        app.run()
