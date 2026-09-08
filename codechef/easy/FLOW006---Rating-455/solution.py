# cook your dish here
t = int(input())

while t > 0:
    n = int(input())

    sum_digits = 0

    while n > 0:
        digit = n % 10          # Get last digit
        sum_digits += digit     # Add digit to sum
        n = n // 10             # Remove last digit

    print(sum_digits)

    t -= 1