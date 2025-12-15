import os
import shutil

source_folder = r"PathHere"

categories = {
    'Imgs': ['.png', '.jpg', '.gif'],
    'Documentos': ['.pdf', '.xml'],
    'Instaladores': ['.exe', '.msi']
}

# Create destination folders if they do not exist
for category in categories:
    destination_path = os.path.join(source_folder, category)
    os.makedirs(destination_path, exist_ok=True)

# Loop through files in the source folder
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    # Ignore directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, extension = os.path.splitext(file)
    extension = extension.lower()

    # Check the file category
    for category, extensions in categories.items():
        if extension in extensions:

            # Set destination path
            destination = os.path.join(source_folder, category, file)

            if os.path.exists(destination):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination):
                    destination = os.path.join(source_folder, category, f"{base}_{counter}{ext}")
                    counter += 1

            # Move the file
            shutil.move(file_path, destination)
            print(f"Movido {file} para {category}")
            break