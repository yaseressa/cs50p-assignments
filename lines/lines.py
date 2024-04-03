import sys
import os
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    if sys.argv[1][-3:] != '.py':
        sys.exit('Not a Python file')
    if not os.path.exists(sys.argv[1]):
        sys.exit('File does not exist')
length = 0
with open(sys.argv[1]) as file:
    for line in file:
        if not(line.strip().startswith('#')) and line.strip():
            length += 1
print(length)
