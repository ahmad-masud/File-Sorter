import os
import shutil
from datetime import datetime

def sort_by_date_modified(directory) -> bool:
    """
    Sort files in a directory by the date they were modified.
    
    :param directory: The directory to sort.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        # Sort files in a directory by the date they were modified
        for item in os.listdir(directory):
            # Check if item is a file
            file_path = os.path.join(directory, item)
            if os.path.isfile(file_path):
                # Get the file modification time
                mod_time = os.path.getmtime(file_path)
                date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
                # Create a new directory for the date
                new_dir = os.path.join(directory, date)
                # Move the file to the new directory
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                shutil.move(file_path, os.path.join(new_dir, item))
        return True  # Return True if the operation completes successfully
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Return False if an error occurs
