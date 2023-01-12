name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst1 = []
for line in handle:
    line = line.strip()
    if not line.startswith("From "):
        continue
    new = line.split()
    lst1.append(new[5])

# print(lst1)
lst2 = []
for i in range(len(lst1)):
    lst1[i] = lst2.append(lst1[i][:2])

# print(lst2)

for word in lst2:
    counts[word] = counts.get(word, 0) + 1

# print(counts)

tup = counts.items()
sort_tup = sorted(tup)
# print(sort_tup)

for k, v in sort_tup:
    print(k, v)
