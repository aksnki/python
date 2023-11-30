x = int(input(" Enter the first Number : "))
y = int(input(" Enter the Second Number : "))
while y !=0 :
      r = x % y
      x = y
      y = r
print(" The GCD of the Number : ", x)
        
