# a = [16, 19, 11, 15, 10, 12, 14]
# for j in range(len(a)):
#     swapped = False
#     i = 0
#     while i<len(a)-1:
#         a[i],a[i+1] = a[i+1],a[i]
#         swapped = True
#         i = i+1
#     if swapped == False:
#         break
#     print (a)

# Creating a bubble sort function  
# def bubble_sort(list1):
#     for i in range(len(list1)-1):
#         for j in range(len(list1)-1):
#             if(list1[j]>list1[j+1]):
#                 temp = list1[j]
#                 list1[j] = list1[j+1]
#                 list1[j+1] = temp
#     return list1
# list1 = [5, 3, 8, 6, 7, 2]
# print("The unsorted list is: ", list1)
# print("The sorted list is: ", bubble_sort(list1))


def bub(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1):
            if(lis[j] > lis[j+1]):
                lis[j] ,lis[j+1]= lis[j+1],lis[j]
    return lis

lis = [5,7,8,3,2,1]
x=bub(lis)
print(x)