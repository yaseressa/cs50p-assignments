import sys
import os
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    if sys.argv[1][-4:] != '.csv' or sys.argv[2][-4:] != '.csv':
        sys.exit('Not a CSV file')
    if not os.path.exists(sys.argv[1]):
        sys.exit(f'Could not read {sys.argv[1]}')

students = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})

with open(sys.argv[2], 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow({"first": student["name"].split(',')[1].strip(), "last": student["name"].split(',')[0], "house": student["house"]})


