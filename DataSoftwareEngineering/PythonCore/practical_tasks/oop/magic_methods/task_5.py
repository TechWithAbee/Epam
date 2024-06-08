# Create a context manager TempDir (Use Context Manager protocol - methods __enter__, __exit__):

# When entering the context, a new temporary directory is created with random, unique name.
# Use os.mkdir to create the directory.
# Until exiting this context the new created directory becomes current one and all actions are executed
# in scope of this new directory.
# When exiting this context, the temporary directory is removed with all files in it.
# Use rmtree from shutil to remove whole directory.
# The new working directory becomes the same as before entering context.

import os
import shutil
import uuid

class TempDir:
    def __enter__(self):
        self.original_dir = os.getcwd()
        self.temp_dir = os.path.join(self.original_dir, str(uuid.uuid4()))
        os.mkdir(self.temp_dir)
        os.chdir(self.temp_dir)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        shutil.rmtree(self.temp_dir)
