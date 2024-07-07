word= str(input("enter a word: "))
reverse_word=word[::-1]
if (word==reverse_word):
    print("it is palindrome")
elif(word!=word):
    print("it is not palindrome")
