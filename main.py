from lib import Question, Question1, Question2, Question3, Question4


def main():
    question1 = Question1()
    question2 = Question2()
    question3 = Question3()
    question4 = Question4()

    print(
        """
##################################
########## Question 1 ############
##################################
          """
    )
    number1 = question1.int_input_less_than_five()
    print("S1: ", question1.s1(number1))
    print("S2: ", question1.s2(number1))
    print("S3: ", question1.s3(number1))
    number1 = question1.int_input_less_than_five()
    print(f"{number1} {'is prime' if question1.isprime(number1) else 'is not prime' }")

    print(
        """
##################################
########## Question 2 ############
##################################
          """
    )
    a, b = question2.take_integer_input("Type 2 integer numbers m and n", 2)
    print(
        f"All common prime divisors of {a} and {b}: ",
        list(question2.common_prime_divisors(a, b)),
    )
    print(f"The GCD of {a} and {b} is", question2.gcd(a, b))
    print(f"The LCM of {a} and {b} is", question2.lcm(a, b))

    print(
        """
##################################
########## Question 3 ############
##################################
          """
    )
    while True:
        try:
            (number3,) = question3.take_integer_input(
                "Input an integer number n (will check input validation)"
            )
            break
        except ValueError as e:
            print("Invalid input. Please type integer!!!")
            continue
    print(f"n in binary format: {format(number3, 'b')}")
    (number3,) = question3.take_integer_input(
        "Input an integer number n (will not check input validation)"
    )
    print(
        f"The sum of all digits of {number3} is:",
        sum(map(int, tuple(str(number3)))),
    )

    print(f"The reverse version of {number3} is:", int(str(number3)[::-1]))
    print(
        """
##################################
########## Question 4 ############
##################################
          """
    )
    m, n = question4.take_integer_input("Type 2 number m and n where m < n", 2)
    print(f"All palindrome in [m, n]:", question4.palindrome(m, n))


if __name__ == "__main__":
    question = Question("Hung")
    print(repr(Question("Hung")))
    #  main()
