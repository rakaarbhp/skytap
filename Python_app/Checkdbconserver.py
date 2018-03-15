from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

@app.route('/index')

def index_page():
        return render_template('index.html')


@app.route('/showsignup')

def signup_page():
        return render_template('signup.html')


@app.route('/register',methods=["GET","POST"])
def register_page():
    conn = MySQLdb.connect(host="10.0.0.3",
                           user = "root",
                           passwd = "watha",
                           db = "Skytap")
    try:
        c = conn.cursor()
        return("okay")
    except Exception as e:
        return(str(e))



if __name__ == "__main__":
        app.run()
