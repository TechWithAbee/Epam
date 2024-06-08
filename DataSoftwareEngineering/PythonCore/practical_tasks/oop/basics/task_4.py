# Implement a custom dictionary that will memorize the 5 latest changed keys.
# Using method "get_history" return these keys.
# Example:

# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]

from collections import deque

class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data
        self.history = deque(maxlen=5)
    
    def set_value(self, key, value):
        self.data[key] = value
        self.history.append(key)

    def get_history(self):
        return list(self.history)
    
d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history()) # ["bar"]