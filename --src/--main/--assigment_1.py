''' ==========================================
== Written by..: Manuel Puello            ====
== Date Written: Jan 26                   ====
== Purpose.....: cot-4500 / Assignment 1  ====
==============================================
'''

#set all the parameters such as the mantisa and exponent.
import math
def assigment_1():
    sign = 0
    exponent = 10000000111
    index, i = 0, 0

    while(exponent != 0):
        index += (exponent % 10) * pow(2, i)
        exponent //= 10
        i += 1

    fraction = str(1110101110010000000000000000000000000000000)
    f = 0
    i = 1

    for item in fraction:
        f += int(item) * (0.5 ** i)
        i += 1

#1 Use double precision, calculate the resulting values (format to 5 decimal places)
    value = ((-1) ** sign) * (2 ** (index - 1023)) * (1 + f)
    resulting_value = value

    print("{:.5f}".format(value))
    print("\n")

#2 Repeat above part using three-digit chopping arithmetic
    value *= (10 ** -3)

    print((math.floor(value * 1000)) / 1000)
    print("\n")

#3 Repeat part 1 using three-digit rounding arithmetic
    value += 0.0005

    print(round(value, ndigits=3))
    print("\n")

#4 Compute the absolute and relative error with the exact value from question 1 and its 3 digit
# rounding
    def absolute_error(precise: float, approx: float):
        return abs((precise - approx))

    def relative_error(precise: float, approx: float):
        return abs((absolute_error(precise, approx)) / precise)

    print(absolute_error(resulting_value, round(resulting_value, 0)))
    print(relative_error(resulting_value, round(resulting_value, 0)))
    print("\n")

#5 From infinite series -1 ** k (x ** k) / (k **3) from 1 to infinite,
# what is the minimum number of terms needed to computer f(1) with error < 10-4?
    def infinite_serie(x, k: int):
        return((-1) ** k) * ((x ** k) / (k ** 3))
    min_error = 1e-4
    current_iteration = 1
    while(abs(infinite_serie(1, current_iteration)) > min_error):
        current_iteration += 1

    print(current_iteration - 1)
    print("\n")

#6 Determine the number of iterations necessary to solve x ** 3 + 4x ** 2 - 10 = 0
#with accuracy 10-4 using a = -4 and b = 7.
# a) Using the bisection method
    def bisection_method(f, lower, upper, accuracy):
        import numpy as np

        if np.sign(f(lower)) == np.sign(f(upper)):
            raise Exception("Root was not found between lower and upper bound")
        midpoint = (lower + upper) / 2

        if np.abs(lower - upper) <= accuracy:
            return 0
        elif np.sign(f(upper)) == np.sign(f(midpoint)):
            return bisection_method(f, lower, midpoint, accuracy) + 1
        elif np.sign(f(lower)) == np.sign(f(midpoint)):
            return bisection_method(f, midpoint, upper, accuracy) + 1

# b)Using the newton Raphson method
    def newton_raphson_method(f, df, initial, accuracy):
        result = f(initial) / df(initial)
        x = initial
        count = 1

        while(abs(result) >= accuracy):
            x -= result
            count += 1
            result = f(x) / df(x)
            return count

    f_x = lambda x: (x ** 3) + ((x ** 2)) - 10
    df_dx = lambda x: 3 * (x ** 2) + (8 * x)

    print(bisection_method(f_x, -4, 7, 0.0001))
    print("\n")
    print(newton_raphson_method(f_x, df_dx, 7, 0.0001))
    print("\n")



assigment_1()
