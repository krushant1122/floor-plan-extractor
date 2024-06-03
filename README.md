<img width="1440" alt="image" src="https://github.com/krushant1122/floor-plan-extractor/assets/63834509/387b1c6a-9f05-4cd1-95cb-1e51dd48a5af">
# 3D to Floor Plan Converter

This script converts 3D images into floor plans by segmenting and extracting the floor area from the image.

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/3d-to-floor-plan.git
2. Install the required dependencies:
pip install opencv-python numpy matplotlib


Usage
Run the script main.py and provide the path to the 3D image as an argument using the --image flag.
python main.py --image path/to/3d_image.jpg
The script will display the original 3D image alongside the extracted floor plan.

Example
python main.py --image example_images/3d_image.jpg
Customization
You may need to adjust the color range defined in the create_floor_plan() function to match the floor color of your images. This can be done by modifying the lower_floor_color and upper_floor_color arrays.

