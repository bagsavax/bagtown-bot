import os
from io import BytesIO
import requests
from PIL import Image, ImageOps

def prep_gpt_image(filename, name, new_name=None):
    """
    
    """
    if str(filename).find('https') == -1:
        initial_image = Image.open(str(filename))
    else:
        response = requests.get(str(filename))
        initial_image = Image.open(BytesIO(response.content))
    rgba_image = initial_image.convert('RGBA')
    rgba_image = rgba_image.resize((1024,1024))
    # 256, 512, 1024
    border = 300
    alpha = Image.new('L', (1024-2*border,1024-2*border), "white")
    alpha = ImageOps.expand(alpha, border)
    im = rgba_image.convert('RGB')
    im.putalpha(alpha)
    byte_stream = BytesIO()
    im.save(byte_stream, format='PNG')

    return byte_stream.getvalue()
