from flask import Flask, render_template, request
# import MySQLdb  #Confirm you get an error

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
#import MySQLdb

app = Flask(__name__)

@app.route('/index')

def index_page():
        return render_template('index.html')


@app.route('/showsignup')

def signup_page():
        return render_template('signup.html')


@app.route('/register')

class Database:

    host = '10.0.0.2'
    user = 'admin'
    password = 'Watha12!'
    db = 'Skytap'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

#def register_page():
 #   conn = MySQLdb.connect(host="10.0.0.2",
 #                          user = "watha",
 #                          passwd = "Watha12!",
 #                          db = "Skytap",
 #                          port = "3306")
    print ("success")
#    try:
#        c = conn.cursor()
#        return("okay")
#    except Exception as e:
#       return(str(e))



if __name__ == "__main__":
        app.run()
