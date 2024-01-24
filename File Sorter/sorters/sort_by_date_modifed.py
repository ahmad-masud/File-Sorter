import os
import shutil
from datetime import datetime

def sort_by_date_modified(directory):
    for item in os.listdir(directory):
        file_path = os.path.join(directory, item)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            new_dir = os.path.join(directory, date)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(file_path, os.path.join(new_dir, item))
