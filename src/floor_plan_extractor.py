import cv2
import numpy as np
import matplotlib.pyplot as plt
from segmentation_model import load_model, segment_image
from utils import create_floor_plan

def main(image_path):
    # Load the 3D image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Segment the image to identify the floor plan
    model = load_model()
    segmentation = segment_image(model, image)

    # Extract the floor plan from the segmentation
    floor_plan = create_floor_plan(segmentation)

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
