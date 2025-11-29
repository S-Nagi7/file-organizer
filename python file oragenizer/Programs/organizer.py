import os
import shutil

def organize_files(directory):
    """
    Organizes files in the specified directory into category folders
    based on file extensions.
    """
    # Define file type categories and their corresponding extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".ico", ".webp"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".md"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Programs": [".exe", ".msi", ".bat", ".sh", ".py", ".js", ".html", ".css", ".java", ".cpp"],
        "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    }
    
    # Check if the provided directory path exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    print(f"Scanning '{directory}'...")
    
    # Counters for statistics
    moved_count = 0
    errors_count = 0

    # Iterate over all items in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories, only process files
        if os.path.isdir(file_path):
            continue
            
        # Determine the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()
        
        # Find the category for the file
        category = "Others"
        for type_name, extensions in file_types.items():
            if file_extension in extensions:
                category = type_name
                break
        
        # Define the destination folder path
        category_path = os.path.join(directory, category)
        
        # Create the category folder if it doesn't exist
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created folder: {category}")
            
        # Define the destination file path
        destination_path = os.path.join(category_path, filename)
        
        # Move the file
        try:
            # Check if file already exists in destination to avoid overwrite
            if os.path.exists(destination_path):
                print(f"Skipped: {filename} (already exists in {category})")
            else:
                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} -> {category}/")
                moved_count += 1
        except Exception as e:
            print(f"Error moving {filename}: {e}")
            errors_count += 1

    print("-" * 30)
    print(f"Organization complete!")
    print(f"Files moved: {moved_count}")
    print(f"Errors encountered: {errors_count}")

if __name__ == "__main__":
    print("--- File Organizer Automation Tool ---")
    target_folder = input("Enter the folder path to organize: ").strip()
    
    # Remove quotes if user dragged and dropped folder
    if target_folder.startswith('"') and target_folder.endswith('"'):
        target_folder = target_folder[1:-1]
        
    if target_folder:
        organize_files(target_folder)
    else:
        print("No folder path provided.")