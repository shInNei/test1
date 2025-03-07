import cv2
import os

# Input and output folder paths
input_folder = "output_frames"
output_folder = "output_frames"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    
    # Check if it's an image
    if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # Read the image
        image = cv2.imread(input_path)
        
        # Resize to 224x224
        resized_image = cv2.resize(image, (240, 180))
        
        # Save the resized image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_image)

print("Resizing complete!")
