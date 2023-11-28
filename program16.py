#write a program which will take any number and find the sum of the digits of the number

n=int(input("enter any number"))
s=0
while(n!=0):
    d=n%10
    s=s+d
    n=int(n/10)
print("sum of digits =",s)

    
  