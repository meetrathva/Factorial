fact = 1
a = int(input("Enter number: "))
for i in range (1,a+1):
    fact *= i
fh = open("6_factorial.txt","w")
fh.write(str(a))
fh.write("\nThe factorial of given number is: ")
fh.write(str(fact))
fh.close()