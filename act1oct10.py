def first_unique_char(s: str):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    for char in s:
        if char_counts[char] == 1:
            return char
            
    return None
user_string = input("Enter a string to test: ")

result = first_unique_char(user_string)

if result:
    print(f"The first unique character is: '{result}'")
else:
    print("No unique character found (all characters repeat).")