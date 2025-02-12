# import os
# import random
# from tqdm.notebook import tqdm
# import shutil
# import yaml


# def train_test_split(path, train_ratio, val_ratio):
#     print("----PROCESS STARTED----")

#     # Get a list of all files in the folder
#     files = [file for file in os.listdir(path) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

#     print(f"--- This folder has a total number of {len(files)} images ---")
#     random.seed(42)
#     random.shuffle(files)

#     # determine the number of images for each set
#     train_size = int(len(files) * train_ratio)
#     val_size = int(len(files) * val_ratio)
#     test_size = len(files) - train_size - val_size
#     print("train_images: ", train_size)
#     print("val_images: ", val_size)
#     print("test_images: ", test_size)

#     # Define main folder name with train and val lengths
#     main_folder = f"data_train_{train_size}_val_{val_size}_test_{test_size}"

#     # Define subfolders
#     subfolders = ["train/images", "train/labels", "val/images", "val/labels", "test/images", "test/labels"]

#     # Creating required directories with train and val lengths in folder names
#     for subfolder in subfolders:
#         os.makedirs(os.path.join(main_folder, subfolder), exist_ok=True)

    
#     # Copying images to train, validation, and test folders
#     for data_type, start, end, message in [("train", 0, train_size, "Training"),
#                                                ("val", train_size, train_size + val_size, "Validation"),
#                                                ("test", train_size + val_size, None, "Test")]:
#             for file in tqdm(files[start:end]):
#                 if file == 'classes':
#                     continue
#                 img_source_path = os.path.join(path, file)
#                 label_source_path = os.path.join(path, f"{os.path.splitext(file)[0]}.txt")
#                 img_dest_path = os.path.join(main_folder, f"{data_type}/images", file)
#                 label_dest_path = os.path.join(main_folder, f"{data_type}/labels", f"{os.path.splitext(file)[0]}.txt")

#                 shutil.copy2(img_source_path, img_dest_path)
#                 shutil.copy2(label_source_path, label_dest_path)

#             print(f"--- {message} data created with {len(files[start:end])} images ---")

#     print()
#     print(main_folder)
# #     return main_folder


# ###########################################
# path = r'C:\Users\rahee\Desktop\Total_annotated_frames'
# train_ratio = 0.89
# val_ratio = 0.10

# train_test_split(path, train_ratio, val_ratio)


# main_folder = r"C:\Users\rahee\Desktop\Total_annotated_frames"
# print(main_folder)



# main_folder = r"C:\Users\rahee\Desktop\SCripts\Opencv\data_train_1186_val_133_test_14"

# # Define the dataset configuration
# dataset_config = {
#     'train': f'/content/{main_folder}/train/images',
#     'val': f'/content/{main_folder}/val/images',
#     'test': f'/content/{main_folder}/test/images',
#     'nc': 6,  # number of classes
#     'names': ['helmet', 'person', 'vest']
# }

# # Write the configuration to a YAML file
# with open(f'{main_folder}/data.yaml', 'w') as file:
#     yaml.dump(dataset_config, file, default_flow_style=False)

# print("data.yaml file created successfully.")

####################################################################################
# import os
# import random
# from tqdm import tqdm  # Use the standard tqdm
# import shutil
# import yaml

# def train_test_split(path, train_ratio, val_ratio):
#     print("----PROCESS STARTED----")

#     # Get a list of all files in the folder that are images
#     files = [file for file in os.listdir(path) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

#     print(f"--- This folder has a total of {len(files)} images ---")
#     random.seed(42)
#     random.shuffle(files)

#     # Determine the number of images for each set
#     train_size = int(len(files) * train_ratio)
#     val_size = int(len(files) * val_ratio)
#     test_size = len(files) - train_size - val_size
#     print("train_images: ", train_size)
#     print("val_images: ", val_size)
#     print("test_images: ", test_size)

#     # Define the main folder name with train, val, and test sizes
#     main_folder = f"V8_helmet_person_vest_data_{len(files)}_train_{train_size}_val_{val_size}_test_{test_size}"

#     # Define subfolders
#     subfolders = ["train/images", "train/labels", "val/images", "val/labels", "test/images", "test/labels"]

#     # Create the required directories
#     for subfolder in subfolders:
#         os.makedirs(os.path.join(main_folder, subfolder), exist_ok=True)

#     # Copy images to train, validation, and test folders
#     for data_type, start, end, message in [("train", 0, train_size, "Training"),
#                                            ("val", train_size, train_size + val_size, "Validation"),
#                                            ("test", train_size + val_size, None, "Test")]:
#         print(f"--- Processing {message} data ---")
#         for file in tqdm(files[start:end], desc=f"Copying {message} data", unit="files"):
#             if file == 'classes':  # Skip any files named 'classes'
#                 continue
#             # Define source and destination paths for images and labels
#             img_source_path = os.path.join(path, file)
#             label_source_path = os.path.join(path, f"{os.path.splitext(file)[0]}.txt")
#             img_dest_path = os.path.join(main_folder, f"{data_type}/images", file)
#             label_dest_path = os.path.join(main_folder, f"{data_type}/labels", f"{os.path.splitext(file)[0]}.txt")

#             # Copy the image and corresponding label
#             shutil.copy2(img_source_path, img_dest_path)
#             shutil.copy2(label_source_path, label_dest_path)

#         print(f"--- {message} data created with {len(files[start:end])} images ---")

#     print(f"\nData split complete. Files are stored in: {main_folder}")
#     return main_folder


# ############# upper code and below code will run both code upper one for splitting and lower one to making .yaml file################
# path = r'D:\usman Nasir\Unilever Final Version\Unilever Version wise Data\helmet_person_vest\Datasets\V7_Dataset\V7_2839_Datasets_helmet_person_vest_merged_stream1_alerts'
# train_ratio = 0.89
# val_ratio = 0.10

