# Functions. Decorators. Functions Arguments. Task 1.
# We have a list of dictionaries:

# friends = [
#     {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
#     {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
# ]
# Create functions query, select, and field_filter to work with lists similar to friends. 
# Stubs for these functions are already created.

# Example:

# >>> result = query(
#     friends,
#     select('name', 'gender', 'sport'),
#     field_filter('sport', *('Basketball', 'Volleyball')),
#     field_filter('gender', *('male',)),
# )
# >>> result
# [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}]
# These functions have to provide a possibility to select necessary columns and make filtering by these columns.

# Do not forget the documentation for each function!

from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    # Apply filters first
    for f in filters:
        data = f(data)
    # Apply selector last
    return selector(data)


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def select_columns(data: DataType) -> DataType:
        return [{col: row[col] for col in columns if col in row} for row in data]
    return select_columns


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def filter_column(data: DataType) -> DataType:
        return [row for row in data if row.get(column) in values]
    return filter_column


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    print('value:', value)
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()

