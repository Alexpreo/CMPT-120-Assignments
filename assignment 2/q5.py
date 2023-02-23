def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = int(input())
denominators = [0] * n

for i in range(n):
    denominator = int(input())
    denominators[i] = denominator

lcm_value = denominators[0]
for i in range(1, n):
    lcm_value = lcm(lcm_value, denominators[i])

print(lcm_value)