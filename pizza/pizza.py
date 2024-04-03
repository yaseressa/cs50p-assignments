import sys
import os
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    if sys.argv[1][-4:] != '.csv':
        sys.exit('Not a CSV file')
    if not os.path.exists(sys.argv[1]):
        sys.exit('File does not exist')
data = []
with open(sys.argv[1]) as file:
    for row in file:
        row = row.strip().split(',')
        data.append([row[0], row[1], row[2]])
print(tabulate(data[1:], data[0], tablefmt="grid"))



