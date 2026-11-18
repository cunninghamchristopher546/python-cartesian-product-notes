import itertools

def solve(value):
    return [list(pair) for pair in itertools.product(value[0], value[1])]
