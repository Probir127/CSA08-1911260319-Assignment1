"""Season boundaries, fractional readings, bonus and complete statements."""
from seasonal import exact_rate, seasonal_payout, bonus, statement
from decimal import Decimal as D
from datetime import date
cases = [
    (date(2026,3,31), '3.5','8.5','30.00','300.00'),
    (date(2026,4,1), '3.5','8.5','32.00','320.00'),
    (date(2026,6,30), '3.5','8.5','32.00','320.00'),
    (date(2026,7,1), '3.5','8.5','30.00','300.00'),
    (date(2026,4,1), '4.25','8.65','35.825','358.25'),
    (date(2026,11,1), '4.25','8.65','33.45','334.50'),
    (date(2026,4,1), '3.45','8.45','31.625','316.25'),
]
for day, fat, snf, rate, pay in cases:
    actual_rate, actual_pay = exact_rate(fat,snf,day), seasonal_payout('10',fat,snf,day)
    assert actual_rate == D(rate) and actual_pay == D(pay)
    print(day, fat, snf, 'rate=', actual_rate, 'pay=', actual_pay, 'PASS')
for litres, expected in [('499.999','0.00'), ('500','0.00'), ('500.001','250.00'), ('501','250.50')]:
    assert bonus(litres) == D(expected)
    print('Bonus litres=', litres, 'expected=', expected, 'actual=', bonus(litres), 'PASS')
rows = [dict(farmer_id='F001', date=date(2026,4,1), shift='AM', litres='250', fat='3.5', snf='8.5'),
        dict(farmer_id='F001', date=date(2026,4,1), shift='PM', litres='251', fat='3.5', snf='8.5')]
assert statement(rows, 'F001', date(2026,4,1)) == (D('16032.00'),D('250.50'),D('16282.50'))
rows[0]['date'], rows[1]['date'] = date(2026,11,1), date(2026,11,1)
assert statement(rows, 'F001', date(2026,11,1)) == (D('15030.00'),D('250.50'),D('15280.50'))
cross = [dict(rows[0], date=date(2026,3,31), litres='10'),
         dict(rows[1], date=date(2026,4,1), litres='10')]
assert statement(cross, 'F001', date(2026,3,31)) == (D('620.00'),D('0.00'),D('620.00'))
try:
    seasonal_payout('1','3.555','8.5',date(2026,4,1))
except ValueError:
    pass
else:
    raise AssertionError('Three decimal fat reading accepted')
print('Both full statements, mixed-season period and resolution rejection PASS')
