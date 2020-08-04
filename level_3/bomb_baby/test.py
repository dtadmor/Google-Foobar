from level_3.bomb_baby.solution import solution
from utils.tests import gen_test

if __name__ == '__main__':

    x = 10**10 + 1
    y = 10**10 + 3
    ans = (10**10 / 2) + 2
    examples = {
        0: {'args': ['1', '2'], 'answer': '1'},
        1: {'args': ['4', '7'], 'answer': '4'},
        2: {'args': [str(x), str(y)], 'answer': str(ans)},
        3: {'args': ['51', '96'], 'answer': 'impossible'}
    }
    gen_test(solution, examples)
