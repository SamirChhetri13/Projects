import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

# get the folder where the code is located
current_folder = os.path.dirname(os.path.abspath(__file__))

#build the full path to the image file in that folder
image_path = os.path.join(current_folder,'photo.jpg')

#open the image
img = Image.open(image_path)
img_np = np.array(img)

# Convert to grayscale
gray_img = np.mean(img_np, axis=2).astype(np.uint8)

# Flip image horizontally
flipped_img = np.fliplr(gray_img)

# Apply thresholding
threshold_value = 100   #pixel greater than 100 will be white otherwise black
threshold_img = (gray_img > threshold_value) * 255
threshold_img = threshold_img.astype(np.uint8)

# Plot all images
plt.figure(figsize=(12, 8)) # size for plotting

plt.subplot(2, 2, 1) # 2rows 2columns 1st boxs
plt.title('Original Image')
plt.imshow(img_np)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Grayscale')
plt.imshow(gray_img, cmap='gray') #camp ='gray' makes sure it display grayscale image
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Flipped Image')
plt.imshow(flipped_img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Threshold Image')
plt.imshow(threshold_img, cmap='gray')
plt.axis('off')

plt.tight_layout() # adjusts space so that the image and title don't overlap
plt.show()



