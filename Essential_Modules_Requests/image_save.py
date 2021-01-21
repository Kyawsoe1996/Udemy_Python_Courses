import requests
from io import BytesIO
from PIL import Image
import pdb;pdb.set_trace()
r = requests.get("https://cdn.hipwallpaper.com/m/64/30/78NJUa.jpg")
# r = requests.get("https://wallpapercave.com/wp/wp2831915.png")
print(r.status_code)
print(r.url)
print(r.headers)
image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image6." + image.format

try:
    image.save(path)
except IOError:
    print("Cannot Save")
