fhand = open("romeo.txt")
counts = dict()

for words in fhand:
    words = words.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

sorted_tuple = sorted([(v, k) for k, v in counts.items()], reverse=True)
for k, v in sorted_tuple[:10]:
    print(v, k)




# lst = []
# for k, v in counts.items():
#     newtup = (v, k)
#     lst.append(newtup)
#
# lst = sorted(lst, reverse=True)
#
# for v, k in lst[:10]:
#     print(k, v)
