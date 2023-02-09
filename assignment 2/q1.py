def SubstringFinder(source, k):
    l = len(source)
    max_substring = ""
    max_unique = 0

    for i in range(l - k + 1):
        substring = source[i:i + k]
        unique = len(set(substring))

        if unique > max_unique:
            max_unique = unique
            max_substring = substring
    return max_substring

while True:
    source = input()
    if source == "quit":
        break

    k = int(input())
    result = SubstringFinder(source, k)
    print(result)   