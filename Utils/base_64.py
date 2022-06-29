import base64
import random
import string

def encode_base64(filepath):
    with open(filepath,"rb") as img:
        b64_string = base64.b64encode(img.read())
        # print(b64_string.decode('utf-8'))
    return b64_string

def decode_base64(img_data):
    file_name = "base_decoded"+''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)for p in range(5))
    path = f"Base64/decode/{file_name}.png"
    with open(path,"wb") as fh:
        fh.write(base64.b64decode(img_data))
    return path



# imgdata = base64.b64decode(strd)
# filename = "soame"
# path = f"Base64/decode/{filename}.png"

# with open(path,"wb") as f:
#     f.write(imgdata)