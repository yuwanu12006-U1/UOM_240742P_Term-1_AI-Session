import math

def largest_prime_factor(n):
    number = n
    largest_factor = 1
    
    while number % 2 == 0:
        largest_factor = 2
        number //= 2

    d = 3
    while d * d <= number:
        while number % d == 0:
            largest_factor = d
            number //= d
        d += 2
    
    if number > 2:
        largest_factor = number
        
    return largest_factor

number_to_factor = 600851475143

result = largest_prime_factor(number_to_factor)
print(f"The largest prime factor of {number_to_factor} is: {result}")
