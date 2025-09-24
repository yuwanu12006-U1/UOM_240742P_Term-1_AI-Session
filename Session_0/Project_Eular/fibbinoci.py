f_n_minus_1 = 1
f_n = 2

even_sum = 2

while True:
    next_term = f_n_minus_1 + f_n
    
    if next_term > 4000000:
        break
    
    if next_term % 2 == 0:
        even_sum += next_term
        
    f_n_minus_1 = f_n
    f_n = next_term
    
print(f"The sum of even-valued Fibonacci terms under 4,000,000 is: {even_sum}")
