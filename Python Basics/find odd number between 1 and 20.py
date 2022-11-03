
num = 1
odd_nums = []
while num:
    if num % 2 != 0:
        odd_nums.append(num)
    if num >=20:
        break
    num += 1
print("Odd numbers: ", odd_nums)