"""Read a sequence of clerk entries and print one ten-day total."""
import sys
from pathlib import Path
from datetime import date
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Task06'))
from calculator import validate_entry, ten_day_total
def main():
    """Collect validated records; blank farmer ID ends data entry."""
    farmer = input('Farmer ID for statement: ').strip()
    start = date.fromisoformat(input('Period start (YYYY-MM-DD): ').strip())
    entries, seen = [], set()
    while True:
        farmer_id = input('Entry farmer ID (blank ends): ').strip()
        if not farmer_id:
            break
        try:
            entry = dict(farmer_id=farmer_id,
                         date=date.fromisoformat(input('Date: ').strip()),
                         shift=input('Shift AM/PM: ').strip().upper(),
                         litres=input('Litres: '), fat=input('Fat %: '), snf=input('SNF %: '))
            pay = validate_entry(entry)
            key = entry['farmer_id'], entry['date'], entry['shift']
            if key in seen:
                raise ValueError('Duplicate farmer/date/shift')
            seen.add(key)
            entries.append(entry)
            print(f'Payment: Rs {pay:8.2f}')
        except (ValueError, KeyError) as error:
            print('Rejected:', error)
    print(f'Ten-day total for {farmer}: Rs {ten_day_total(entries, farmer, start):.2f}')
if __name__ == '__main__':
    main()
