from flask import Flask, request, render_template
from trivia import get_questions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    questions = get_questions(5)

    for i, q in enumerate(questions):
        q.id = i

    return render_template("quiz.html", questions=questions)

@app.route('/', methods=['POST'])
def post_quiz():
    correct = 0

    for i in range(5):
        if request.form[str(i)] == "True":
            correct += 1
    
    return 'You got ' + str(correct) + ' out of 5 correct!'


@app.route('/greet/<name>')
def greet(name):
    return render_template("greet.html", user_name=name)

if __name__ == '__main__':
    app.run()