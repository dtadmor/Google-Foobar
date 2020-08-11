import time


def gen_test(func, examples):

    for i, case in examples.items():

        output = func(*case['args'])
        success = case['answer'] == output

        msg = 'Case {}; Arguments {}; Success {}'.format(
            i, case['args'], success
        )
        if not success:
            msg += '; Output {}; Answer {}'.format(output, case['answer'])

        print(msg)


def time_test(func, examples, precision=5):

    for i, case in examples.items():

        start = time.time()
        _ = func(*case['args'])
        end = time.time()
        run_time = round(end-start, precision)

        msg = 'Case {}; Arguments {}; Time {}'.format(i, case['args'], run_time)
        print(msg)


def rules_test(func, rules_func, examples):

    for i, case in examples.items():

        output = func(*case['args'])
        result = rules_func(output, *case['args'])
        msg = 'Case {}; Arguments {}; Result {}'.format(i, case['args'], result)
        print(msg)
