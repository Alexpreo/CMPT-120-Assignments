def palindromeChecker(source):
    word = toLower(source)
    word_len = len(word)
    for i in range(word_len//2):
        if word[i] != word[word_len-i-1]:
            return 'No'
    return 'Yes'
    
    
def toLower(source):
    lowercase = ''
    for char in source:
        if ord(char) >= 65 and ord(char) <= 90:
            char = ord(char)+32
            to_letters = chr(char)
            lowercase += to_letters
        elif:
            
        else:
            lowercase += char
    return lowercase
            
source = str(input())
print(palindromeChecker(source))