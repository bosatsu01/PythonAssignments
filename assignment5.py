num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

l1=[num1,num2,num3,num4,num5]
print(l1)


print("sum: ",sum(l1))


print("Smallest: ",min(l1))


print("Largest",max(l1))


l1.sort()
print("Sort Ascending: ",l1)


l1.sort(reverse=True)
print("Sort Descending: ",l1)


t=()
t=tuple(l1)
print("tuple: ",t)

del l1
