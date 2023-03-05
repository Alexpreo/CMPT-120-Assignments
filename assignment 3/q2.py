n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

max_sum = float('-inf')
current_sum = 0
for num in numbers:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)