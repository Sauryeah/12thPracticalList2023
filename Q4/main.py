file = open("myfile.txt", "r")
para1 = file.readlines()
file.close()
para = []
histogram = {}
for line in para1:
  para += line.split()

for word in para:
  if word.lower() not in histogram:
    histogram[word.lower()] = 1
  else:
    histogram[word.lower()] += 1

#A, i
print("\n(A)(i) Total number of words:", len(para))
#A, ii
print("(ii) Number of different words:", len(histogram.values()))
#A, iii
print("iii) The most common words:", end=" ")
occ = list(histogram.values())
for key in histogram:
  if histogram[key] == max(occ):
    print(key, end=", ")

#B
lendict = {}
for word in para:
  lendict[word] = len(word)


def find_longest_word():
  global lendict
  occ2 = lendict.values()
  print("\n\n(B) The longest word(s):", end=" ")
  for key in lendict:
    if lendict[key] == max(occ2):
      print(key, end=", ")


find_longest_word()


def filter_long_words(n):
  longwords = []
  for key in lendict:
    if lendict[key] > n:
      longwords.append(key)
  return longwords


print("List of words longer than n: ",
      filter_long_words(int(input("\n\nEnter n: "))))
