nth=int(input("Enther number of Factorial :"))
tot=1
if nth<=0:
    print("Enter Positive Number")
elif nth==1:
    print(f"The Factorial number is : {nth}")
else:
    for i in range(1,nth+1):
        tot *= i
print(tot)