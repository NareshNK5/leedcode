'''
nth=int(input("Enther Nth number of Fibonnaci :"))
n1,n2=0,1
c=0
if nth<=0:
    print("Enter Positive Number")
elif nth==1:
    print(f"The fibonanci number is : {nth}")
else:
    while c<nth:
        ntht=n1+n2
        print(n1)
        n1=n2
        n2=ntht
        c+=1
'''

#-----------------------check----------------------
fib_nums = [0, 1]  
number = int(input('Enter the number you want to check for fibonacci number: '))
while fib_nums[-1] <= number:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])
print(fib_nums)
if number in fib_nums:
    print(f'Yes. {number} is a fibonacci number.')
else:
    print(f'No. {number} is NOT a fibonacci number.')