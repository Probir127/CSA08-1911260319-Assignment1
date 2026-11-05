"""Load exact rates from a JSON configuration with string-valued decimals."""
import json
from decimal import Decimal
from pathlib import Path
with Path(__file__).with_name('rates.json').open() as stream:
    rate_card = {key: Decimal(value) for key, value in json.load(stream).items()}
assert set(rate_card) == {'base', 'fat', 'snf'}
assert all(value.is_finite() and value >= 0 for value in rate_card.values())
print(rate_card)
