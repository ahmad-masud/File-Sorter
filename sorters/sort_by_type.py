import os
import shutil

def sort_by_type(directory) -> bool:
    """
    Sort files in a directory by their type.
    
    :param directory: The directory to sort.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        # Sort files in a directory by their type
        for item in os.listdir(directory):
            # Check if item is a file
            if os.path.isfile(os.path.join(directory, item)):
                # Get the file type
                file_type = item.split('.')[-1]
                # Create a new directory for the file type
                new_dir = os.path.join(directory, file_type)
                # Move the file to the new directory
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                shutil.move(os.path.join(directory, item), os.path.join(new_dir, item))
        return True  # Explicitly return True if the function completes successfully
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Return False if an error occurs
