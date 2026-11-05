"""Explore expressions and negative step counts."""
import math
for expression in ['-2 ** 2', '(-2) ** 2', '2 ** 3 ** 2',
                   '(4.2 - 3.5) / 0.1', '(3.1 - 3.5) / 0.1',
                   'round(-3.6)', 'int(-3.6)', 'math.floor(-3.6)']:
    print(expression, '=', eval(expression))
for fat in [4.2, 3.1]:
    raw = (fat - 3.5) / 0.1
    for fn in [round, int, math.floor]:
        steps = fn(raw)
        print(f'fat={fat}, {fn.__name__}: steps={steps}, rate={30 + steps * .4:.2f}')
