import os
import json


def process_problem(prob):
    choices = len(prob['options'])
    prob['id'] = '%02d' % int(prob['topic'].split('. ')[0])
    prob['name'] = f'{prob["chapter"]}_{prob["id"]}'
    if choices == 2:
        prob['type'] = 'TF'
        del prob['options']
        if prob['answer'] == 'A':
            prob['answer'] = ['T']
        else:
            prob['answer'] = ['F']
    elif choices == 4:
        prob['type'] = 'MC'
        prob['answer'] = [prob['answer']]
        prob['options'] = list(map(lambda x: x[3:], prob['options']))
    elif choices == 5:
        prob['type'] = 'MR'
        option_e = prob['options'][4][3:]
        prob['options'] = prob['options'][:4]
        if len(option_e.split(' and ')) == 2:
            prob['answer'] = list(map(lambda x: x.upper(), option_e.split(' and ')))
        elif len(option_e.split(', ')) == 3:
            prob['answer'] = list(map(lambda x: x.upper(), option_e.split(', ')))
        elif option_e.lower().startswith('all of the above'):
            prob['answer'] = ['A', 'B', 'C', 'D']
        elif option_e == 'a, c d':  # special case
            prob['answer'] = ['A', 'C', 'D']
        else:
            print(option_e)
            assert False
        prob['options'] = list(map(lambda x: x[3:], prob['options']))
    else:
        assert False
    return prob


dirname = os.path.abspath(os.path.dirname(__file__))


problemset_file = os.path.join(dirname, "..", "data", "problemset.json")

with open(problemset_file, "r") as f:
    problemset = json.load(f)

problems = []
for chap, prob_list in problemset.items():
    for prob in prob_list:
        problems.append(process_problem(
            {
                "chapter": '%02d' % int(chap),
                **prob
            }
        ))

output_dir = os.path.join(dirname, "..", "data", "problem")
for prob in problems:
    filename = os.path.join(output_dir, prob['chapter'], prob['name'] + '.json')
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'w') as f:
        json.dump(prob, f)
