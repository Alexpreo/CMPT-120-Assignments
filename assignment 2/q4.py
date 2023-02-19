primes = 0
comps = 0
tot = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeWeight(num, primes):
    for i in range(num):
        if is_prime(i) == True:
            primes += 1
    return primes

def compWeight(num, comps):
    for j in range(num):
        if is_prime(j) == True:
            div = num % j
            if div == 0:
                comps += 1
    return comps


basket = int(input())
for k in range(basket):
    num = int(input())
    if is_prime(num) == True:
        outputPrime = primeWeight(num, primes)
        tot += outputPrime
        # print(tot)
    else:
        outputComp = compWeight(num, comps)
        tot += outputComp
        # print(tot)

if is_prime(tot) == True:
    print(tot - primeWeight(tot, primes))
else:
    print(tot - compWeight(num, comps))

    

