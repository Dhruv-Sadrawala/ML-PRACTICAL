from imageio import imread, imwrite
from PIL import Image
import numpy as np

# Read a JPEG image into a numpy array
img = imread('cats.jpeg')  # Replace with a valid image path
print(img.dtype, img.shape)

# Tinting the image
img_tint = img * [1, 0.45, 0.3]
img_tint = np.clip(img_tint, 0, 255).astype(np.uint8)  # Ensure values are in valid range

# Saving the tinted image
imwrite('tinted_image.jpg', img_tint)  # Save to a valid path

# Resizing the tinted image to be 300 x 300 pixels
img_tint_resize = Image.fromarray(img_tint).resize((300, 300))

# Saving the resized tinted image
img_tint_resize.save('resized_tinted_image.jpg')  # Save to a valid path

print("Image Processing Completed.")
