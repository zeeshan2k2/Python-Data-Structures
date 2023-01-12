
fname = input("Enter file name: ")
fh = open(fname)
list1 = []
list2 = []
for line in fh:
    line.rstrip()
    new = line.split()
    list1.append(new)

for i in list1:
    for j in i:
        list2.append(j)

list2 = set(list2)
list3 = []
for i in list2:
    list3.append(i)

list3.sort()

print(list3)



