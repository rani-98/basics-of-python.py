text="hello how are you "
vowel_count=0
for char in text:
    if char.lower() in "aeiou":
        vowel_count+=1
print(vowel_count)


