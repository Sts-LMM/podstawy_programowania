def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

print(is_perfect_number(is_perfect_number(int(input("Write num to return biggest num you wrote: ")))))
