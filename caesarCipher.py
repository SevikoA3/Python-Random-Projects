#variables
choice = int(input('do you want to encrypt[1] or decrypt[2]?\n'))
text = input('input your text: ')
offset = int(input('input your offset: '))
newText = ''

#encrypt
if choice == 1:
    for char in text:
        if char.isalpha() and char.islower():
            newChar = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
            newText += newChar
        elif char.isalpha() and char.isupper():
            newChar = chr((ord(char) - ord('A') + offset) % 26 + ord('A')).upper()
            newText += newChar
        else:
            newText += char

#decrypt
elif choice == 2:
    for char in text:
        if char.isalpha() and char.islower():
            newChar = chr((ord(char) - ord('a') - offset) % 26 + ord('a'))
            newText += newChar
        elif char.isalpha() and char.isupper():
            newChar = chr((ord(char) - ord('A') - offset) % 26 + ord('A')).upper()
            newText += newChar
        else:
            newText += char

print('your result is (' + newText + ')')