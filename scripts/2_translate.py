import os
import sys
import json
from typing import List, Tuple

from utils.prompts import TRANSLATE_PROMPT
from utils.config import *
from utils.model import OpenAIWrapper

model = OpenAIWrapper(model_name, api_key, base_url, 2048, 0, 1)

dirname = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(dirname, "..", "data", "statement")
output_dir = os.path.join(dirname, "..", "data", "translation")


def translate(prob: dict) -> Tuple[str, List[str]]:
    print('Translating %s...' % prob['name'])
    message = TRANSLATE_PROMPT % json.dumps(prob)
    for _ in range(5):
        try:
            if _ > 0:
                print('Retrying...')
                response = model.send(message, use_cache=False)
            else:
                response = model.send(message, use_cache=True)
            result = json.loads(response)
            return result['topic'], (result['options'] if 'options' in prob else None)
        except Exception as e:
            print(e)
            continue
    return None, None


for chapter in os.listdir(source_dir):
    for problem in os.listdir(os.path.join(source_dir, chapter)):
        with open(os.path.join(source_dir, chapter, problem), 'r', encoding='utf-8') as f:
            prob = json.load(f)
        trans_filename = os.path.join(output_dir, chapter, problem)
        topic_cn, options_cn = translate(prob)
        prob['topic_cn'] = topic_cn
        if options_cn is not None:
            prob['options_cn'] = options_cn
        if not os.path.exists(os.path.dirname(trans_filename)):
            os.makedirs(os.path.dirname(trans_filename))
        with open(trans_filename, 'w', encoding='utf-8') as f:
            json.dump(prob, f, ensure_ascii=False)
