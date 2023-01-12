fname = input("Enter file name: ")
fh = open(fname)
count = 0
lis1 = []
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    new = line.split()
    email = new[1]
    lis1.append(email)
    count += 1


counts = dict()
for word in lis1:
     counts[word] = counts.get(word, 0) + 1

lis2 = []

for keys, val in counts.items():
    lis2.append(val)

list2 = set(lis2)

lis3 = []
for i in list2:
    lis3.append(i)

max_value = lis3[-1]

for keys, val in counts.items():
    if val == max_value:
        print(keys, max_value)
