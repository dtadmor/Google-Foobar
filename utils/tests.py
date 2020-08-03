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
