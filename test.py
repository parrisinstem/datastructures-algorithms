def sum_digits(n):
    if n < 0 or n > 9:
        return "Invalid. Select number between 0-9"
    
    digits = []
    for i in range(1,5):
        digits.append(int(str(n) * i))

    return sum(digits)

print(sum_digits(7))