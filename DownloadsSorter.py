import os
import shutil

downloads_folder = os.path.join(os.path.expanduser("~"),"Downloads")

extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",

    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".exe": "Installers",
    ".msi": "Installers",

    ".c": "C",
    ".h": "C",
    ".cpp": "Cpp",
    ".hpp": "Cpp",
    ".java": "Java",
    ".jar": "Java",
    ".py": "Python",
    ".ipynb": "Python",
    ".html": "Web",
    ".css": "Web",
    ".js": "Web",
    ".ts": "Web",
}

for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]
            folder_path = os.path.join(downloads_folder, folder_name)   #C:\Users\X\Downloads\Images

            os.makedirs(folder_path, exist_ok=True) #create the folder if it doesn't exist

            destination_path = os.path.join(folder_path, filename)  #C:\Users\X\Downloads\Images\Urlaub.jpg
            
            if os.path.exists(destination_path):
                print(f"Skipped {filename}: already exists in {folder_name}")
            else:
                shutil.move(file_path, destination_path)   # move(von_wo, nach_wo)
                print(f"Successfully moved {filename} to {folder_name}")

        else:
            print(f"{filename} is an unknown datatype") 
            
    else:
        print(f"{filename} already a folder")    