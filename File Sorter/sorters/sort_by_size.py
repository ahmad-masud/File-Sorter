import os
import shutil

def sort_by_size(directory):
    for item in os.listdir(directory):
        file_path = os.path.join(directory, item)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            if size < 1024 * 1024:  # smaller than 1MB
                size_folder = 'Small'
            elif size < 1024 * 1024 * 10:  # smaller than 10MB
                size_folder = 'Medium'
            else:
                size_folder = 'Large'
            new_dir = os.path.join(directory, size_folder)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(file_path, os.path.join(new_dir, item))
