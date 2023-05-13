def isPrimeNo(num, factors):
  return factors == [1]


def isPerfectNo(num, factors):
  s = 0
  for i in factors:
    s += i
  return s == num


def GenerateFactors(num):
  factors = []
  for i in range(1, num):
    if num % i == 0:
      factors.append(i)
  print("Factors: ", factors + [num])
  return factors
