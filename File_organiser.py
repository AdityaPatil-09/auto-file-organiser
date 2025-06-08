import os      
import shutil  

# Step 1: Get the path to your Downloads folder
# This works on Windows, Mac, and Linux
downloads_path = os.path.expanduser("~/Downloads")

#  Step 2: Define which file types go into which folders
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Scripts": [".py", ".js", ".sh"],
    "Others": []  # Files that don't match any type will go here
}

# Step 3: Go through everything in the Downloads folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)  # Full path to the file

    # Only work with actual files, skip folders
    if os.path.isfile(file_path):
        moved = False  # Flag to check if the file has been moved

        # Step 4: Check which folder the file belongs to
        for folder, extensions in file_types.items():
            # Does the filename end with one of the extensions in this folder?
            if any(filename.lower().endswith(ext) for ext in extensions):
                # Create the folder if it doesn't exist
                target_folder = os.path.join(downloads_path, folder)
                os.makedirs(target_folder, exist_ok=True)

                # Move the file into the target folder
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {folder}")
                moved = True
                break  # No need to check other folders

        # Step 5: If no folder matched, move to 'Others'
        if not moved:
            other_folder = os.path.join(downloads_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Others")
print("\n All files are moved, Thanks for using this script")