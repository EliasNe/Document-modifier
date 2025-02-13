import os
import shutil
from datetime import datetime

# Folder path containing the files
folder_path = r"C:\Users\EliasBlanksvärd\OneDrive - Uper Group\Skrivbordet\testmap2"


def newfolder(folder_path):

# Loop through each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

    # Skip directories, only process files
        if os.path.isfile(file_path):
        
        # Generate today's date as YYYYMMDDHHMMSS
            today_str = datetime.now().strftime("%Y%m%d%H%M%S")

            new_filen_name = file_name[15:]
        # Rename the file using today's date
            new_name = f"{today_str}_{new_filen_name}"

        # save it as a utf-8
            new_name = new_name.encode("utf-8", "ignore").decode("utf-8")
            
        # Define new file path
            new_path = os.path.join(folder_path, new_name)

        # Rename the file
            shutil.move(file_path, new_path)
        
        print(f"Renamed: {file_name} -> {new_name}")






print(newfolder(folder_path))



   
        




