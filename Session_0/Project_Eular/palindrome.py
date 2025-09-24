def is_palindrome(n):
    """
    Checks if a number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def find_largest_palindrome():
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    """
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if is_palindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome

result = find_largest_palindrome()
print(f"The largest palindrome made from the product of two 3-digit numbers is: {result}")
