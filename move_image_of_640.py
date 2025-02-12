import os
from PIL import Image
import shutil

def move_images_with_size(source_folder, target_folder, target_size=(640, 640)):
    """
    Move images with the specified size and their corresponding .txt files
    from the source folder to the target folder.

    :param source_folder: Path to the source folder containing images and .txt files
    :param target_folder: Path to the target folder where files will be moved
    :param target_size: Tuple specifying the target image size (width, height)
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    moved_count = 0

    for file in os.listdir(source_folder):
        if file.lower().endswith('.jpg'):
            image_path = os.path.join(source_folder, file)
            txt_path = os.path.join(source_folder, f"{os.path.splitext(file)[0]}.txt")

            try:
                # Open the image and check its size
                with Image.open(image_path) as img:
                    if img.size == target_size:
                        # Move the image file
                        shutil.move(image_path, os.path.join(target_folder, file))

                        # Move the corresponding .txt file if it exists
                        if os.path.exists(txt_path):
                            shutil.move(txt_path, os.path.join(target_folder, os.path.basename(txt_path)))

                        moved_count += 1
            except Exception as e:
                print(f"Error processing file {file}: {e}")

    print(f"Total files moved: {moved_count}")

###########################################
# Define paths and target size
source_folder = r'D:\usman Nasir\Unilever Final Version\Unilever Version wise Data\helmet_person_vest\Datasets\V8_datasets'
target_folder = r'C:\Users\rahee\Desktop\New folder'
target_size = (640, 480)

# Run the function
move_images_with_size(source_folder, target_folder, target_size)
