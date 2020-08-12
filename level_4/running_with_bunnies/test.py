import time

from level_4.running_with_bunnies.solution import solution
from utils.tests import gen_test, time_test


if __name__ == '__main__':
    examples = {
        0: {
            'args': [
                [
                    [0, 2, 2, 2, -1],
                    [9, 0, 2, 2, -1],
                    [9, 3, 0, 2, -1],
                    [9, 3, 2, 0, -1],
                    [9, 3, 2, 2, 0]
                ],
                1
            ],
            'answer': [1, 2]
        },
        1: {
            'args': [
                [
                    [0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0]
                ],
                3
            ],
            'answer': [0, 1]
        },
        2: {
            'args': [
                [
                    [0, 1, 5, 2, 2],
                    [9, 0, 1, 2, -1],
                    [-3, 3, 0, 2, -1],
                    [9, 3, 2, 0, -1],
                    [9, 3, 2, 2, 0]
                ],
                0
            ],
            'answer': [0, 1, 2]
        },
        3: {
            'args': [
                [
                    [0, 2, 2, 2, 2, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1]
                ],
                2
            ],
            'answer': [4]
        },
        4: {
            'args': [
                [
                    [0, 5, 1],
                    [2, 0, 4],
                    [3, 2, 1]
                ],
                7
            ],
            'answer': [0]
        },
        5: {
            'args': [
                [
                    [0, 9, 9],
                    [9, 0, 9],
                    [9, 9, -1]
                ],
                0
            ],
            'answer': [0]
        },
        6: {
            'args': [
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]
                ],
                1
            ],
            'answer': []
        },
        7: {
            'args': [
                [
                    [0, 1],
                    [1, -1]
                ],
                100
            ],
            'answer': []
        },
        8: {
            'args': [
                [
                    [0, 1],
                    [1, 0]
                ],
                100
            ],
            'answer': []
        },
        9: {
            'args': [
                [[]],
                100
            ],
            'answer': []
        }
    }
    gen_test(solution, examples)

    timed_examples = {}
    time_limit = 1
    for i, n_bunnies in enumerate(range(1,6), max(examples)):
        times = [[1 for _ in range(n_bunnies+2)] for _ in range(n_bunnies+2)]
        times[0][n_bunnies+1]
        timed_examples[i] = {'args': [times, time_limit]}
    time_test(solution, timed_examples)
