import math
import time

from level_4.free_the_bunny_prisoners.solution import solution
from utils.tests import gen_test, rules_test, time_test


def rules_func(answer, num_buns, num_required):

    if num_required > num_buns:
        return ''

    num_missing = num_required - 1
    num_copies = num_buns - num_missing
    if num_required > 0:
        uniq_keys = math.factorial(num_buns)/(
            math.factorial(num_copies) * math.factorial(num_missing)
        )
    else:
        uniq_keys = 0
    keys_per_bunny = num_copies * uniq_keys / num_buns

    keys = []
    failures = []
    for bunny_keys in answer:
        if len(bunny_keys) != keys_per_bunny:
            failures.append('keys per bunny')
        if bunny_keys != sorted(bunny_keys):
            failures.append('bunny key sorted')
        keys.extend(bunny_keys)
    if len(set(keys)) != uniq_keys:
        failures.append('num uniq keys')
    if answer != sorted(answer):
        failures.append('bunnies sorted')
    for i in range(num_buns-num_required):
        sample = answer[i]
        for j in range(i+1, i+num_required):
            sample.extend(answer[j])
        if set(sample) != set(range(uniq_keys)):
            failures.append('actual answer')

    if len(failures) > 0:
        failures = set(failures)
        result = 'Failure (' + ' ,'.join(failures) + ')'
    else:
        result = 'Success'

    return result


if __name__ == '__main__':
    examples = {
        0: {
            'args': [2, 1],
            'answer': [[0], [0]]
        },
        1: {
            'args': [4, 4],
            'answer': [[0], [1], [2], [3]]
        },
        2: {
            'args': [5, 3],
            'answer': [
                [0, 1, 2, 3, 4, 5],
                [0, 1, 2, 6, 7, 8],
                [0, 3, 4, 6, 7, 9],
                [1, 3, 5, 6, 8, 9],
                [2, 4, 5, 7, 8, 9]
            ]
        },
        3: {
            'args': [3, 2],
            'answer': [[0, 1], [0, 2], [1, 2]]
        },
        4: {
            'args': [5, 0],
            'answer': [[] for _ in range(5)]
        },
    }
    gen_test(solution, examples)

    timed_examples = {}
    for num_buns in range(10):
        for i, num_required in enumerate(range(1,10), max(examples)):
            timed_examples[i] = {'args': [num_buns, num_required]}
    time_test(solution, timed_examples)

    i = len(timed_examples)
    rules_examples = {k+i:v for k,v in timed_examples.items()}
    rules_test(solution, rules_func, rules_examples)
