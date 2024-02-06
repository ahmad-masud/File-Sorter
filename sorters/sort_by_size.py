import os
import shutil

def sort_by_size(directory) -> bool:
    """
    Sort files in a directory by their size.
    
    :param directory: The directory to sort.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        # Sort files in a directory by their size
        for item in os.listdir(directory):
            # Check if item is a file
            file_path = os.path.join(directory, item)
            if os.path.isfile(file_path):
                # Check the file size
                size = os.path.getsize(file_path)
                if size < 1024 * 1024:  # smaller than 1MB
                    size_folder = 'Small'
                elif size < 1024 * 1024 * 10:  # smaller than 10MB
                    size_folder = 'Medium'
                else:
                    size_folder = 'Large'
                # Create a new directory for the file size
                new_dir = os.path.join(directory, size_folder)
                # Move the file to the new directory
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                shutil.move(file_path, os.path.join(new_dir, item))
        return True  # Return True if the operation completes successfully
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Return False if an error occurs
