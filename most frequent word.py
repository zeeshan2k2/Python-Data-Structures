file = input("Enter the name of the file : ")
handle = open(file)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

ke = counts.values()
li1 = []
for num in ke:
    li1.append(num)

li1 = set(li1)
li2 = []
for i in li1:
    li2.append(i)

max_number = li2[-1]

for key, val in counts.items():
    if val == max_number:
        print("The word '" + key + "' is used", max_number, "times.")


