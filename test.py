

def fibonacci(n):
#base case 
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sum_even(n):
    #base case
    if n <= 0:
        return 0
    
    #get fibonacci values
    fibonacci_value = fibonacci(n) 
    #list comprehension sum only even fibonacci values 
    sum_even_numbers = fibonacci_value if fibonacci_value % 2 == 0 else 0

    #recursive step 
    return sum_even_numbers + fibonacci_sum_even(n - 1)

#test case

total_sum = fibonacci_sum_even(100)
print(total_sum)
# print(f"The sum of the first 100 even value fibonacci numbers is {total_sum}")
