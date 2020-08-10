from level_3.prepare_the_bunnies_escape.solution import solution
from utils.tests import gen_test


if __name__ == '__main__':
    examples = {
        0: {
            'args': [
                [
                    [0, 1, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 0, 0],
                    [1, 1, 1, 0]
                ]
            ],
            'answer': 7
        },
        1: {
            'args': [
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]
                ]
            ],
            'answer': 11
        }
    }
    gen_test(solution, examples)
