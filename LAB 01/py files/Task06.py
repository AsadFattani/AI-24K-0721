
str = input("Enter a string: ")
list = str.split()
length = 0

for word in list:
    if len(word) > length:
        length = len(word)
        longestWord = word

print(f"Longest word: {longestWord} with length {length}")
