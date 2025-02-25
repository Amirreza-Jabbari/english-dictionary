import sys
import csv
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

search_index = input('Enter vocabulary to find\n')
search_index = search_index.capitalize()
csv_file = csv.reader(open('english Dictionary.csv', "r"), delimiter=",")
for row in csv_file:
    if search_index == row[0]:
        print(*row[1:], sep='\n')
