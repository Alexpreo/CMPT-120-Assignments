n = int(input())
anagrams = {}

for i in range(n):

    word = input().replace(' ', '').replace(',', '').lower() 
    sorted_word = ''.join(sorted(word))

    if sorted_word in anagrams:
        anagrams[sorted_word].add(word)
    else:
        anagrams[sorted_word] = {word}

max_size = max(len(s) for s in anagrams.values())

print(max_size)