import os
import shutil

def sort_by_type(directory):
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            file_type = item.split('.')[-1]
            new_dir = os.path.join(directory, file_type)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(os.path.join(directory, item), os.path.join(new_dir, item))
