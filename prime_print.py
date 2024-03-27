def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(limit):
    prime_numbers = []
    for num in range(2, limit):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Print prime numbers up to 50
print(print_prime_numbers(50))
