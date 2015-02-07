from __future__ import with_statement # for Python 2.5 and 2.6
from flask import Flask, request, redirect, render_template, g
import sqlite3, os
app = Flask(__name__)

email_addresses = []

def saveMap(contents): #actual saver function
	path = "saved.txt"
	if os.path.exists(path):
		os.remove(path)
	savedMap = open("saved.txt","wt")
	savedMap.write(contents)

def loadmap():
	path = "saved.txt"
	savedMap = open(path, "r")
	contents = savedMap.read()
	return contents

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
	email = request.form['email']
	#email_addresses.append(email)
	#print(email_addresses)
	past = loadmap()
	saveMap(past + '\n' + email)
	return redirect('/')

@app.route('/emails.html')
def emails():
	email_addresses = loadmap().split('\n')
	return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run(debug = True)