
string = input("Enter a string: ")
search_char = input("Enter a character to count: ")

count = 0

index = 0
while index < len(string):
    if string[index] == search_char:
        count += 1
    index += 1

print(f"The character '{search_char}' appears {count} times in the string.")