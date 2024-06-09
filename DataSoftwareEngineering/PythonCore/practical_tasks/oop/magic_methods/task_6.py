# Create a context manager Cd which changes the current directory to pointed one.
# For example:

# with Cd('/home')


# When entering the context you need to save the previous directory and when you exit you need to restore it.
# During context manager initialization check that the passed directory is a directory and exists.
# If the passed directory is not a directory or does not exist raise ValueError.
# Use the following functions from the os module: getcwd, chdir, path.isdir


import os

class Cd:
    def __init__(self, new_path):
        self.new_path = new_path
        if not os.path.isdir(self.new_path):
            raise ValueError(f"{self.new_path} is not a valid directory or does not exist.")

    def __enter__(self):
        # Save the current working directory
        self.original_path = os.getcwd()
        print(self.original_path)
        # Change to the new directory
        os.chdir(self.new_path)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Change back to the original directory
        os.chdir(self.original_path)

# example
with Cd('/home'):
    print(os.getcwd()) # /home