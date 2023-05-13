#Binary
def B(number):
  s = ""
  quotient = number
  while quotient > 0:
    #Using Base 2
    remainder = int(quotient % 2)
    quotient = int((quotient - remainder) / 2)
    s += str(remainder)
  #flip
  s = s[::-1]
  print("Result: ", s)
  return s


#Octal
def O(number):
  s = ""
  quotient = number
  while quotient > 0:
    #Using Base 8
    remainder = int(quotient % 8)
    quotient = int((quotient - remainder) / 8)
    s += str(remainder)
  #flip
  s = s[::-1]
  print("Result: ", s)
  return s


#Hexadecimal
def H(number):
  s = ""
  quotient = number
  while quotient > 0:
    #Using base 16
    remainder = int(quotient % 16)
    quotient = int((quotient - remainder) / 16)

    #converting decimal remainders into hexadecimal digits
    if remainder == 10:
      s += "A"
    elif remainder == 11:
      s += "B"
    elif remainder == 12:
      s += "C"
    elif remainder == 13:
      s += "D"
    elif remainder == 14:
      s += "E"
    elif remainder == 15:
      s += "F"
    else:
      s += str(remainder)
  #flip
  s = s[::-1]
  print("Result: ", s)
  return s


number = int(input("Sample input: "))
p = str(input("Desired type: "))
if p == "B":
  B(number)
elif p == "O":
  O(number)
elif p == "H":
  H(number)
