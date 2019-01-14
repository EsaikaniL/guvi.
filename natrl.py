num1 = int(input())
if num1 < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num1 > 0):
       sum += num1
       num1 -= 1
   print(sum)
