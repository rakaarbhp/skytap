from flask import Flask, render_template
from Workingdbcopy import connection

app = Flask(__name__)

@app.route('/index')

def index_page():
        return render_template('index.html')


@app.route('/showsignup')

def signup_page():
        return render_template('signup.html')

@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        c, conn = connection()
        return("okay")
    except Exception as e:
        return(str(e))
		


if __name__ == "__main__":
        app.run()
