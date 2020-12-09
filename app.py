from flask import Flask, render_template, request
from surveys import Question, Survey, satisfaction_survey

app = Flask(__name__)
# app.config['TESTING'] = True
responses = []
survey = satisfaction_survey

@app.route('/')
def fetch_root():
    return render_template('root.html', instructions=survey.instructions )

@app.route('/questions/<num>')
def get_question(num):
    # num = request.args['num']
    question = satisfaction_survey.questions[int(num)]
    return render_template('questions.html')


