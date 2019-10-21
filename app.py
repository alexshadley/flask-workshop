from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/greet/<name>')
def greet(name):
    return render_template("greet.html", user_name=name)

if __name__ == '__main__':
    app.run()