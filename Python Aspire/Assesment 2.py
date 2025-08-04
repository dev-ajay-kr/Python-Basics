# 1. # Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
# s = 'hello'
# # Print out 'e' using indexing
print("=================Output Separator======================")
s = 'hello'
print(s[1])

# 2. # Reverse the string 'hello' using slicing:
# s —'hello'
# # Reverse the string using slicing
print("=================Output Separator======================")
s = 'hello'
reversed_s = s[::-1]
print(reversed_s)

# 3. # Given the string hello, give two methods Of producing the letter 'o' using indexing.
# s —'hello'
# # Print out the 'o'
# # Method 1:
print("=================Output Separator======================")
s = 'hello'
print(s[4])  # 'o' is at index 4

# # Method 2:
print("=================Output Separator======================")
s = 'hello'
print(s[-1])  # 'o' is at index -1, which is the last character

# 4. # Use for, .split(), and if to create a Statement@at will print out words that start with 's':
# St = 'Print only the words that Start with S in this sentence'

print("=================Output Separator======================")
st = 'Print only the words that Start with S in this sentence'
# Split the sentence into words
words = st.split()

# Loop through each word and print words that start with 's' or 'S'
for word in words:
    if word[0].lower() == 's':
        print(word)

# 5. # Write python program that displays stars(*) in right angled triangular form using nested loops

# Number of rows for the triangle
print("=================Output Separator======================")
rows = 5

for i in range(rows):
    for j in range(i + 1):
        # Print star
        print('*', end='')
    print()

# 6. # Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string, printing each letter on a separate line,
# except backwards.


print("=================Output Separator======================")
# Given string
s = 'hello'

index = len(s) - 1
while index >= 0:
    print(s[index])
    index -= 1
#
# 7 Convert 1024 to binary and hexadecimal representation

print("=================Output Separator======================")
# Decimal number
number = 1024

# Convert to binary
binary_representation = bin(number)
# Convert to hexadecimal
hexadecimal_representation = hex(number)

print(f"Binary representation: {binary_representation}")
print(f"Hexadecimal representation: {hexadecimal_representation}")



# 8. Round 5.23222 to two decimal places

print("=================Output Separator======================")
number = 5.23222
rounded_number = round(number, 2)
print(rounded_number)

# 9.Check if every letter in the string s is lower case
# s = 'hello how are you Mary, are you feeling okay?'

print("=================Output Separator======================")
s = 'hello how are you Mary, are you feeling Okay?'
is_all_lower = s.islower()
print(is_all_lower)  # This will print False because 'Mary' and 'Okay' have uppercase letters.


# 10.How many times does the letter 'w' show up in the string below?
# s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'

print("=================Output Separator======================")
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
count_w = s.count('w')
print(count_w)  # This will print the number of times 'w' appears in the string.
#
# 11:Reverse the list below:
# listl =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("=================Output Separator======================")
list1 =[1, 2, 3, 4]
rev_list1 = list1[::-1]
print(rev_list1)