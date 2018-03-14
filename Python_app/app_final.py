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
    if request.method == 'POST':
        conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "watha",
                           db = "Skytap")
        c = conn.cursor()
        FIRSTNAME = request.form['inputFirstName']
        LASTNAME = request.form['inputLastName']
        EMAIL = request.form['inputEmail']
        USERNAME = request.form['inputUsername']
        PASSWORD = request.form['inputPassword']
        sql = """INSERT INTO skytap_userinfo(FirstName,LastName,Emailaddress,UserName,Password) VALUES(%s,%s,%s,%s,%s)"""
        c.execute(sql,(FIRSTNAME,LASTNAME,EMAIL,USERNAME,PASSWORD))
        conn.commit()
        print('success')
        return render_template('signup.html')
#   try:
#        c, conn = connection()
#        return("okay")
#    except Exception as e:
#        return(str(e))


if __name__ == "__main__":
        app.run(debug=True)
