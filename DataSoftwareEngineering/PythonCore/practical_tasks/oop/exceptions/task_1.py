# Implement a Pagination class helpful to arrange text on pages and list content on the given page.
# The class should take in a text and a positive integer which indicate 
# how many symbols will be allowed per page (take spaces into account as well).
# You need to be able to get the number of whole symbols in the text, 
# get the number of pages that came out and the method that accepts the page number, 
# and return the number of symbols on this page. If the provided number of the page is missing raise exception with message "Invalid index. Page is missing".
# Implement searching/filtering pages by symbols/words and displaying pages with all the symbols on it. 
# If the provided symbols/words are missing raise exception with message "'<symbol/word>' is missing on the pages".
# If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.
# Pages indexing starts with 0.
# Example:

# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19

# >>> pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# >>> pages.find_page('Your')
# [0]
# >>> pages.find_page('e')
# [1, 3]
# >>> pages.find_page('beautiful')
# [1, 2]
# >>> pages.find_page('great')
# Exception: 'great' is missing on the pages
# >>> pages.display_page(0)
# 'Your '

import math
from typing import List

class Pagination:
    def __init__(self, data: str, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page

    @property
    def page_count(self) -> int:
        return math.ceil(len(self.data) / self.items_on_page)

    @property
    def item_count(self) -> int:
        return len(self.data)

    def count_items_on_page(self, page_number: int) -> int:
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing.")
        
        start_index = page_number * self.items_on_page
        end_index = start_index + self.items_on_page
        
        return len(self.data[start_index:end_index])

    def find_page(self, query: str) -> List[int]:
        if query not in self.data:
            raise Exception(f"'{query}' is missing on the pages")
        
        pages = []
        full_text = self.data
        query_len = len(query)
        
        for i in range(len(full_text) - query_len + 1):
            if full_text[i:i + query_len] == query:
                start_page = i // self.items_on_page
                end_page = (i + query_len - 1) // self.items_on_page
                for page in range(start_page, end_page + 1):
                    if page not in pages:
                        pages.append(page)

        if not pages:
            raise Exception(f"'{query}' is missing on the pages")
        
        return pages

    def display_page(self, page_number: int) -> str:
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing.")
        
        start_index = page_number * self.items_on_page
        end_index = start_index + self.items_on_page
        
        return self.data[start_index:end_index]
    

pages = Pagination('Your beautiful text', 5)
print(pages.page_count)

print(pages.item_count)

print(pages.count_items_on_page(0))

print(pages.count_items_on_page(3))

print(pages.count_items_on_page(2))

print(pages.find_page('Your'))

print(pages.find_page('e'))

print(pages.find_page('beautiful'))

# print(pages.find_page('great'))

for i in range(pages.page_count):
    print(pages.display_page(i), end="")

print('\n')
print(pages.display_page(3))