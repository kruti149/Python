wordWithoutVovels = ""
userWord = input("Enter a word ").upper()
for letter in userWord:
    if(letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        wordWithoutVovels = wordWithoutVovels + letter;
        continue
    else:
        print(letter)
print ("word without is ", wordWithoutVovels)