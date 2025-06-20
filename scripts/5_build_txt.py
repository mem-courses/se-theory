import os
import json

VERSION = 3.0

TEMPLATE_HEADER = f'''
#import "../docs/template.typ": *
#show: project.with(
  title: link(
    "https://mem.ac",
    [*客观题题库* (v{VERSION})],
  ),
  header-content: "软件工程 / 客观题题库 (v{VERSION}) / mem 整理版",
)

#hint
'''

dirname = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(dirname, "..", "data", "translation")
explaination_dir = os.path.join(dirname, "..", "data", "explanation")
output_dir = os.path.join(dirname, "..", "build")


def parse_statement(statement, options, answer=[], index=None):
    statement = statement.replace('"', '\\"')
    if index is not None:
        statement += f' #{index}'
    if len(answer) == 0:
        result = '(  ) ' + statement
    else:
        result = f'({"".join(answer)}) ' + statement
    if options is not None:
        result += '\n'
        for char, option in zip('ABCD', options):
            if char in answer:
                result += f'- {char}. {option}\n'
            else:
                result += f'- {char}. {option}\n'
    return result + '\n\n'


def parse_explaination(explaination):
    return explaination + '\n\n'


tasks = [
    {
        'fields': ['en', 'expl_ans'],
    },
    {
        'fields': ['en'],
    }
]
for task in tasks:
    task['name'] = f'软工题库mem整理版_v{VERSION}_{'+'.join(task["fields"])}'
    task['data'] = []

index = 0
for chapter in os.listdir(source_dir):
    for problem in os.listdir(os.path.join(source_dir, chapter)):
        problem = problem.split('.')[0]
        with open(os.path.join(source_dir, chapter, problem + '.json'), 'r', encoding='utf-8') as f:
            prob = json.load(f)
        print('Processing %s...' % problem)

        index += 1
        prefix = f'{int(prob["chapter"])}-'

        if prob['type'] == 'TF':
            en = parse_statement(prefix + prob['topic'], None, index=index)
            cn = parse_statement(prefix + prob['topic_cn'], None, index=index)
            en_ans = parse_statement(prefix + prob['topic'], None, prob['answer'])
            cn_ans = parse_statement(prefix + prob['topic_cn'], None, prob['answer'])
        else:
            en = parse_statement(prefix + prob['topic'], prob['options'], index=index)
            cn = parse_statement(prefix + prob['topic_cn'], prob['options_cn'], index=index)
            en_ans = parse_statement(prefix + prob['topic'], prob['options'], prob['answer'])
            cn_ans = parse_statement(prefix + prob['topic_cn'], prob['options_cn'], prob['answer'])
            # print(en_ans)

        with open(os.path.join(explaination_dir, chapter, problem + '.md'), 'r', encoding='utf-8') as f:
            explaination = f.read()
        expl = parse_explaination(explaination)
        expl_ans = parse_explaination(explaination + '\n\n' + cn_ans)

        for task in tasks:
            for field in task['fields']:
                task['data'].append(eval(f'{field}'))
        task['data'].append('\n')

for task in tasks:
    filename = os.path.join(output_dir, f'{task["name"]}.txt')
    with open(filename, 'w', encoding='utf-8') as f:
        content = '\n\n'.join(task['data'])
        for _ in range(10):
            content = content.replace('\n\n\n', '\n\n')
        f.write(content)
