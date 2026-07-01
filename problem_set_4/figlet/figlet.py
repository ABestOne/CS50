import sys
from pyfiglet import Figlet
import random

fonts = Figlet().getFonts()
if len(sys.argv) == 1:
    f = Figlet(font=random.choice(fonts))
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
        f = Figlet(font=sys.argv[2])
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
input_string = input('Input: ')
print('Output: ')
print(f.renderText(input_string))


