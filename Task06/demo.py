"""Demonstrate pure calculation functions."""
from calculator import rate_per_litre, payout
for litres, fat, snf in [('10','3.5','8.5'), ('8.5','4.2','8.7'), ('12','3.1','8.3')]:
    print('Rate:', rate_per_litre(fat, snf), 'Payment:', payout(litres, fat, snf))
