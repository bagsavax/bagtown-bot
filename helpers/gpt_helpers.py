import os
from io import BytesIO
import requests
from PIL import Image, ImageOps

def prep_gpt_image(filename, name, new_name=None):
    # dont judge me im tired
        img_file = str(filename)
        image_name = name
        if img_file.find('https') == -1:
            rgb_image = Image.open(img_file)
        else:
            response = requests.get(img_file)
            rgb_image = Image.open(BytesIO(response.content))
        rgba_image = rgb_image.convert('RGBA')
        rgba_image = rgba_image.resize((1024,1024))
        # 256, 512, 1024
        converted_name = "{}-temp.png".format(name)
        # Convert the image to a BytesIO object
        # byte_stream = BytesIO()
        # image.save(byte_stream, format='PNG')
        # byte_array = byte_stream.getvalue()
        rgba_image.save(converted_name)

        print('image size:' + "\t", rgba_image.size)
        img = Image.open(converted_name)
        border = 300
        alpha = Image.new('L', (1024-2*border,1024-2*border), "white")
        alpha = ImageOps.expand(alpha, border)
        im = Image.open(converted_name).convert('RGB')
        im.putalpha(alpha)
        byte_stream = BytesIO()
        im.save(byte_stream, format='PNG')
        return byte_stream.getvalue()
        # im.save(f'RESULT-{name}.png')
