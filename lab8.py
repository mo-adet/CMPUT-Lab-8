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
    """

    :param dividend:
    :param divisor:
    :return:
    """
    assert dividend >= 0 and divisor >= 0, "Error: The divisor and dividend must be a positive integer. "

    if divisor == 0:
        raise Exception("Error: Can't divide by 0. ")

    if divisor >= dividend:
        return 0

    return 1 + intDivision(dividend-divisor, divisor)

def sumDigits(some_sum):
    """
    :param some_sum:
    :return:
    """
    if some_sum != "":
        if int(some_sum) < 0:
            raise Exception("Error: Number must be a positive integer. ")

    # on the first call
    if isinstance(some_sum, int):
        some_sum = str(some_sum)

    # Base case
    if some_sum == "":
        return 0

    number = int(some_sum[0])

    return number + sumDigits(some_sum[1:])

def reverseDisplay(some_num):
    """

    :param some_num:
    :return:
    """
    if some_num != "":
        if int(some_num) < 0:
            raise Exception("Error: Number must be a positive integer. ")

    if isinstance(some_num, int):
        some_num = str(some_num)

    if some_num == "":
        return ""

    return some_num[-1] + reverseDisplay(some_num[:-1])

def binary_search2(key,alist,low,high):
    # finds and returns the position of key in alist
    # or returns ‘Item is not in the list’
    # - key is the target integer that we are looking for
    # - alist is a list of valid integers that is searched
    # - low is the lowest index of alist
    # - high is the highest index of alist
    if low > high:
        return "The item is not in the list. "
    guess = (low+high)//2


    # if the item is found, return the index
    if alist[guess] == key:
        return guess
    # if the key is less than the guess, search the lower half of the list.
    elif key < alist[guess]:
        return binary_search2(key, alist, low, high-1)

    else:
        return binary_search2(key, alist, low+1, high)



def main():
    # --- Exercise 1
    random_list = [67, 75, 78, 3, 6]
    list_length = mylen(random_list)
    print(f"The length of the list is: {list_length}")

    # --- Exercise 2
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    try:
        print(f"Integer division {n} // {m} = {intDivision(n,m)}")
    except Exception as e:
        print(e)

    # --- Exercise 3
    number = int(input('Enter a number: '))
    try:
        print(sumDigits(number))
    except Exception as e:
        print(e)

    # --- Exercise 4
    number_to_reverse = int(input('Enter a number: '))
    print(reverseDisplay(number_to_reverse))

    # --- Exercise 5
    some_list = [-8, -2, 1, 3, 5, 7, 9]
    print(binary_search2(9, some_list, 0, len(some_list) - 1))
    print(binary_search2(-8, some_list, 0, len(some_list) - 1))
    print(binary_search2(4, some_list, 0, len(some_list) - 1))


if __name__ == '__main__':
    main()
