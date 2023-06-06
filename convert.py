from PIL import Image
import numpy as np
import sys

# Open image named input.png
image = Image.open('input.jpeg')

# Resize image to 6x6 pixels
image = image.resize((6,6), Image.ANTIALIAS)

# Convert image to BW
image = image.convert('1')

# Save image as output
image.save('output.jpeg')

# Convert image to numpy array
image = np.array(image)

# Print image
print(image)
print(image.shape)