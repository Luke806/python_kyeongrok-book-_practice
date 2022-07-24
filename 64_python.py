def is_even(num):

    zero = num % 2 == 0
    one = num % 2 == 1

    print(3, "%2 == 0:", zero)
    print(3, "%2 == 1:", one)

    return zero

result = is_even(3)

print(result)