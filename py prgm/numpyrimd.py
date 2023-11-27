def pattern(number):
   for i in range (1,number+1):
       for a in range(1,i+1):
           print(a*i,end=" ")
       print("\n")
n=int(input("enter the limit:"))
pattern(n)
