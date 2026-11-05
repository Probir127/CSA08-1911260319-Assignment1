"""Independent expected payments and rejection/boundary tests."""
import sys
from pathlib import Path
from decimal import Decimal as D
from datetime import date
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Task06'))
from calculator import payout, ten_day_total, validate_entry
cases = [
    ('standard', ('10','3.5','8.5'), '300.00'),
    ('above', ('8.5','4.2','8.7'), '283.90'),
    ('below', ('12','3.1','8.3'), '333.60'),
    ('lowest fat', ('5','2.0','8.5'), '120.00'),
    ('highest fat', ('4','7.0','8.5'), '176.00'),
    ('zero litres', ('0','3.5','8.5'), '0.00'),
    ('half paisa up', ('0.001','2.1','8.7'), '0.03'),
]
for label, args, expected in cases:
    actual = payout(*args)
    assert actual == D(expected), (label, actual, expected)
    print(f'{label:18} expected={expected:>7} actual={actual:>7} PASS')
invalid = [('eight','3.5','8.5'), ('-1','3.5','8.5'), ('1','1.9','8.5'),
           ('1','7.1','8.5'), ('1','3.5','8,5'), ('nan','3.5','8.5'),
           ('1','3.55','8.5'), ('1','3.5','10.1'), ('Infinity','3.5','8.5')]
for args in invalid:
    try:
        payout(*args)
    except ValueError:
        print('Expected rejection:', args, 'PASS')
    else:
        raise AssertionError(('Accepted invalid entry', args))
assert sum((payout(*args) for _, args, _ in cases[:5]), D(0)) == D('1213.50')
rows = [dict(farmer_id='F001', date=date(2026,11,1), shift='AM',
             litres='10', fat='3.5', snf='8.5'),
        dict(farmer_id='F001', date=date(2026,11,10), shift='PM',
             litres='10', fat='3.5', snf='8.5'),
        dict(farmer_id='F001', date=date(2026,11,11), shift='AM',
             litres='10', fat='3.5', snf='8.5'),
        dict(farmer_id='F002', date=date(2026,11,1), shift='AM',
             litres='10', fat='3.5', snf='8.5')]
assert ten_day_total(rows, 'F001', date(2026,11,1)) == D('600.00')
bad = dict(rows[0], shift='night')
try:
    validate_entry(bad)
except ValueError:
    pass
else:
    raise AssertionError('Invalid shift accepted')
print('Five-entry total: 1213.50 PASS; date/farmer filtering PASS; invalid shift PASS')
