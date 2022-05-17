# void function
def display_currency(num):
    print("$" + format(num, ",.2f"), end="")

    #   rewritting as a function that returns a value
def make_currency(num):
    return "$" + format(num, format(",.2f"))

#   multiple parameters
def bigger(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c





#   each function has its own se of valuables
#   better to make everything I can inside a function
def main():
    num = 77772.45
    display_currency(num)
    amount = make_currency(num)
    print("***", amount, "***")

def is_prime(n):
    # by definition all prime numbers are > 1
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    #   with special cases eliminated, test the number
    else:
        factor_count = 0
        for factor in range(3, n + 1, 2):
            #   use modulus to test for division with no remainder ie a factor
            if n % factor == 0:
                factor_count += 1
        return not (factor_count > 1)


for value in range(1,101):
    if is_prime(value):
        print(value. end = "")
