import sys
from pyfiglet import Figlet


if len(sys.argv) == 1:
    f = Figlet()
if len(sys.argv) == 3:
    if(sys.argv[1] in ['-f', '--font']):
        f = Figlet(font=sys.argv[2])

print(f'Output: {f.renderText(input('Input: '))}')
