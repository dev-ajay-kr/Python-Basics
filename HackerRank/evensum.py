# def fibevensum(mx):
#     evensum = 0
#     x, y = 0, 1
#     while y < mx:
#         if y%2 == 0: evensum += y
#         x, y = y, x+y
#     return evensum
# print(fibevensum(int(input())))








def fibevensum(mx_list):
    evensum_list = []
    for mx in mx_list:
        evensum=0
        x,y= 0,1
        while y< mx:
            if y%2 == 0: evensum +=y
            x,y=y,x+y
        evensum_list.append(evensum)
    return evensum_list
n= int(input())
mx_list = [int(input()) for _ in range(n)]
for i in range(len(fibevensum(mx_list))):
    print(fibevensum(mx_list)[i])



# ==========================

def fibevensum(mx_list):
    evensum_list = []
    for mx in mx_list:
        evensum=0
        x,y= 0,1
        while y< mx:
            if y%2 == 0: evensum +=y
            x,y=y,x+y
        evensum_list.append(evensum)
    return evensum_list
n= int(input())
mx_list = [int(input()) for _ in range(n)]
arr=fibevensum(mx_list)

for i in range(len(arr)):
    print(arr[i])













def fibevensum(mx_list):
    evensum_list = []
    for mx in mx_list:
        evensum = 0
        x, y = 0, 1
        while y < mx:
            if y%2 == 0: evensum += y
            x, y = y, x+y
        evensum_list.append(evensum)
    return evensum_list
n=int(input())
mx_list = [int(input()) for _ in range(n)]
# print(fibevensum(mx_list))
for i in range(len(mx_list)):
    print(mx_list[i])
