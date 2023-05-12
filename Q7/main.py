i = int(input("Enter number: "))


def count(n):
  return len(str(n))


def reverse(n):
  return str(n)[::-1]


def hasdigit(n):
  global i
  return str(n) in str(i)


def show(n):
  s = ""
  i = 10**(len(str(n)) - 1)
  m = n
  while i > 1:
    p = int(n - (n % i))
    n = int(n % i)
    s += str(p) + " + "
    i = i / 10
  s += str(m)[-1]
  return s


print(count(i))
print(reverse(i))
print(hasdigit(int(input("Enter digit: "))))
print(show(i))
