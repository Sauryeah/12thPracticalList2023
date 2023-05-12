num = int(input("Enter number: "))
s = ""
while num != 0:
  if num < 4:
    s += "I" * num
    num = 0
  elif num == 4:
    s += "IV"
    num = 0
  elif num < 9:
    s += "V"
    num -= 5
  elif num == 9:
    s += "IX"
    num = 0
  elif num < 39:
    s += "X"
    num -= 10
  elif num <= 49:
    s += "XL"
    num -= 40
  elif num <= 99:
    s += "L"
    num -= 50
  elif num <= 399:
    s += "C"
    num -= 100
  elif num <= 499:
    s += "CD"
    num -= 400
  elif num <= 899:
    s += "D"
    num -= 500
  elif num < 999:
    s += "CM"
    num -= 900
  elif num < 1999:
    s += "M"
    num -= 1000
print(s)


def romanToInt(rom):
  n = 0
  while rom != "":
    if rom.startswith("CM"):
      n += 900
      rom = rom[2:]
    elif rom.startswith("M"):
      n += 100
      rom = rom[1:]
    elif rom.startswith("CD"):
      n += 400
      rom = rom[2:]
    elif rom.startswith("D"):
      n += 500
      rom = rom[1:]
    elif rom.startswith("C"):
      n += 100
      rom = rom[1:]
    elif rom.startswith("XL"):
      n += 40
      rom = rom[2:]
    elif rom.startswith("L"):
      n += 50
      rom = rom[1:]
    elif rom.startswith("X"):
      n += 100
      rom = rom[1:]
    elif rom.startswith("IV"):
      n += 4
      rom = rom[2:]
    elif rom.startswith("V"):
      n += 5
      rom = rom[1:]
    elif rom.startswith("I"):
      n += 1
      rom = rom[1:]
  print(n)


romanToInt(str(input("Enter roman numeral: ")))