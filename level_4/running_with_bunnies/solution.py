import itertools

def search(start, end, path, gps, times, orig_start):

    min_time = gps[start][end]
    if min_time is None:
        if start != end:
            path = path[:] + [start]

        min_time = times[start][end]
        for loc in range(len(times)):
            if loc not in path:
                if loc != end:
                    time_to_end, gps = search(
                        start=loc,
                        end=end,
                        path=path,
                        gps=gps,
                        times=times,
                        orig_start=orig_start
                    )
                else:
                    time_to_end = min(0, times[loc][end])
                time = times[start][loc] + time_to_end
                min_time = min(time, min_time)

        if start == orig_start:
            gps[start][end] = min_time

    return min_time, gps


def has_inf_time_loop(times):

    min_time = min(min(times, key=lambda x: min(x)))
    has_negatives = min_time < 0
    inf_time_loop = False
    gps = [[None for _ in times[0]] for _ in times]

    if has_negatives:
        path_exclude = []
        for start in range(len(times)):
            if min(times[start]) < 0:
                time, gps = search(
                    start=start,
                    end=start,
                    path=path_exclude,
                    gps=gps,
                    times=times,
                    orig_start=start
                )
                inf_time_loop = time < 0
                if inf_time_loop:
                    break
                path_exclude.append(start)

    return inf_time_loop, gps


def find_bunnies(n_buns, time_limit, gps, times):

    max_bunny = len(times) - 2
    bunny_paths = itertools.permutations(range(1, max_bunny+1), n_buns)
    bunny_paths = sorted(bunny_paths, key=lambda x: sorted(x))

    for bunnies in bunny_paths:
        time = 0
        i = 0
        loc = 0
        while i != len(bunnies):
            bunny = bunnies[i]
            new_time, gps = search(
                start=loc,
                end=bunny,
                path=[],
                gps=gps,
                times=times,
                orig_start=loc
            )
            time += new_time
            i += 1
            loc = bunny
        end = len(times) - 1
        new_time, gps = search(
            start=bunny,
            end=end,
            path=[],
            gps=gps,
            times=times,
            orig_start=bunny
        )
        time += new_time

        if time <= time_limit:
            rescued_bunnies = sorted(bunnies)
            rescued_bunnies = [b-1 for b in rescued_bunnies]
            break
    else:
        rescued_bunnies = []

    return rescued_bunnies, gps


def solution(times, time_limit):

    max_buns = len(times) - 2
    if max_buns < 1:
        bunnies = []
    else:
        inf_time_loop, gps = has_inf_time_loop(times)
        if inf_time_loop:
            bunnies = list(range(max_buns))
        else:
            for n_buns in range(max_buns, 0, -1):
                bunnies, gps = find_bunnies(n_buns, time_limit, gps, times)
                if len(bunnies) == n_buns:
                    break

    return bunnies
