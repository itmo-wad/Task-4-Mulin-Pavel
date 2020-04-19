from flask import Flask, send_from_directory, request, flash, redirect, session
from flask import render_template
import autorization



app = Flask(__name__)
app.secret_key = b'eHk\x8d\xd9\x18\xf1\xd9)#\xaaf\x8aK=<'
logins = {'admin': 'admin'}
#session = False

#login_manager = LoginManager()
#login_manager.init_app(app)




@app.route('/', methods = ['GET','POST'])
def login():
	if request.method == "POST":
		if autorization.user_exist(request.form['username'], request.form['password']):
			session['username'] = request.form['username']
			return redirect('mainpage')
		else:
			return render_template('error_login.html')
	elif request.method == "GET":
		if 'username' in session:
			return render_template('main_info.html')
	return render_template('login_page.html')

@app.route('/mainpage')
def mainpage():
	if request.method == "GET":
		if 'username' in session:
			return render_template('main_info.html')
		else:
			return redirect ('/')


@app.route('/showregistered', methods = ['GET','POST'])
def showregistered():
	if request.method == "POST":
		if 'username' in session:
			flash(autorization.showAllUsers())
			return render_template('main_info.html')

@app.route('/register', methods = ['GET','POST'])
def register():
	if request.method == "GET":
		if 'username' in session:
			return render_template('main_info.html')
		else:
			return render_template('register_page.html')
	elif request.method == "POST":
		if autorization.create_user(request.form['username'], request.form['password']):
			return redirect ('mainpage')
		else:
			flash("This username is already in use. Please try another one")
			return render_template('register_page.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect ('/')


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
