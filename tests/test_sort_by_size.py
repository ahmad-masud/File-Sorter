import os
import sys
import shutil
import unittest
import tempfile
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from sorters import sort_by_size

class TestSortBySize(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        # Create sample files of different sizes
        self.files = {
            'small.txt': 512,  # 512 bytes
            'medium.txt': 5 * 1024 * 1024,  # 5 MB
            'large.txt': 15 * 1024 * 1024,  # 15 MB
        }
        for filename, size in self.files.items():
            file_path = os.path.join(self.test_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(b'\0' * size)

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_sort_by_size(self):
        # Call the function to test
        sort_by_size(self.test_dir)

        # Check if files are sorted into correct directories
        for filename, _ in self.files.items():
            if 'small' in filename:
                self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Small', filename)))
            elif 'medium' in filename:
                self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Medium', filename)))
            elif 'large' in filename:
                self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Large', filename)))

    def test_empty_directory(self):
        # Test the function with an empty directory
        empty_dir = os.path.join(self.test_dir, "empty")
        os.makedirs(empty_dir)
        self.assertTrue(sort_by_size(empty_dir))
        self.assertEqual(len(os.listdir(empty_dir)), 0, "The directory should be empty")

if __name__ == '__main__':
    unittest.main()
