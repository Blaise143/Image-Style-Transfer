import requests
import numpy as np
from PIL import Image
from urllib import request
import matplotlib.pyplot as plt
import copy

# url = "https://cdn.mos.cms.futurecdn.net/W2xQZxs7T2gUE2fMbUv4s6-320-80.jpg"

# f = open('flowers', 'wb')
# f.write(requests.get(url).content)
# f.close()
blaise = plt.imread("Image/Blaise.jpeg")
starry = plt.imread("Image/StaryNight.jpg")
sunset = plt.imread("Image/sunset.jpeg")
genius = plt.imread("Image/einstein.jpeg")
# blaise = np.rot90(blaise, k=3)
# np.rot90(blaise)
# print(stary)
# print(blaise)
# plt.imshow(stary)
# plt.show()
# plt.imshow(blaise)
# plt.show()
# print(f"Blaise Shape: {blaise.shape}")
# print(f"Stary Shape: {starry.shape}")
# print(f"sunset Shape: {sunset.shape}")
# blaise_2 = copy.deepcopy(blaise)

# img = Image.open("Image/Blaise.jpeg")
# area = (384, 384, 510, 510)
# cropped_img = img.crop(area)
# cropped_img.show()
blaise = Image.open('Image/Blaise.jpeg')
new_image = blaise.resize((769, 1021))
new_image.save('new_blaise_2.jpeg')
# im = plt.imread("myimage_500.jpg")
# print(im.shape)
# starry = Image.open("Image/StaryNight.jpg")
# starry = starry.resize((1021, 769))
# starry.save("new_starry.jpg")
# starry = plt.imread("new_starry.jpg")
# blaise = plt.imread("new_blaise.jpg")
# blaise = np.rot90(blaise, k=3)
# plt.imshow(blaise)
# plt.show()
print(f"blaise shape: {blaise.shape}")
# print(new_image.shape)
print(f"sunset shape: {sunset.shape}")
# print(blaise.shape)
# print(genius.shape)
print(f"starry shape: {starry.shape}")

