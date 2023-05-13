from perfect import *

num = int(input("Enter number: "))
factors = GenerateFactors(num)

print("Prime number?: ", isPrimeNo(num, factors))
print("Perfect number?: ", isPerfectNo(num, factors))
