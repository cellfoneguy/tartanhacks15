from flask import Flask, request, redirect, render_template, g
import alex
app = Flask(__name__)

@app.route('/')
def hello_world():
	person = alex.alex
	array = person.whoYouOwe().split('\n')
	array2 = person.whoOwesYou().split('\n')
	return render_template('index.html', person = person, array=array, array2=array2)

if __name__ == "__main__":
    app.run(debug = True)