def first_unique_char(s: str):
    # Step 1: Count occurrences of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Step 2: Scan the string from left to right to find the first unique character
    for char in s:
        if char_counts[char] == 1:
            return char
            
    return None

# --- Taking Input From the User ---
user_string = input("Enter a string to test: ")

# Run the function
result = first_unique_char(user_string)

# Display the output clearly
if result:
    print(f"The first unique character is: '{result}'")
else:
    print("No unique character found (all characters repeat).")