def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_power_of_5(n):
    return n > 0 and (n & (n - 1)) == 0 and n % 5 == 0


def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0
  
