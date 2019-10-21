from flask import Flask, render_template
from trivia import get_questions

app = Flask(__name__)

@app.route('/')
def index():
    questions = get_questions(5)
    return render_template("quiz.html", questions=questions)


@app.route('/greet/<name>')
def greet(name):
    return render_template("greet.html", user_name=name)

if __name__ == '__main__':
    app.run()