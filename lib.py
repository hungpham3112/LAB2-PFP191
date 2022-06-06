import math
from typing import Iterable


class Question:
    def __init__(self, name):
        self.name = name

    def take_integer_input(self, prompt="", num: int = 1) -> Iterable[int]:
        """
        take `num` element and return iterable
        E.g:
        ```
        >>> object = take_integer_input(3)
        Enter 3 number(s): 1 2 3
        >>> tuple(object)
        (1, 2, 3)
        ```
        """
        print(prompt, end=", ")
        return map(int, input(f"enter {num} number(s): ").split())


class Question1(Question):
    def __init__(self):
        pass

    def int_input_less_than_five(self):
        number = int(input("Type your number greater than 5: "))
        return number if number > 5 else self.int_input_less_than_five()

    def s1(self, number):
        return sum(range(1, number + 1))

    def s2(self, number):
        return math.factorial(number)

    def s3(self, number):
        return sum((1 / n for n in range(1, number + 1)))

    def isprime(self, number):
        """Returns True if number is prime."""
        if number == 2:
            return True
        if number == 3:
            return True
        if number % 2 == 0:
            return False
        if number % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= number:
            if number % i == 0:
                return False

            i += w
            w = 6 - w

        return True


class Question2(Question):
    def __init__(self):
        pass

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def common_prime_divisors(self, a, b):
        return (i for i in range(1, min(a, b) + 1) if a % i == b % i == 0)


class Question3(Question):
    def __init__(self):
        pass


class Question4(Question):
    def __init__(self):
        pass

    def palindrome(self, m, n):
        """
        Display all palindrome in the range of [m, n] where m < n
        """
        return [
            number for number in range(m, n + 1) if str(number) == str(number)[::-1]
        ]
