"""write a python program to print the fibonacci series"""
n=int(input("Enter the numbers:"))
a=0
b=1
sum=0
c=0 #c=1
while(c<n): #while(c<=n):
    print(sum,end=" " )
    c+=1
    a=b
    b=sum
    sum=a+b