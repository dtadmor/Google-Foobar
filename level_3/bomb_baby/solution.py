def solution(x, y):

    generations = 0
    x = int(x)
    y = int(y)
    remainder = 1

    while remainder != 0:
        min_xy, max_xy = sorted((x, y))
        extra_gen = max_xy // min_xy
        remainder = max_xy % min_xy
        x = remainder
        y = min_xy
        generations += extra_gen

    if min_xy == 1:
        generations -= 1
        generations = str(generations)
    else:
        generations = 'impossible'
        
    return generations
