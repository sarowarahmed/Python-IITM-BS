string1 = input()
string2 = input()

# Create a new string by removing characters from string2 that are present in string1
new_string = ''.join(char for char in string2 if char not in string1)

# Print the new string
print(new_string)     
             
        