# # Perform the train-test split
# main_folder = train_test_split(path, train_ratio, val_ratio)


# # Define the dataset configuration with three classes
# dataset_config = {
#     'train': f'{main_folder}/train/images',
#     'val': f'{main_folder}/val/images',
#     'test': f'{main_folder}/test/images',
#     'nc': 3,  # number of classes (helmet, person, vest)
#     'names': ['helmet', 'person', 'vest']  # Class names with corresponding indices
# }

# # Write the configuration to a YAML file
# yaml_file_path = os.path.join(main_folder, 'data.yaml')
# with open(yaml_file_path, 'w') as file:
#     yaml.dump(dataset_config, file, default_flow_style=False)

# print(f"data.yaml file created successfully at {yaml_file_path}.")

# print(f"\nData split complete. Files are stored in: {os.path.abspath(main_folder)}")


#################################################################################################
# again upper code is available 


import os
import random
from tqdm import tqdm
from collections import Counter
from PIL import Image
import shutil
import yaml

def train_test_split(path, train_ratio, val_ratio, class_names):
    print("---- PROCESS STARTED ----")

    # Get a list of all files in the folder that are images
    files = [file for file in os.listdir(path) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

    print(f"--- This folder has a total of {len(files)} images ---")
    random.seed(42)
    random.shuffle(files)

    # Determine the number of images for each set
    train_size = int(len(files) * train_ratio)
    val_size = int(len(files) * val_ratio)
    test_size = len(files) - train_size - val_size
    print(f"Train images: {train_size}")
    print(f"Validation images: {val_size}")
    print(f"Test images: {test_size}")

    # Analyze dataset
    empty_txt_count = 0
    object_count = Counter()
    image_sizes = Counter()

    for file in tqdm(files, desc="Analyzing dataset", unit="files"):
        if file.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(path, file)
            txt_path = os.path.join(path, file.replace(os.path.splitext(file)[-1], ".txt"))

            # Check image size
            with Image.open(image_path) as img:
                width, height = img.size
                image_sizes[(width, height)] += 1

            # Check annotation file
            if os.path.exists(txt_path):
                with open(txt_path, 'r') as f:
                    lines = f.readlines()
                    if not lines:  # Empty TXT file
                        empty_txt_count += 1
                    else:  # Annotated file
                        for line in lines:
                            class_id = line.split()[0]
                            object_count[class_id] += 1

    # Define the main folder name with train, val, and test sizes
    main_folder = os.path.join(path, f"V1_ytml9_maingate_{len(files)}_train_{train_size}_val_{val_size}_test_{test_size}")

    # Define subfolders
    subfolders = ["train/images", "train/labels", "val/images", "val/labels", "test/images", "test/labels"]

    # Create the required directories
    for subfolder in subfolders:
        os.makedirs(os.path.join(main_folder, subfolder), exist_ok=True)

    # Copy images to train, validation, and test folders
    for data_type, start, end, message in [("train", 0, train_size, "Training"),
                                           ("val", train_size, train_size + val_size, "Validation"),
                                           ("test", train_size + val_size, None, "Test")]:
        print(f"--- Processing {message} data ---")
        for file in tqdm(files[start:end], desc=f"Copying {message} data", unit="files"):
            if file == 'classes':  # Skip any files named 'classes'
                continue
            # Define source and destination paths for images and labels
            img_source_path = os.path.join(path, file)
            label_source_path = os.path.join(path, f"{os.path.splitext(file)[0]}.txt")
            img_dest_path = os.path.join(main_folder, f"{data_type}/images", file)
            label_dest_path = os.path.join(main_folder, f"{data_type}/labels", f"{os.path.splitext(file)[0]}.txt")

            # Copy the image and corresponding label
            shutil.copy2(img_source_path, img_dest_path)
            if os.path.exists(label_source_path):
                shutil.copy2(label_source_path, label_dest_path)

        print(f"--- {message} data created with {len(files[start:end])} images ---")

    # Generate YAML file
    dataset_config = {
        'train': f'{main_folder}/train/images',
        'val': f'{main_folder}/val/images',
        'test': f'{main_folder}/test/images',
        'nc': len(class_names),  # number of classes
        'names': class_names     # Class names with corresponding indices
    }

    yaml_file_path = os.path.join(main_folder, 'data.yaml')
    with open(yaml_file_path, 'w') as file:
        yaml.dump(dataset_config, file, default_flow_style=False)

    print(f"data.yaml file created successfully at {yaml_file_path}.")

    # Print analysis results
    print("==== Dataset Analysis Results ====")
    print(f"Total images: {len(files)}")
    print(f"Background images (empty TXT): {empty_txt_count}")
    annotated_images_count = len(files) - empty_txt_count
    print(f"Annotated images: {annotated_images_count}")
    print("Object counts:")
    for class_id, count in object_count.items():
        class_name = class_names[int(class_id)] if int(class_id) < len(class_names) else "unknown"
        print(f"  {class_name} ({class_id}): {count}")
    print("Image size distribution:")
    for size, count in image_sizes.items():
        print(f"  {size[0]}x{size[1]}: {count}")

    print(f"\nData split complete. Files are stored in: {main_folder}")
    return main_folder

####
# Path to the dataset
dataset_path = r'C:\Users\rahee\Desktop\YTML9_Project\Annotated_data\verified_and_checked_annotated_data\V1_main_gate_ent_exit'

# Ratios for splitting the dataset
train_ratio = 0.89
val_ratio = 0.10

# List of class names (update as needed)
class_names = ['loadingvehicle']

# Perform the train-test split
train_test_split(dataset_path, train_ratio, val_ratio, class_names)
