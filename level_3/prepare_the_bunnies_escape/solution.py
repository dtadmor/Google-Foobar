def update_dist_map(dist_map, loc, walls, steps):
    dist_map[walls][str(loc)] = steps
    return dist_map


def at_end(loc, end):
    if loc == end:
        return True
    else:
        return False


def should_continue(loc, steps, walls, dist_map):
    shortest_dist = dist_map[walls].get(str(loc))
    if (shortest_dist is None) or (steps < shortest_dist):
        dist_map = update_dist_map(dist_map, loc, walls, steps)
        return True, dist_map
    else:
        return False, dist_map


def should_be_done(steps, best_path):
    if steps >= best_path:
        return True
    else:
        return False


def get_map_limits(map):
    max_y = len(map) - 1
    max_x = len(map[0]) - 1
    end = [max_x, max_y]
    min_best = max_x + max_y - 1
    max_best = max_x * max_y
    return end, min_best, max_best


def move(loc, walls, d_x, d_y, end, map):
    x = loc[0] + d_x
    y = loc[1] + d_y
    loc = [x, y]
    on = on_map(loc, end)
    if on:
        walls += map[y][x]
        legal = few_walls(walls)
    else:
        legal = False
    return loc, walls, legal


def few_walls(walls):
    if walls <= 1:
        few = True
    else:
        few = False
    return few


def on_map(loc, end):
    if loc[0] > end[0] or loc[0] < 0:
        on = False
    elif loc[1] > end[1] or loc[1] < 0:
        on = False
    else:
        on = True
    return on


def explore(loc, steps, walls, end, dist_map, map):

    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    steps += 1
    if should_be_done(steps, dist_map['max_best']):
        return dist_map

    for (d_x, d_y) in deltas:
        new_loc, new_walls, legal = move(loc, walls, d_x, d_y, end, map)
        if legal:
            if at_end(new_loc, end):
                dist_map = update_dist_map(dist_map, new_loc, new_walls, steps)
                if steps == dist_map['min_best']:
                    dist_map['max_best'] = dist_map['min_best']
                elif steps < dist_map['max_best']:
                    dist_map['max_best'] = steps
                return dist_map
            cont, dist_map = should_continue(new_loc, steps, new_walls, dist_map)
            if cont:
                dist_map = explore(new_loc, steps, new_walls, end, dist_map, map)

    return dist_map

def solution(map):

    end, min_best, max_best = get_map_limits(map)
    dist_map = {0:{}, 1:{}, 'min_best': min_best, 'max_best': max_best}
    loc = [0, 0]
    steps = 1
    walls = 0
    dist_map = update_dist_map(dist_map, loc, walls, steps)
    explore(loc, steps, walls, end, dist_map, map)
    dist = dist_map['max_best']

    return dist
