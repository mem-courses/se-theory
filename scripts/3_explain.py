import os
import json

from utils.prompts import EXPLAIN_PROMPT
from utils.model import OpenAIWrapper
from utils.config import *

model = OpenAIWrapper(model_name, api_key, base_url, 2048, 0.7, 1)

dirname = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(dirname, "..", "data", "translation")
output_dir = os.path.join(dirname, "..", "data", "explanation")


for chapter in os.listdir(source_dir):
    for problem in os.listdir(os.path.join(source_dir, chapter)):
        problem = problem.split('.')[0]
        with open(os.path.join(source_dir, chapter, problem + '.json'), 'r', encoding='utf-8') as f:
            prob = json.load(f)

        if prob['type'] == 'TF':
            statement = '(T or F) ' + prob['topic']
        elif prob['type'] == 'MC' or prob['type'] == 'MR':
            statement = prob['topic'] + ' ( )\n'
            for letter, option in zip('ABCD', prob['options']):
                statement += f'\n{letter}. {option}'
        else:
            assert False
        statement += '\n\nThe answer is ' + ', '.join(prob['answer']) + '.'

        print('Explaining problem %s...' % prob['name'])
        print(statement)
        message = EXPLAIN_PROMPT % statement
        explanation = model.send(message).strip().replace('\n', '')

        exp_filename = os.path.join(output_dir, chapter, problem + '.md')
        if not os.path.exists(os.path.dirname(exp_filename)):
            os.makedirs(os.path.dirname(exp_filename))
        with open(exp_filename, 'w', encoding='utf-8') as f:
            f.write(explanation)
