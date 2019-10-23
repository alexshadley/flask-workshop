import random
import requests

API_URL = "https://opentdb.com/api.php"
QUESTION_CATEGORY = 18
QUESTION_TYPE = 'multiple'

class Answer:
    def __init__(self, text, correct):
        self.text = text
        self.correct = correct

class Question:
    def __init__(self, text, correct_answer, wrong_answers):
        self.text = text
        self.answers = [Answer(a, False) for a in wrong_answers]
        self.answers.append(Answer(correct_answer, True))
    
    def __repr__(self):
        return f'{self.text}\n'
    
    def scramble_answers(self):
        answers = list(self.answers)
        random.shuffle(answers)
        return answers

def get_questions(amount, difficulty=None):
    url_params = {
        'amount': amount,
        'category': QUESTION_CATEGORY,
        'type': QUESTION_TYPE,
    }
    if difficulty:
        url_params['difficulty'] = difficulty

    response = requests.get(API_URL, params=url_params)

    questions = []
    for r in response.json()['results']:
        new_question = Question(
            r['question'],
            r['correct_answer'],
            r['incorrect_answers']
        )
        questions.append(new_question)
    
    return questions

