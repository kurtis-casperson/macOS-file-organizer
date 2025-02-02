import os
import shutil


source_directory = os.path.expanduser("~/Downloads")
destination_directory = os.path.expanduser("~/Documents")


category_keywords = {
    "Resume": ["resume", "cover"],
    "Work": ["project", "report", "meeting"],
    "Personal": ["vacation", "birthday", "shopping"],
    "Images": [".jpg", ".png", ".jpeg", ".heic"],
}


def moveFiles():
    """Moves all files from the source directory to the destination directory."""
    # verify that the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # create file paths and move files from source to destination
    for file in os.listdir(source_directory):
        if file == ".DS_Store":
            continue
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(destination_directory, file)

        if os.path.isfile(source_path):
            shutil.move(source_path, destination_path)

        print(f"Moved files to {destination_directory}")


def categorizeFiles():
    """Use the category keywords to create new folder paths if they do not exist"""
    for category in category_keywords.keys():
        folder_path = os.path.join(destination_directory, category)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"created the {category} folder")

    # loop through files and categorize them
    for file in os.listdir(destination_directory):
        new_path = os.path.join(destination_directory, file)

        if not os.path.isfile(new_path):
            continue

        file_category = None
        for category, keywords in category_keywords.items():
            if any(keyword in file.lower() for keyword in keywords):
                file_category = category
                break

        if file_category:
            destination_folder = os.path.join(destination_directory, file_category)
            destination_path = os.path.join(destination_folder, file)

            shutil.move(new_path, destination_path)
            print(f"Moved {file} to {destination_folder}")


def manageFilesWorkFlow():
    moveFiles()
    categorizeFiles()


manageFilesWorkFlow()
