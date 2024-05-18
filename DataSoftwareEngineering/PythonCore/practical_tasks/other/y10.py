# Description
# Implement class Currency and inherited classes Euro, Dollar, and Pound. The course is 1 EUR == 2 USD == 100 GBP

# You need to implement the following methods:

# course – a classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}

#   >>> print(
#       f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
#       f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
#       f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
#   )
#   Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
#   Dollar.course(Pound) ==> 50.0 GBP for 1 USD
#   Pound.course(Euro)   ==> 0.01 EUR for 1 GBP
# to_currency – this method transforms the currency from one currency to another. The method should return an instance of a required currency.

#   >>> e = Euro(100)
#   >>> r = Pound(100)
#   >>> d = Dollar(200)
  
#   >>> print(
#       f"e = {e}\n"
#       f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
#       f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
#       f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
#   )
#   e = 100 EUR
#   e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
#   e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
#   e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed
  
#   >>> print(
#       f"r = {r}\n"
#       f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
#       f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
#       f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
#   )
#   r = 100 GBP
#   r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
#   r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
#   r.to_currency(Pound) = 100.0 GBP  # Pound instance printed
# + - returns an instance of a new value

#   >>> e = Euro(100)
#   >>> r = Pound(100)
#   >>> d = Dollar(200)
#   >>> print(
#       f"e + r  =>  {e + r}\n"
#       f"r + d  =>  {r + d}\n"
#       f"d + e  =>  {d + e}\n"
#   )
#   e + r  =>  101.0 EUR  # Euro instance printed
#   r + d  =>  10100.0 GBP  # Pound instance printed
#   d + e  =>  400.0 USD  # Dollar instance printed
# other comparison methods: > < ==

# Please pay attention to the examples. Your code should work exactly the same.


from __future__ import annotations
from typing import Type

class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    exchange_rates = {
        'Euro': {'Euro': 1, 'Dollar': 2, 'Pound': 100},
        'Dollar': {'Euro': 0.5, 'Dollar': 1, 'Pound': 50},
        'Pound': {'Euro': 0.01, 'Dollar': 0.02, 'Pound': 1}
    }

    symbols = {
        'Euro': 'EUR',
        'Dollar': 'USD',
        'Pound': 'GBP'
    }

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        rate = cls.exchange_rates[cls.__name__][other_cls.__name__]
        return f"{rate} {cls.symbols[other_cls.__name__]} for 1 {cls.symbols[cls.__name__]}"

    def to_currency(self, other_cls: Type[Currency]):
        rate = self.exchange_rates[self.__class__.__name__][other_cls.__name__]
        return other_cls(self.value * rate)

    def __str__(self):
        return f"{self.value} {self.symbols[self.__class__.__name__]}"

    def __add__(self, other: Currency):
        if not isinstance(other, Currency):
            return NotImplemented
        value_in_self_currency = other.to_currency(self.__class__).value
        return self.__class__(self.value + value_in_self_currency)

    def __eq__(self, other: Currency):
        if not isinstance(other, Currency):
            return NotImplemented
        return self.value == other.to_currency(self.__class__).value

    def __lt__(self, other: Currency):
        if not isinstance(other, Currency):
            return NotImplemented
        return self.value < other.to_currency(self.__class__).value

    def __gt__(self, other: Currency):
        if not isinstance(other, Currency):
            return NotImplemented
        return self.value > other.to_currency(self.__class__).value


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass

# Test cases
if __name__ == "__main__":
    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)

    print(
        f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
        f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
        f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
    )

    print(
        f"e = {e}\n"
        f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
        f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
        f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
    )

    print(
        f"r = {r}\n"
        f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
        f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
        f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
    )

    print(
        f"e + r  =>  {e + r}\n"
        f"r + d  =>  {r + d}\n"
        f"d + e  =>  {d + e}\n"
    )
