sum_prime = 0

for num in range(2, 1000):
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        sum_prime += num

print("Sum =", sum_prime)
