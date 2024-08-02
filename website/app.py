from flask import Flask, request, render_template,Response,redirect,url_for
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user ="root",passwd="root",database="students")
cursor=mycon.cursor()
app=Flask(__name__)

@app.route('/') # the data is hide in url bar
def signup():
	return render_template('signup.html')

response={'success':False,'msg' : 'Login again!'}

@app.route('/saveData',methods=['POST','GET'])
def saveData():
	if request.method=="POST":
		uName=request.form['name']
		gender=request.form['Gender']
		CourseSelect=request.form['option']
		Email=request.form['email']
		uPaswd=request.form['password']

		try:
			sql_insert = "INSERT INTO stu1 (name, gender, course, email, password) VALUES (%s, %s, %s, %s, %s)"
			val_insert = (uName, gender, CourseSelect, Email, uPaswd)
			cursor.execute(sql_insert,val_insert)
			mycon.commit()
			response={'success':True,'msg':"Signup successfully!"}
		except Exception as e:
			mycon.rollback();
			response={'success':False,'msg' : 'Signup again!'}
			print(e)
	return render_template('login.html',response=response)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        uEmail = request.form['email']
        uPaswd = request.form['password']
        mycon=mysql.connector.connect(host="localhost",user ="root",passwd="root",database="students")
        cursor=mycon.cursor()
        sql_fetch = "SELECT * FROM stu1 WHERE email=%s AND password=%s"
        cursor.execute(sql_fetch, (uEmail, uPaswd))
        user = cursor.fetchone()

        if user:
        	response={'success':True,'msg' : 'Login successfully!'}
        	return redirect(url_for('websiteThemeSwitcher',response=response))
        else:
        	response={'success':False,'msg' : 'Login again!'}
        	return render_template('login.html',response=response)
    response={'success':False,'msg' : ''}
    return render_template('login.html',response=response)

@app.route('/websiteThemeSwitcher')
def websiteThemeSwitcher():
	response={'success':True,'msg' : 'Login successfully!'}
	return render_template('websiteThemeSwitcher.html',response=response)
if __name__=="__main__":
	app.run(debug=True)
mycon.close()