"""Compare a simple decimal grammar with float conversion."""
import math
def simple_number(text):
    """Accept an optional sign and ASCII digits with at most one dot."""
    text = text.strip()
    if text[:1] in ('+', '-'):
        text = text[1:]
    return (bool(text) and text.count('.') <= 1
            and any(c in '0123456789' for c in text)
            and all(c in '0123456789.' for c in text))
for text in ['8,5', ' 8.5 ', 'eight', '-2', 'nan', '1e2']:
    try:
        value = float(text)
        converted = str(value) if math.isfinite(value) else 'reject nonfinite'
    except ValueError:
        converted = 'invalid'
    print(repr(text), 'simple check:', simple_number(text), 'try float:', converted)
amount = 283.90
print(f'{"Farmer":<10}{"Amount":>10}')
print(f'{"F001":<10}{amount:10.2f}')
