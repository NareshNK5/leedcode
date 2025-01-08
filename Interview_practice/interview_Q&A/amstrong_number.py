# def is_armstrong(num):
#     num_str = str(num)
#     num_digits = len(num_str)
#     total_sum = 0
#     for digit_char in num_str:
#         digit = int(digit_char)
#         total_sum += digit ** num_digits
#     if num == total_sum:
#         return True
#     else:
#         return False
# user_input = int(input("Enter a positive integer: "))
# if is_armstrong(user_input):
#     print(f"{user_input} is an Armstrong number.")
# else:
#     print(f"{user_input} is not an Armstrong number.")

# num=407
# def ams(num):
#     num_str=str(num)
#     num_len=len(num_str)
#     total=0
#     for i in num_str:
#         total += int(i) ** num_len
#     if num==total:
#         print("True")
#     else:
#         print("False")
# ams(num)

num=407
nums=str(num)
l=len(nums)
tot=0
for i in nums:
    temp=int(i)
    tot+=temp**l
if tot == num:
    print("amstrong")
else:
    print("not amstrong")