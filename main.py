import hashlib
import os


def calculate_image_hashes(folder_path):
    hash_dict = {}

    # Iterate over all files in the folder and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Calculate the SHA256 hash for each image in the file
            if file.endswith((".jpg", ".jpeg", ".png")):
                try:
                    with open(file_path, "rb") as f:
                        image_data = f.read()
                        sha256_hash = hashlib.sha256(image_data).hexdigest()

                        # Update the dictionary with the file path and hash
                        hash_dict.setdefault(sha256_hash, []).append(file_path)
                except IOError:
                    print(f"Error reading file: {file_path}")

    return hash_dict


# Example usage
folder_path = input("Please enter the folder path: ")
# folder_path = "../../../iCloudPhotos/Photos"
# folder_path = "..\..\..\OneDrive\Pictures"
image_hash_dict = calculate_image_hashes(folder_path)

# Print the dictionary that maps the hash to the file paths
for hash_value, file_paths in image_hash_dict.items():
    print(f"Hash: {hash_value}")
    print("File paths:")
    for file_path in file_paths:
        print(file_path)
    print()
