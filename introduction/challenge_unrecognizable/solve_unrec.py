# p1, p2, k
# c1 = p1 ^ k
# c2 = p2 ^ k

# c1 ^ c2 = p1 ^ k ^ c2 ^ k = p2 ^ p1

# dobbiamo fare lo xor tra le 2 immagini


#!/usr/local/bin/python3
import numpy as np
from PIL import Image

# Open images
im1 = Image.open("challenge.png")
im2 = Image.open("whoami.png")

# Make into Numpy arrays
im1np = np.array(im1)*255
im2np = np.array(im2)*255

# XOR with Numpy
result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

# Convert back to PIL image and save
Image.fromarray(result).save('result.png')
