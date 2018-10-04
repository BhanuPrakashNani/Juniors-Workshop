a=input("Enter the number: ")
sum = 0
c=int(a)
b=len(a)
while c > 0:
   num = c%10
   sum +=(num ** b)
   c=c//10
if int(a) == sum:
   print("its an Armstrong number")
else:
   print("its not an Armstrong number")
