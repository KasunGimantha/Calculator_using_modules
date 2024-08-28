from my_package.advanced_operations.advanced_math import modulus
from my_package.advanced_operations.advanced_math import power_num
from my_package.math_operations import add, div, mult, sub


def process():
    first_val = float(input("Enter first value: "))
    secod_val = float(input("Enter second value: "))

    add(first_val, secod_val)
    sub(first_val, secod_val)
    div(first_val, secod_val)
    mult(first_val, secod_val)
    modulus(first_val, secod_val)
    power_num(first_val, secod_val)


process()
