from level_5.disorderly_escape.solution import solution
from utils.tests import gen_test, time_test


if __name__ == '__main__':
    examples = {
        0: {
            'args': [2, 2, 2],
            'answer': '7'
        },
        1: {
            'args': [2, 3, 4],
            'answer': '430'
        },
        2: {
            'args': [1, 1, 1],
            'answer': '1'
        },
        3: {
            'args': [1, 1, 20],
            'answer': '20'
        },
        4: {
            'args': [12, 12, 1],
            'answer': '1'
        },
        5: {
            'args': [4, 1, 2],
            'answer': '5'
        },
        6: {
            'args': [2, 3, 2],
            'answer': '13'
        },
        7: {
            'args': [4, 2, 2],
            'answer': '22'
        },
        8: {
            'args': [3, 4, 2],
            'answer': '87'
        },
        9: {
            'args': [4, 4, 2],
            'answer': '317'
        },
        10: {
            'args': [1, 3, 3],
            'answer': '10'
        },
        11: {
            'args': [2, 2, 3],
            'answer': '27'
        },
        12: {
            'args': [3, 2, 3],
            'answer': '92'
        },
        13: {
            'args': [2, 4, 3],
            'answer': '267'
        },
        14: {
            'args': [3, 3, 3],
            'answer': '738'
        },
        15: {
            'args': [5, 2, 3],
            'answer': '678'
        },
        16: {
            'args': [2, 5, 2],
            'answer': '34'
        },
        17: {
            'args': [3, 3, 2],
            'answer': '36'
        }
    }
    gen_test(solution, examples)

    timed_examples = {
        18: {'args': [12, 12, 20]},
        19: {'args': [11, 12, 20]}
    }
    time_test(solution, timed_examples)
