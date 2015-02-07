from flask import Flask, request, redirect, render_template, g
import sqlite3
app = Flask(__name__)

email_addresses = []

@app.before_request
def before_request():
	g.db = sqlite3.connect("emails.db")

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
	email = request.form['email']
	g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
	g.db.commit()
	return redirect('/')

@app.route('/emails.html')
def emails():
	email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
	return render_template('emails.html', email_addresses=email_addresses)

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'db'):
		g.db.close()

if __name__ == "__main__":
    app.run(debug = True)