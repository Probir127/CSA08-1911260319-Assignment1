"""Running totals implement the hand trace in the report."""
import sys
from pathlib import Path
from decimal import Decimal
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Task06'))
from calculator import payout
total = Decimal('0.00')
for row in [('10','3.5','8.5'), ('8.5','4.2','8.7'), ('12','3.1','8.3')]:
    pay = payout(*row)
    total += pay
    print('Input:', row, 'payment:', pay, 'running total:', total)
