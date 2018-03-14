import MySQLdb

conn = MySQLdb.connect(host="localhost",
                   user = "root",
                   passwd = "watha",
                   db = "Skytap")
c = conn.cursor()
FIRSTNAME = 's'
LASTNAME = FIRSTNAME = 's'
EMAIL = 'A@a.com'
USERNAME = 'aasdfasdfs'
PASSWORD = 'ASA'
sql = """INSERT INTO skytap_userinfo(FirstName,LastName,Emailaddress,UserName,Password) VALUES(%s,%s,%s,%s,%s)"""
c.execute(sql,(FIRSTNAME,LASTNAME,EMAIL,USERNAME,PASSWORD))
conn.commit()
print('success')
