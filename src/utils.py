import numpy as np

def create_floor_plan(segmentation):
    # Simple thresholding approach to create a binary floor plan
    # This is a placeholder function; refine as needed
    floor_plan = np.zeros_like(segmentation)
    floor_plan[segmentation == 15] = 255  # Assuming class 15 is the floor class
    return floor_plan
