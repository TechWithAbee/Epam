# Create a context manager TempDir (Use Context Manager protocol - methods __enter__, __exit__):

# When entering the context, a new temporary directory is created with a random, unique name. Use os.mkdir to create the directory.
# Until exiting this context, the new created directory becomes the current one, and all actions are executed in the scope of this new directory.
# When exiting this context, the temporary directory is removed with all files in it. Use rmtree from shutil to remove the whole directory.
# The new working directory becomes the same as before entering the context.


import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from unittest import TestCase

class TempDir:
    def __enter__(self):
        self.original_dir = os.getcwd()
        self.temp_dir = tempfile.mkdtemp()
        os.chdir(self.temp_dir)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        shutil.rmtree(self.temp_dir)

class TestTempDir(TestCase):
    @patch('os.getcwd', MagicMock(return_value='/home/user'))  # Mock os.getcwd
    @patch('tempfile.mkdtemp', MagicMock(return_value='/tmp/my_temp_dir'))  # Mock tempfile.mkdtemp
    @patch('os.chdir')  # Mock os.chdir
    @patch('shutil.rmtree')  # Mock shutil.rmtree
    def test_tempdir(self, mock_rmtree, mock_chdir, mock_mkdtemp, mock_getcwd):
        with TempDir() as temp_dir:
            # Check if os.chdir was called correctly
            mock_chdir.assert_called_once_with('/tmp/my_temp_dir')
            # Check if the returned value is correct
            self.assertEqual(temp_dir.temp_dir, '/tmp/my_temp_dir')
        # Check if shutil.rmtree was called correctly
        mock_rmtree.assert_called_once_with('/tmp/my_temp_dir') 

# Example Usage (Outside of the test)
with TempDir() as temp:
    print(f"Current working directory: {os.getcwd()}")
    with open("test.txt", "w") as f:
        f.write("Test file content")
    print(f"Files in temporary directory: {os.listdir('.')}")
print(f"Restored working directory: {os.getcwd()}") 