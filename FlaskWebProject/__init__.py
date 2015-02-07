from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	author = "Pu (Paul) Liang"
	name = "piece of shit"
    return render_template('/template/index.html', author=author, name=name)

if __name__ == '__main__':
    app.run()