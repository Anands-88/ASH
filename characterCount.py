message = 'The first time setdefault() is called, the dictionary in spam changes to the method returns the value black because this is now the value set for the key color When spam.setdefault color, white is called next, the value for that key is not changed to white, because spam already has a key named color'

'The setdefault() method is a nice shortcut to ensure that a key exists. Here is a short program that counts the number of occurrences of each letter in a string. Open the file editor window and enter the following code, saving it as characterCount.py:'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] + 1

print(count)