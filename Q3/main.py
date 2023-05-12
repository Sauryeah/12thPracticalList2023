file = open('db.txt', 'r')
db = file.readlines()
file.close()
lis, regno, dept, lislis = [], [], [], []
#a
for line in db:
  details = tuple(line.split())
  lis.append(details)

#b
for linetup in lis:
  b = list(linetup)
  lislis.append(b)
  regno.append(b[2])
  dept.append(b[4])
regno.sort()

#c
for no in regno:
  for line in lislis:
    if line[2] == no:
      print("Admission number:", line[2])
      print("Name:", line[0], line[1])
      print("Years:", line[3])
      print("Stream:", line[4], "\n")

print("\nThe names of students with no of years less than 3:")
for no in regno:
  for line in lislis:
    if line[2] == no:
      if int(line[3]) < 3:
        print(line[0], line[1])

#d
print("\nNumber of people in each department:")
D = {}
for i in dept:
  D[i] = dept.count(i)
for i in D:
  print(i, "=", D[i])
