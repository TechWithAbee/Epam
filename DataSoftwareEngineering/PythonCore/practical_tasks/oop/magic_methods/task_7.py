# Create a context manager LogFile inherited from ContextDecorator
# which adds text lines into a log file.
# Every text line must contain the following information:

# date and time when started (Start:)
# execution time (Run:)
# error information (in the code wrapped by context manager) (An error occured:)


# The trace format example when no errors occurred:


# Start: 2021-03-22 12:38:24.757637 | Run: 0:00:00.000054 | An error occurred: None



# The example in case of ZeroDivisionError exception


# Start: 2021-03-22 12:38:24.758463 | Run: 0:00:00.000024 | An error occurred: division by zero


# The log file name is passed as an argument to text manager constructor.
# For example:

# @LogFile('my_trace.log')
# def some_func():
#     ...


# The log file has to be open in append mode to allow reopening existing file and adding
# new information into this file if the same name is pointed.
# When an exception is happened the error message has to be put in An error occured: into the log and reraised upper.
# Use open builtin function to open the log file.

import datetime
from contextlib import ContextDecorator

class LogFile(ContextDecorator):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name
    
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time
        error_message = str(exc_val) if exc_val else "None"
        
        log_message = (
            f"Start: {self.start_time} | "
            f"Run: {execution_time} | "
            f"An error occurred: {error_message}\n"
        )
        
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(log_message)
        
        # Reraise the exception if one occurred
        if exc_type:
            return False  # This will re-raise the exception