from PIL import Image
from PIL.ExifTags import TAGS

def get_data(img_path):
    img = Image.open(img_path)
    info = img.getexif()

    for tag_id in info:
        name = TAGS.get(tag_id, tag_id)
        value = info.get(tag_id)
        print(f"{name}: {value}")

get_data("example.jpeg")