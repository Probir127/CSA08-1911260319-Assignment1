"""Naming, dynamic typing, multiple assignment and swapping."""
BASE_RATE = '30.00'
FAT_STEP_VALUE = '0.40'
SNF_STEP_VALUE = '0.30'
value = 10
print(value, type(value))
value = '10'
print(value, type(value))
a, b = 1, 2
a, b = b, a
print('After swap:', a, b)
