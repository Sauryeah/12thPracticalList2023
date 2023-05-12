num = int(input("Enter number: "))


def GenerateFactors(num):
  factors = []
  for i in range(1, num):
    if num % i == 0:
      factors.append(i)
  print("Factors: ", factors + [num])
  return factors


factors = GenerateFactors(num)


def isPrimeNo(num):
  global factors
  return factors == [1]


def isPerfectNo(num):
  global factors
  s = 0
  for i in factors:
    s += i
  return s == num


print("Prime number?: ", isPrimeNo(num))
print("Perfect number?: ", isPerfectNo(num))
