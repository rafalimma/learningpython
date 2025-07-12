from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'imagem.jpg'
NEW = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(ORIGINAL)
print(pil_image.size)
width, height = pil_image.size
exif = pil_image.info
print(exif)
new_width = 640
new_height = height * new_width / width
new_height = int(new_height)
# print(new_width, new_height)

new_image = pil_image.resize(new_width, new_height)
new_image.save(NEW, optimize=True, quality=70, exif=exif)
