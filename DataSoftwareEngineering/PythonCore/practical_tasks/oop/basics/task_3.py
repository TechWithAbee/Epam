# Implement a Counter class that optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."
# Implement two methods: "increment" and "get"
# Example:

# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43

# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2

# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# Maximal value is reached.
# >>> c.get()
# 43


class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop
        self.current = start
    
    def increment(self):
        if self.stop is not None and self.current == self.stop:
            print("The maximal value is reached.")
        else:
            self.current += 1
    
    def get(self):
        return self.current
    
c = Counter(start=42)
c.increment()
print(c.get()) # 43

c = Counter(start=42, stop=43)
c.increment()
print(c.get()) # 43

c.increment()
print(c.get()) # 43