print("Break usage:")
for i in range(1,6):
    if i==3:
        break         #Break
    print(i)                    

print("continue")
s="string"
for n in s:
    if n=="r":
        continue         #Continue
    print(n)                 

print("pass")  
for i in range(1,11):
    if i%2==0:
        pass         #Pass
    else:
        print(i)              

print("for with if else")
for i in range(1,11):
     if i%2==0:
         print(i," is even")
     else :
         print(i," is odd")          

print("while with if else")
i=1
while i<=10:
     if i%2==0:
         print(i," is even")
         i+=1 
     else:
         print(i," is odd")         
         i+=1          
              