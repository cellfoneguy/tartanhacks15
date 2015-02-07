from flask import Flask, request, redirect, render_template, g
#import alex
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/testing')
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug = True)