from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Paul'}
	return render_template('index.html',
							title='Home',
							user=user)

if __name__ == '__main__':
	app.run()
