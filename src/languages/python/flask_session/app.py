from flask import Flask, render_template, request, redirect, url_for, jsonify, flash,session
from markupsafe import escape

app = Flask(__name__)

app.secret_key = 'your-secret-key'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])	
def login():
	if request.method == 'POST':
		user_name = request.form['name']
		session['user_name'] = user_name
		return redirect(url_for('user'))

	else:
		if 'user_name' in session:
			return redirect(url_for('user'))
		return render_template('login.html')


@app.route('/user')
def user():
	if 'user_name' in session:
		user_name = session['user_name']
		return f"<h1>{ user_name }</h1>"
	else:
		return redirect(url_for('index'))

@app.route('/logout')
def logout():
	session.pop('user_name', None)
	return redirect(url_for('index'))		


if __name__ == "__name__":
	app.run(debug=True)		


