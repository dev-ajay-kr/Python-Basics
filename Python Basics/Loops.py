####### FOR LOOP
months = ["Jan", "Feb", "Mar"]
for a in months:
    print(a)

for a in "itsourcecode":
  print(a)
####else in for loop
count = [5, 4, 3, 2, 1]

for i in count:
    print(i)
else:
    print("No items left.")


############WHILE loop
i = 1
while i < 11:
  print(i)
  i=i+1
  i+=1
else:
    print(i,"has become lesss")


#### ----------Nested Loop -----------######
color = ["red", "blue", "yellow"]
thing = ["cellphone", "laptop", "shoe"]

for a in color:
  for b in thing:
    print(a, b)

###------LOOP CONTROL _____________##########

# Break Statement
# Continue Statement
# Pass Statement

# Example: Make a list of odd numbers between 1 and 20. (use while, break)

num = 1
odd_nums = []
while num:
    if num % 2 != 0:
        odd_nums.append(num)
    if num >=20:
        break
    num += 1
print("Odd numbers: ", odd_nums)



# Example: If the current number is 6, skip the iteration (use while, continue)

num = 0
while num < 10:
    num += 1
    if num == 6:
        continue
    print(num)

###########   The pass statement
#to hold the code for future enhancement
#while loop pass statement
print("While loop Pass Statement\n")
num = 1
while num <= 10:
    if num == 6:
        pass
    print(num)
    num += 1

print("\nFor loop Pass Statement\n")
#for loop pass statement
for num in range(1, 11):
    if num == 6:
        pass
    print(num)
