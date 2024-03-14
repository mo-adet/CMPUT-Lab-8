'''
Title: Lab 8
Date: March 13, 2024
Author: Muhammad Adetunji
'''

def mylen(some_array):
    """

    :param some_array:
    :return:
    """

    if some_array == []:
        return 0

    some_array.pop()

    return 1 + mylen(some_array)

def intDivision(dividend, divisor):
    if divisor >= dividend:
        return 0

    return 1 + intDivision(dividend-divisor, divisor)

def main():
    random_list = [67, 75, 78, 3, 6]
    list_length = mylen(random_list)
    print(f"The length of the list is: {list_length}")
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print(f"Integer division {n} // {m} = {intDivision(n,m)}")

if __name__ == '__main__':
    main()
