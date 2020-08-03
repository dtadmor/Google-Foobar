from level_3.grandest_staircase.solution import solution
from utils.tests import gen_test

if __name__ == '__main__':
    examples = {
        0: {'args': [3], 'answer': 1},
        1: {'args': [4], 'answer': 1},
        2: {'args': [5], 'answer': 2},
        3: {'args': [200], 'answer': 487067745}
    }
    gen_test(solution, examples)
