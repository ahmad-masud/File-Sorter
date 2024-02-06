import os
import sys
import shutil
import unittest
import tempfile
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from sorters import sort_by_type

class TestSortByType(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        # Create sample files of different types
        self.files = ['test.txt', 'example.png', 'demo.pdf']
        for f in self.files:
            open(os.path.join(self.test_dir, f), 'a').close()  # Create an empty file

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_sort_by_type(self):
        # Call the function to test
        sort_by_type(self.test_dir)

        # Check if files are sorted into correct directories
        for f in self.files:
            file_type = f.split('.')[-1]
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, file_type, f)))

    def test_empty_directory(self):
        # Test the function with an empty directory
        empty_dir = os.path.join(self.test_dir, "empty")
        os.makedirs(empty_dir)
        self.assertTrue(sort_by_type(empty_dir))
        self.assertEqual(len(os.listdir(empty_dir)), 0, "The directory should be empty")

if __name__ == '__main__':
    unittest.main()
