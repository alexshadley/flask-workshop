from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/greet/<name>')
def greet(name):
    return '<h1>Welcome to the greeter.</h1><p>Consider yourself greeted, ' + name + '</p>'

if __name__ == '__main__':
    app.run()