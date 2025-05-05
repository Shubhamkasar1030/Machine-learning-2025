a=int(input("Enter the number : "))
l=len(str(a))
sum=0
n=str(a)
for i in range(0,l):
    sum=sum+(int(n[i])**l)

if(a==sum):
    print("yess")
else:
    print("NO")