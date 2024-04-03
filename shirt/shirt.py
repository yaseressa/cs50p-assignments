import sys
import os
from PIL import Image, ImageOps
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    if not(sys.argv[1].endswith('.jpg') or sys.argv[1].endswith('.jpeg') or sys.argv[1].endswith('.png')):
        sys.exit('Not an Image file')
    if sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit('Invalid Output Image File.')
    if not os.path.exists(sys.argv[1]):
        sys.exit(f'Could not read {sys.argv[1]}')

img = Image.open(sys.argv[1])
mask = Image.open('shirt.png')
img_resize = ImageOps.fit(img, (600, 600), bleed=0.0, centering=(0.5, 0.5))
img_resize.paste(mask, box=None, mask=mask)


img_resize.save(sys.argv[2])
