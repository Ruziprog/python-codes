import csv

FILE = 'animes.csv'
YEAR_COL = 'year'
VALUE_COL = 'episodes'
NAME_COL = 'title'
MIN_YEAR = 1900

total = 0
count = 0

with open(FILE, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            year_str = str(row[YEAR_COL])
            year = int(year_str[:4])
            value = int(row[VALUE_COL])
        except (ValueError, KeyError, TypeError):
            continue

        if year > MIN_YEAR:
            total += value
            count += 1

if count > 0:
    print(f"\nAverage: {total / count:.1f}")
else:
    print("No data found.")