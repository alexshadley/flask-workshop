import random
import requests

API_URL = "https://opentdb.com/api.php"
QUESTION_CATEGORY = 18
QUESTION_TYPE = 'multiple'

class Question:
    def __init__(self, text, correct_answer, wrong_answers):
        self.text = text
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers 
    
    def __repr__(self):
        return f'{self.text}\ncorrect: {self.correct_answer}\n'
    
    def scramble_answers(self):
        answers = [self.correct_answer] + self.wrong_answers
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

