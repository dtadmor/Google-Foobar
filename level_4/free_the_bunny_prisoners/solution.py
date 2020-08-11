def map_bunnies_to_keys(
    key, bunnies, min_bun, max_bun, loop, num_loops, key_dist
):

    for bunny in range(min_bun, max_bun):
        bunnies = bunnies + [bunny]
        if loop != num_loops:
            key_map, key = map_bunnies_to_keys(
                key=key,
                bunnies=bunnies,
                min_bun=bunny+1,
                max_bun=max_bun+1,
                loop=loop+1,
                num_loops=num_loops,
                key_dist=key_dist
            )
        else:
            for bunny in bunnies:
                key_dist[bunny].append(key)
        key += 1
        bunnies = bunnies[:-1]
    key -= 1

    return key_dist, key


def solution(num_buns, num_required):

    num_missing = num_required - 1
    num_copies = num_buns - num_missing
    key_dist = [[] for _ in range(num_buns)]

    if num_required > num_buns:
        return key_dist

    key_dist, _ = map_bunnies_to_keys(
        key=0,
        bunnies=[],
        min_bun=0,
        max_bun=num_required,
        loop=1,
        num_loops=num_copies,
        key_dist=key_dist
    )

    return key_dist
