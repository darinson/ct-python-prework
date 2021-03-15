# Question 1
def greeting(name):
    print("Hello " + name.title() + ".")


def greeting2(name):
    # Instead of concatenating, use "string interpolation" formatting via str.format method and curly brackets
    print("Hello {}!".format(name.title()))
    # String Interpolation/f-strings/formatted string literals
    print(f"Hello again {name.title()} {name.title()}!")


greeting2("Darin")

# Question 2 - Print first odd numbers between 1 and 100


def odd_numbers():
    for i in range(1, 101, 2):
        print(i)


def odd_numbers2():
    numbers = list(range(0.101))
    for number in numbers != 0:
        print(number)


# odd_numbers()

# Question 3


def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num


test = max_num_in_list([2, 3, 5, 8, 9])
print(max_num_in_list([2, 3, 5, 8, 9]))

# Question 4

"""
    TRUTH TREE
    AND
    T & T == T 
    T & F == F
    F & F == F
    OR
    T || F == T
    F || T == T
    F || F == F
"""


def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 4 1.b solution

def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)


is_leap_year(2019)

# Question 5


def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)


is_consecutive([1, 2, 3, 4, 5])
is_consecutive([1, 2, 5, 6])
