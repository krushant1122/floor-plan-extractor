import numpy as np
from scipy.ndimage import label

def create_floor_plan(segmentation):
    # Identify the unique classes in the segmentation output
    unique_classes = np.unique(segmentation)
    print("Unique classes in segmentation:", unique_classes)
    
    # Heuristic: Assume the floor class is the one with the largest connected component in the lower half
    height, width = segmentation.shape
    lower_half = segmentation[height // 2:, :]
    
    largest_component_size = 0
    floor_class = 0
    
    for cls in unique_classes:
        if cls == 0:
            continue  # Skip background class
        
        class_mask = (lower_half == cls).astype(np.uint8)
        labeled, num_features = label(class_mask)
        
        for feature in range(1, num_features + 1):
            component_size = np.sum(labeled == feature)
            if component_size > largest_component_size:
                largest_component_size = component_size
                floor_class = cls
    
    print(f"Assumed floor class: {floor_class}")
    
    # Create floor plan based on the identified floor class
    floor_plan = np.zeros_like(segmentation)
    floor_plan[segmentation == floor_class] = 255
    
    return floor_plan
