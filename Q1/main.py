def createf():
  f = open('Q1.txt', 'w+')
  f.write(
    "Neither apple nor pine are in pineapple.\nBoxing rings are square.\nWriters write, but fingers don't fly. Overlook and oversee are opposites.\nA house can burn up just as it burns down. An alarm goes off by going on."
  )


createf()

#a
f = open("Q1.txt", "r+")
print("\n(A)")
print(f.read())
f.close()

#b
print("\n(B)")
f = open("Q1.txt", "a")
f.write("\nBalls.")
f = open("Q1.txt", "r")
c = 1
for i in f:
  print(c, i)
  c += 1

#c
print("\n(C)")
print(f.seek(0))
l = f.readlines()
print(l[len(l) - 1])

#d
print("\n(D)")
print(l[0][10::])

#e
print("\n(E)")
i = int(input("Enter line number: "))
print(l[i - 1])

#f
D = {}
for line in l:
  words = line.split()
  for word in words:
    for letter in "abcdefghijklmnopqrstuvwxyz":
      if word.startswith(letter) or word.startswith(letter.upper()):
        if letter not in D:
          D[letter] = 1
        else:
          D[letter] += 1
print("\n(F)\n")
for lett in D:
  print("Words beginning with", lett, " = ", D[lett])
f.close()
