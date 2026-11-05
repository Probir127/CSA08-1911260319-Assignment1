"""Seasonal calculator with proportional 0.1% steps and period bonus."""
import sys
from pathlib import Path
from decimal import Decimal as D
from datetime import timedelta
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Task06'))
from calculator import (measurement, money, MIN_FAT, MAX_FAT, MIN_SNF,
                        MAX_SNF, BASE_FAT, BASE_SNF, STEP)
BONUS_THRESHOLD, BONUS_PER_LITRE = D('500'), D('0.50')
def select_rates(collection_date):
    """Return base, fat-step and SNF-step values for the collection date."""
    if 4 <= collection_date.month <= 6:
        return D('32.00'), D('0.45'), D('0.30')
    return D('30.00'), D('0.40'), D('0.30')
def exact_rate(fat, snf, collection_date):
    """Keep fractional steps and the unrounded rate until payment posting."""
    fat = measurement(fat, MIN_FAT, MAX_FAT, D('0.01'))
    snf = measurement(snf, MIN_SNF, MAX_SNF, D('0.01'))
    base, fat_value, snf_value = select_rates(collection_date)
    return base + (fat-BASE_FAT)/STEP*fat_value + (snf-BASE_SNF)/STEP*snf_value
def seasonal_payout(litres, fat, snf, collection_date):
    """Round litres times the unrounded rate to paise once per delivery."""
    litres = measurement(litres, D('0'), None, D('0.001'))
    return money(litres * exact_rate(fat, snf, collection_date))
def bonus(total_litres):
    """Pay 0.50 on ALL period litres only when the total exceeds 500."""
    total_litres = measurement(total_litres, D('0'), None, D('0.001'))
    return money(total_litres * BONUS_PER_LITRE) if total_litres > BONUS_THRESHOLD else D('0.00')
def statement(entries, farmer_id, start):
    """Return base payment, bonus and total for one farmer and ten-day window."""
    end, pay, litres = start + timedelta(days=10), D('0.00'), D('0')
    seen = set()
    for row in entries:
        if row['farmer_id'] != farmer_id or not start <= row['date'] < end:
            continue
        if not isinstance(row['farmer_id'], str) or not row['farmer_id'].strip():
            raise ValueError('Farmer ID must be nonempty text')
        if row['shift'] not in ('AM','PM'):
            raise ValueError('Invalid shift')
        key = row['date'], row['shift']
        if key in seen:
            raise ValueError('Duplicate delivery')
        seen.add(key)
        pay += seasonal_payout(row['litres'], row['fat'], row['snf'], row['date'])
        litres += D(str(row['litres']))
    extra = bonus(litres)
    return pay, extra, pay + extra
