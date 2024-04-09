def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def list_primes_up_to_n(n):
    prime_numbers = []
    for num in range(2, n+1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Kiểm tra và liệt kê các số nguyên tố từ 1 đến n
n = int(input("Nhập n: "))
prime_list = list_primes_up_to_n(n)
print("Các số nguyên tố từ 1 đến", n, "là:", prime_list)
