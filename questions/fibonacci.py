#1. First 100 even-valued Fibonacci numbers

#Selective recursive apporach as Fibonacci sequeue itself is recursive is usually done but 
#with input 100 this could cause stack overflow in the call stack in some systems, therefore I have completed iteratively as well

#Iteratively
def fibonacci(n):
    #base case
    if n <= 1:
        return n
    #init sequence starting numbers
    fibonacci_numbers = [0, 1]

    #iterate through up to the index of n
    for i in range(2, n + 1):
        #append each value throughout iteraion
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    
    return fibonacci_numbers[n]


def fibonacci_sum_even(n):

    sum_even_numbers = 0
    #iterate through every 3rd starting at index 3 as that is where even numbers are placed
    for i in range(3, n + 1, 3):
        fibonacci_numbers = fibonacci(i)
        #confirm the numbers are even by ensuring modulo 2 = 0
        if fibonacci_numbers % 2 == 0:
            #increment the num
            sum_even_numbers += fibonacci_numbers

    return sum_even_numbers

#test case
total_sum = fibonacci_sum_even(100)
print(f"The sum of the first 100 even value fibonacci numbers is {total_sum}")

#Recursively
def fibonacci(n):
    #base case
    if n <= 1:
        return n
    #init sequence starting numbers
    fibonacci_numbers = [0, 1]

    #iterate through up to the index of n
    for i in range(2, n + 1):
        #append each value throughout iteraion
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    
    return fibonacci_numbers[n]

def fibonacci(n):
    #base case 
    if n <= 1:
        return n
    #recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sum_even(n):
    #base case
    if n <= 0:
        return 0
    
    #get fibonacci numbers
    fibonacci_value = fibonacci(n) 
    #list comprehension sum only even fibonacci numbers 
    sum_even_numbers = fibonacci_value if fibonacci_value % 2 == 0 else 0

    #recursive step 
    return sum_even_numbers + fibonacci_sum_even(n - 1)

#test case
total_sum = fibonacci_sum_even(100)
print(f"The sum of the first 100 even value fibonacci numbers is {total_sum}")#1. First 100 even-valued Fibonacci numbers

#Selective recursive apporach as Fibonacci sequeue itself is recursive is usually done but 
#with input 100 this could cause stack overflow in the call stack in some systems, therefore I have completed iteratively as well

#Iteratively
def fibonacci(n):
    #base case
    if n <= 1:
        return n
    #init sequence starting numbers
    fibonacci_numbers = [0, 1]

    #iterate through up to the index of n
    for i in range(2, n + 1):
        #append each value throughout iteraion
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    
    return fibonacci_numbers[n]


def fibonacci_sum_even(n):

    sum_even_numbers = 0
    #iterate through every 3rd starting at index 3 as that is where even numbers are placed
    for i in range(3, n + 1, 3):
        fibonacci_numbers = fibonacci(i)
        #confirm the numbers are even by ensuring modulo 2 = 0
        if fibonacci_numbers % 2 == 0:
            #increment the num
            sum_even_numbers += fibonacci_numbers

    return sum_even_numbers

#test case
total_sum = fibonacci_sum_even(100)
print(f"The sum of the first 100 even value fibonacci numbers is {total_sum}")

#Recursively
def fibonacci(n):
    #base case
    if n <= 1:
        return n
    #init sequence starting numbers
    fibonacci_numbers = [0, 1]

    #iterate through up to the index of n
    for i in range(2, n + 1):
        #append each value throughout iteraion
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    
    return fibonacci_numbers[n]

def fibonacci(n):
    #base case 
    if n <= 1:
        return n
    #recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sum_even(n):
    #base case
    if n <= 0:
        return 0
    
    #get fibonacci numbers
    fibonacci_value = fibonacci(n) 
    #list comprehension sum only even fibonacci numbers 
    sum_even_numbers = fibonacci_value if fibonacci_value % 2 == 0 else 0

    #recursive step 
    return sum_even_numbers + fibonacci_sum_even(n - 1)

#test case
total_sum = fibonacci_sum_even(100)
print(f"The sum of the first 100 even value fibonacci numbers is {total_sum}")