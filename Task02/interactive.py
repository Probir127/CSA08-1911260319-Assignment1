"""Reproduce interpreter expressions and print actual prompts and results."""
import sys
from decimal import Decimal
expressions = ['type(10)', 'type(10.0)', 'type("10")', 'type(True)',
               'type([10, 8.5])', '7 / 2', '7 // 2', '7 % 2', '-7 // 2',
               '0.1 + 0.2', '0.1 + 0.2 == 0.3',
               'Decimal("0.1") + Decimal("0.2") == Decimal("0.3")']
for expression in expressions:
    print('>>>', expression)
    print(repr(eval(expression)))
for value in [3340030, 33400.30, Decimal('33400.30')]:
    print(type(value).__name__, 'bytes =', sys.getsizeof(value))
