import hashlib
import json
import os
import re
import time
from pathlib import Path

from flask import Flask, render_template, request, jsonify, send_file
from openai import OpenAI

from pddlgym.demo_planning import demo_planning

PDDL_PROBLEM_PATH = 'pddlgym/pddl/sokoban/task02.pddl'
PDDL_DOMAIN_PATH = 'pddlgym/pddl/sokoban.pddl'

app = Flask(__name__)
client = OpenAI()

# OpenAI API Key
# openai.api_key = 'YOUR_API_KEY'


def add_context(prompt):
    domain_pddl = open(PDDL_DOMAIN_PATH, 'r').read()
    problem_pddl = open(PDDL_PROBLEM_PATH, 'r').read()
    return f'''Given the PDDL domain:
    {domain_pddl}
    
    And the PDDL problem
    {problem_pddl}
    
    The user asks: {prompt}'''


def get_completion(prompt):
    print(prompt)
    prompt_with_context = add_context(prompt)
    response = query_openai(prompt_with_context)
    save_if_code(response)

    return response


def query_openai(prompt_with_context):
    hash = hashlib.md5(prompt_with_context.encode('utf-8')).hexdigest()
    CACHE_PATH = './cache/openai_response_cache/'
    answer_cache_path = CACHE_PATH + hash + '.txt'
    if os.path.exists(answer_cache_path):
        time.sleep(2)
        return open(answer_cache_path).read()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "You are a PDDL generator that edit either PDDL domain or PDDL problem based on the user ask. User will copy-paste your answers, so they have to be full."},
            {"role": "user", "content": prompt_with_context},
            # {"role": "assistant", "content": "<history here"}
        ]
    )
    response = completion.choices[0].message.content
    Path(CACHE_PATH).mkdir(parents=True, exist_ok=True)
    open(answer_cache_path, 'w').write(response)
    return response


def save_if_code(response):
    codes = []
    code_re_result = re.findall('```.*?\n(.+?)```', response, re.DOTALL)
    if code_re_result:
        codes = code_re_result
    elif 'define ( ' in response:
        codes = [response]
    for code in codes:
        if 'define (domain ' in code:
            print(f'Writing domain to {PDDL_DOMAIN_PATH}')
            open(PDDL_DOMAIN_PATH, 'w').write(code)
        elif 'define (problem ' in code:
            print(f'Writing problem to {PDDL_PROBLEM_PATH}')
            open(PDDL_PROBLEM_PATH, 'w').write(code)
        else:
            print(code)
            raise ValueError('Unexpected code')

        # demo_planning("sokoban", render=True, verbose=True)


@app.route("/", methods=['POST', 'GET'])
def query_view():
    if request.method == 'POST':
        print('step1')
        prompt = request.form['prompt']
        response = get_completion(prompt)
        print(response)

        return jsonify({'response': response})
    demo_planning("sokoban", render=True, verbose=True, max_num_steps=0)
    return render_template('index.html')

@app.route("/simulation", methods=['GET'])
def get_simulation_image():
    return send_file('simulation.png', mimetype='image/jpg')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
