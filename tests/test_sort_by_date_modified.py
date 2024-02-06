import os
import sys
import shutil
import unittest
import tempfile
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path(__file__).parent.parent))

from sorters import sort_by_date_modified

class TestSortByDateModified(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        # Create sample files with different modification dates
        self.files = ['recent.txt', 'old.txt']
        now = datetime.now()
        old = now.replace(year=now.year - 1)
        for f in self.files:
            file_path = os.path.join(self.test_dir, f)
            with open(file_path, 'w') as file:
                file.write("Sample content")
            # Set the modification date to now for recent.txt and last year for old.txt
            os.utime(file_path, (datetime.timestamp(old) if f == 'old.txt' else datetime.timestamp(now),) * 2)

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

def test_sort_by_date_modified(self):
    # Call the function to test
    sort_by_date_modified(self.test_dir)

    # Check if files are sorted into correct directories based on their modification date
    for f in self.files:
        # Find the expected directory based on modification date
        file_path = os.path.join(self.test_dir, f)
        mod_time = os.path.getmtime(file_path)
        date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
        new_file_path = os.path.join(self.test_dir, date_folder, f)
        
        # Ensure the file has been moved to the new directory
        self.assertTrue(os.path.exists(new_file_path))


    def test_empty_directory(self):
        # Test the function with an empty directory
        empty_dir = os.path.join(self.test_dir, "empty")
        os.makedirs(empty_dir)
        self.assertTrue(sort_by_date_modified(empty_dir))
        self.assertEqual(len(os.listdir(empty_dir)), 0, "The directory should be empty")

if __name__ == '__main__':
    unittest.main()
