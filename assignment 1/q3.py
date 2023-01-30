def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

totPrimes = 0
checks = int(input('How many numbers do you want to check?\n'))

for k in range(checks):
    while True:
        num = int(input("Enter a positive integer:\n"))
        if is_prime(num):
            print(num, "is a prime number.")  
            totPrimes += 1
            break
        if num < 0:
            print("PrimeFinder ignores negative numbers!")
        else:
            break
 
print("Total prime numbers:", totPrimes)