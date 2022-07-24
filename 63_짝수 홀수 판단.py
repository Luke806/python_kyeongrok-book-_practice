def is_even(num):

    zero = num%2 == 0
    one = num%1 == 0
    print("num%2 == 0:",zero)
    print("num%1 == 0:",one)

result = is_even(3)
print(result)