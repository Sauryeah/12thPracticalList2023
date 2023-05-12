file = open("file1.txt", "r")
file2 = open("file2.txt", "a")
s = ""
para = file.readlines()
for line in para:
  words = line.split()
  for word in words:
    for letter in "bcdfghjklmnpqrstvwxyz":
      if word.startswith(letter) or word.startswith(letter.upper()):
        s += word + " "
print(s)
file2.write(s)
file.close()
file2.close()
