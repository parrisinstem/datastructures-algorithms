def sum_digits(n):
    #conditional for numbers only between 0-9
    if n < 0 or n > 9:
        return "Invalid. Select number between 0-9"
    
    digits = []
    #iterate through 4 times
    for i in range(1,5):
        #append the integer of n,nn,nnn,nnnn
        digits.append(int(str(n) * i))
    #sum
    return sum(digits)
print(sum_digits(3))
print(sum_digits(7))