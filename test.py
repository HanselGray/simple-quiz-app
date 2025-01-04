import os
import random
import re
from time import sleep
# def load_questions(file_path):
#     questions = []
    
#     question = {
#                     "question": '',
#                     "options": [],
#                     "answer": [],
                   
#             }
#     options = []

#     with open(file_path, 'r', encoding='utf-8') as f:
#         data = f.readlines()
#         for line in data:
            
#             if re.match(r'^\d+\.',line):
#                 question['question']=line
#                 continue

#             if re.match(r'Correct Answer',line):

#                 question['options']=options
#                 question['answer']=[item for item in line.split(":", 1)[-1].strip().split(',')]
                
#                 # for field in question:
#                 #     print(f'Field name {field}: {question[field]}')
#                 #     print('\n')
#                 # sleep(5)
#                 questions.append(question)
#                 options=[]
#                 question = {
#                     "question": '',
#                     "options": [],
#                     "answer": [],
#                 }
                
#                 continue
#             if line =='\n' or line ==' \n':
#                 continue
#             options.append(line)
#     return questions
            
            

# questions=load_questions('chap1.txt')
# print(len(questions))

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(sep=",",maxsplit=1)

print(x)

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)
