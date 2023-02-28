def palindromeChecker(source):
    word = converter(source)
    word_len = len(word)
    if word == '':
        return 'Yes'
    for i in range(word_len//2):
        if word[i] == word[word_len-i-1]:
            return 'Yes'
    return 'No'
    # word = converter(source)
    # reverse = word[::-1]
    # if word == reverse:
    #     return 'Yes'
    # return 'No'
    
def converter(source):
    lowercase = ''
    for char in source:
        if ord(char) >= 65 and ord(char) <= 90:
            char = ord(char)+32
            to_letters = chr(char)
            lowercase += to_letters
        elif ord(char) == 32 or ord(char) == 44:
            char = ord(char)
            char = 0
            to_letters = chr(char)
            lowercase += to_letters
        else:
            lowercase += char
    #print(lowercase)
    return lowercase
            
source = str(input())
print(palindromeChecker(source))