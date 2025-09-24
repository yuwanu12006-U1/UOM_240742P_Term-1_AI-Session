import math

def get_prime_factorization(n):
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def smallest_evenly_divisible(limit):
    max_prime_powers = {}
    for i in range(2, limit + 1):
        factors = get_prime_factorization(i)
        for prime, power in factors.items():
            max_prime_powers[prime] = max(max_prime_powers.get(prime, 0), power)
    
    lcm = 1
    for prime, power in max_prime_powers.items():
        lcm *= prime ** power
    return lcm

limit = 20
result = smallest_evenly_divisible(limit)
print(f"The smallest positive number evenly divisible by all numbers from 1 to {limit} is: {result}")
