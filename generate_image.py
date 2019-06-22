from PIL import Image, ImageDraw, ImageFont
import os
def generate(text):
    color = (0, 0, 0)
    img = Image.new('RGB', (500, 500), color)
    imgDrawer = ImageDraw.Draw(img)
    font = ImageFont.truetype('8133.ttf', 72)
    imgDrawer.text((20, 210), text,( 97,237,132), font = font)

    img.save('123.png')
    return '123.png'