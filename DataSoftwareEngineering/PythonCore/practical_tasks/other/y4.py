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

# Example usage
@LogFile('my_trace.log')
def some_func():
    print("Executing some_func()")
    # Simulate an error
    # raise ZeroDivisionError("division by zero")
    
@LogFile('my_trace.log')
def another_func():
    print("Executing another_func()")
    # Normal execution

# Running the functions
some_func()
another_func()
