"""Measured float drift and cache timings; dataset repeats a known payment."""
from decimal import Decimal as D
from time import perf_counter
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Task06'))
from calculator import rate_per_litre, payout
def timed(fn):
    """Return the result and elapsed seconds of a callable."""
    begin = perf_counter()
    result = fn()
    return result, perf_counter() - begin
def add_float(n):
    """Accumulate already-rounded float payments."""
    total = 0.0
    for _ in range(n):
        total += 33.40
    return total
def add_decimal(n):
    """Accumulate exact Decimal payments."""
    total, payment = D('0.00'), D('33.40')
    for _ in range(n):
        total += payment
    return total
def add_paise(n):
    """Accumulate exact integer paise."""
    total = 0
    for _ in range(n):
        total += 3340
    return total
def full_calculator(n):
    """Validate, compute and round n one-litre deliveries and add payments."""
    total = D('0.00')
    for _ in range(n):
        total += payout('1', '4.2', '8.7')
    return total
results = []
for n in (300, 6000, 150000):
    f, ft = timed(lambda: add_float(n))
    d, dt = timed(lambda: add_decimal(n))
    p, pt = timed(lambda: add_paise(n))
    calculated, ct = timed(lambda: full_calculator(n))
    assert calculated == d
    row = dict(n=n, float_repr=repr(f), decimal=str(d),
               difference=str(D.from_float(f)-d), float_seconds=ft,
               decimal_seconds=dt, paise_seconds=pt, full_calculator_seconds=ct,
               float_rounded_matches=(D(str(round(f,2))) == d))
    assert D(p) / 100 == d
    results.append(row)
pairs = [('3.5','8.5'), ('4.2','8.7'), ('3.1','8.3')] * 50000
def recalculate():
    """Calculate a rate for each record."""
    return sum((rate_per_litre(*key) for key in pairs), D(0))
def cached():
    """Build a local cache for one immutable rate card."""
    cache, total = {}, D(0)
    for key in pairs:
        if key not in cache:
            cache[key] = rate_per_litre(*key)
        total += cache[key]
    return total
a, at = timed(recalculate)
b, bt = timed(cached)
assert a == b
result = dict(python=sys.version, totals=results,
              cache=dict(n=len(pairs), k=3, recompute_seconds=at, cache_seconds=bt))
print(json.dumps(result, indent=2))
