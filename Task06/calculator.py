"""Exact original milk calculator. Decimal input is created from text."""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from datetime import date, timedelta

BASE_RATE = Decimal('30.00')
BASE_FAT = Decimal('3.5')
BASE_SNF = Decimal('8.5')
STEP = Decimal('0.1')
FAT_STEP_VALUE = Decimal('0.40')
SNF_STEP_VALUE = Decimal('0.30')
MIN_FAT, MAX_FAT = Decimal('2.0'), Decimal('7.0')
MIN_SNF, MAX_SNF = Decimal('6.0'), Decimal('10.0')  # Assumed limits
PAISA = Decimal('0.01')

def number(value):
    """Return a finite Decimal; reject booleans, NaN and infinity."""
    if isinstance(value, bool):
        raise ValueError('A boolean is not a measurement')
    try:
        result = value if isinstance(value, Decimal) else Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError('Enter a number using a decimal point') from None
    if not result.is_finite():
        raise ValueError('The number must be finite')
    return result

def measurement(value, lower, upper, quantum):
    """Validate range and measurement resolution, returning a Decimal."""
    value = number(value)
    if value < lower or (upper is not None and value > upper):
        raise ValueError('Measurement outside allowed range')
    if value % quantum != 0:
        raise ValueError('Too many decimal places')
    return value

def money(value):
    """Round one monetary amount to the nearest paisa, ties upward."""
    return value.quantize(PAISA, rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    """Return the exact rate for original readings at 0.1% resolution."""
    fat = measurement(fat, MIN_FAT, MAX_FAT, STEP)
    snf = measurement(snf, MIN_SNF, MAX_SNF, STEP)
    return money(BASE_RATE + (fat - BASE_FAT) / STEP * FAT_STEP_VALUE
                 + (snf - BASE_SNF) / STEP * SNF_STEP_VALUE)

def payout(litres, fat, snf):
    """Return one payment rounded to paise; allow litre precision of 0.001."""
    litres = measurement(litres, Decimal('0'), None, Decimal('0.001'))
    return money(litres * rate_per_litre(fat, snf))

def validate_entry(entry):
    """Check identity, date, shift and numeric fields of one dictionary."""
    if not isinstance(entry['farmer_id'], str) or not entry['farmer_id'].strip():
        raise ValueError('Farmer ID must be nonempty text')
    if entry['shift'] not in ('AM', 'PM'):
        raise ValueError('Shift must be AM or PM')
    if type(entry['date']) is not date:
        raise ValueError('Date must be a calendar date')
    return payout(entry['litres'], entry['fat'], entry['snf'])

def ten_day_total(entries, farmer_id, start):
    """Sum posted payments for one farmer in [start, start + 10 days)."""
    end = start + timedelta(days=10)
    total = Decimal('0.00')
    for entry in entries:
        pay = validate_entry(entry)
        if entry['farmer_id'] == farmer_id and start <= entry['date'] < end:
            total += pay
    return total
