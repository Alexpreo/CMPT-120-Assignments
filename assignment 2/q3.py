def is_palindrome(source):
    source = ""
    for char in source:
        if char >= "A" and char <= "Z":
            source += chr(ord(char) + 32)
        else:
            source += char

    source_no_space = ""
    for char in source:
        if char != " " and char != ",":
            source_no_space += char

    reversed = ""
    for i in range(len(source_no_space)-1, -1, -1):
        reversed += source_no_space[i]
    if source_no_space == reversed:
        return True
    else:
        return False


source = input()

if is_palindrome(source):
    print("Yes")
else:
    print("No")
