import cv2
import numpy as np
import matplotlib.pyplot as plt
from segmentation_model import load_model, segment_image

def create_floor_plan(image):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define floor color range in HSV
    # These values may need to be adjusted depending on the floor color
    lower_floor_color = np.array([10, 0, 0])
    upper_floor_color = np.array([40, 255, 255])

    # Threshold the HSV image to get only floor colors
    mask = cv2.inRange(hsv, lower_floor_color, upper_floor_color)

    # Focus on the lower half of the image for floor detection
    height, width = mask.shape
    mask[0:height//2, :] = 0

    # Morphological operations to remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask

def main(image_path):
    # Load the 3D image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Create floor plan using color-based segmentation
    floor_plan = create_floor_plan(image)

    # Display the original image and the floor plan
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Original 3D Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title('Extracted Floor Plan')
    plt.imshow(floor_plan, cmap='gray')
    plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert 3D images into floor plans.")
    parser.add_argument("--image", type=str, required=True, help="Path to the 3D image.")
    args = parser.parse_args()
    main(args.image)
