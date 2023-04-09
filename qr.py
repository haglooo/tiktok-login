from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
import random

def gen(qr_data):
    qr = base64.b64decode(qr_data)
    img = Image.open(BytesIO(qr))
    image = img.convert("RGB")
    width, height = image.size
    hex_digits = "0123456789abcdef"
    hex_code = "#" + "".join(random.choices(hex_digits, k=6))
    rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))
    for x in range(width):
        for y in range(height):
            current_color = image.getpixel((x, y))
            if current_color == (255, 255, 255):
                image.putpixel((x, y), (0, 0, 0))
            if current_color == (0, 0, 0):
                image.putpixel((x, y), rgb_code)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font.ttf", 25)
    position = (50, 470)
    draw.text(position, "t.me/@haglooo", font=font, fill=(255, 255, 255))


    image.show()