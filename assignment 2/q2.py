def SubstringFinder2(source, target):
    for i in range(len(source) - len(target) + 1):
        if source[i:i + len(target)] == target:
            return i
    return -1

source = input()
target = input()

result = SubstringFinder2(source, target)
print(result)