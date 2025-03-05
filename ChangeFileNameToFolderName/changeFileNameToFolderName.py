import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import time

def get_modified_date(file_path):
    # Get the last modified time and format it to dd/mm/yyyy
    timestamp = os.path.getmtime(file_path)
    return time.strftime('%d-%m-%Y', time.localtime(timestamp))

# Hide the main Tkinter window
root = tk.Tk()
root.withdraw()

# Open folder selection dialog
folder_path = filedialog.askdirectory()

if folder_path:
    # Get the folder name from the selected path
    folder_name = os.path.basename(folder_path)

    # Get today's date in "dd-mm-yyyy" format
    current_date = datetime.today().strftime("%d-%m-%Y")

    print(f"Selected Folder: {folder_path}\n")

    # Loop through all files in the folder and rename them
    for index, file_name in enumerate(os.listdir(folder_path), start=1):
        print(file_name)
        file_path = os.path.join(folder_path, file_name)

        # Ensure it's a file (not a folder)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1]  # Extract file extension
            print(f"index = {index}")
            new_name = f"{get_modified_date(file_path)} {folder_name} {index:03d}{file_extension}"  # Format name
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(file_path, new_path)
            print(f"Renamed: {file_name} -> {new_name}")
