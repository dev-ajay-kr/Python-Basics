num1 = input("Enter the num \n")
num = int(num1)
p_num = 0
for number in range(1, num):
    if number > 0:
        p_num = p_num + 1
print(p_num)

# number = [1,2,-2,-4,-67,-23,4,56,78,44,-67,5,6,7,8,88,98]
# p_num = 0
# for num in number:
#     if num > 0:
#         p_num = p_num + 1
# print("Here are total number of positive num", p_num)