from flask import Flask, render_template, request, jsonify
import os
import random
from time import sleep
import re 

app = Flask(__name__)

# Load questions from file
def load_questions(file_path):
    questions = []
    
    question = {
                    "question": '',
                    "options": [],
                    "answer": [],
                   
            }
    options = []

    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            
            if re.match(r'^Q\d+\.',line):
                question['question']=line.split('.',1)[1]
                continue

            if re.match(r'Correct Answer',line):

                question['options']=options
                question['answer']=[item for item in line.split(":", 1)[-1].strip().split(',')]
                
                # for field in question:
                #     print(f'Field name {field}: {question[field]}')
                #     print('\n')
                # sleep(5)
                questions.append(question)
                options=[]
                question = {
                    "question": '',
                    "options": [],
                    "answer": [],
                }
                
                continue
            if line =='\n' or line ==' \n':
                continue
            options.append(line)
    return questions

questions = []
print(len(questions))

@app.route('/')
def index():
    random.shuffle(questions)
    return render_template('test_new_quiz.html', questions=questions)

@app.route('/chap/<int:chap_num>')
def render_chapter_question(chap_num):
    print(f'chap{chap_num}.txt')
    global questions
    questions=load_questions(f'chap{chap_num}.txt')
    random.shuffle(questions)
    for question in questions:
        print(f'{question['question']}\nAnswer:{question['answer']}')
    return render_template('test_new_quiz.html', questions=questions)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = int(data['question_index'])
    selected_option = data['selected_options']
    print(selected_option)
    correct_answer = questions[question_index]['answer']
    print(f'Question: {questions[question_index]['question']}')

    # Check if community votes exist
    # has_votes = questions[question_index]['community_votes']

    result = {
        "is_correct": selected_option == correct_answer,
        "correct_answers": correct_answer,
        # "has_votes": has_votes
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)