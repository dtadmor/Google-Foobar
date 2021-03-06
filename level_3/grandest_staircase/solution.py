def explore(bricks, last_step, solution_map):

    brick_solutions = solution_map.get(bricks)
    if isinstance(brick_solutions, dict):
        n_options = brick_solutions.get(last_step)
        if isinstance(n_options, int):
            return n_options

    max_split = (bricks - 1) // 2
    if last_step >= max_split:
        assert bricks > last_step, 'Not enough bricks left!'
        n_options = 1
        return n_options

    if last_step > 0:
        n_options = 1
    else:
        n_options = 0
    for step in range(last_step+1, max_split+1):
        n_options += explore(
            bricks=bricks-step, last_step=step, solution_map=solution_map
        )

    if not isinstance(solution_map.get(bricks), dict):
        solution_map[bricks] = {}
    solution_map[bricks][last_step] = n_options

    return n_options


def solution(n):

    n_options = explore(bricks=n, last_step=0, solution_map={})

    return n_options
