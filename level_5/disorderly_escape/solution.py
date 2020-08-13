import math


def find_unique_pos_sums(n, this_sum=None, all_sums=None):

    if n == 0:
        sum_dict = {addend: this_sum.count(addend) for addend in set(this_sum)}
        if all_sums is None:
            all_sums = []
        all_sums.append(sum_dict)
        return all_sums

    second_largest_addend = n // 2
    if this_sum is None:
        min_addend = 1
        this_sum = []
    else:
        min_addend = this_sum[-1]
    possible_addends = list(range(min_addend, second_largest_addend+1)) + [n]

    for next_addend in possible_addends:
        next_sum = this_sum[:] + [next_addend]
        next_n = n - next_addend
        all_sums = find_unique_pos_sums(next_n, next_sum, all_sums)

    return all_sums


def permutations_of_cycle_combinations(cycle_combinations, n_elements):

    n_permutations = math.factorial(n_elements)
    cycle_permutations = []

    for combination in cycle_combinations:
        inter_cycle_permutations = 1
        intra_cycle_permutations = 1
        for cycle_len, n_cycles in combination.items():
            inter_cycle_permutations *= math.factorial(n_cycles)
            intra_cycle_permutations *= cycle_len ** n_cycles
        n_combination_permutations = n_permutations / (
            inter_cycle_permutations * intra_cycle_permutations
        )
        cycle_permutations.append([n_combination_permutations, combination])

    return cycle_permutations


def gcd(x, y):

    z = [x, y]
    r = 1
    while r != 0:
        x = min(z)
        y = max(z)
        r = y % x
        z = [r, x]

    return x


def solution(w, h, s):

    row_cycle_combinations = find_unique_pos_sums(h)
    row_permutations = permutations_of_cycle_combinations(
        row_cycle_combinations, h
    )
    col_cycle_combinations = find_unique_pos_sums(w)
    col_permutations = permutations_of_cycle_combinations(
        col_cycle_combinations, w
    )
    n_fix = 0
    order_G = 0

    for n_col_permutations, col_permutation in col_permutations:
        for n_row_permutations, row_permutation in row_permutations:
            order_G += n_col_permutations * n_row_permutations
            n_cycles = 0
            for col_cycle_len, n_col_cycles in col_permutation.items():
                for row_cycle_len, n_row_cycles in row_permutation.items():
                    n_repetitions = n_col_cycles * n_row_cycles
                    n_cycles += (
                        gcd(col_cycle_len, row_cycle_len) * n_repetitions
                    )
            n_similar_actions = n_col_permutations * n_row_permutations
            n_fix += n_similar_actions * s**n_cycles
    n_groups = n_fix / order_G

    return str(n_groups)
