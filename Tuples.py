# x = ("Glen", "Sally", "ben")
# print(x[2])
# y = (3, 1, 9)
# print(y)
# print(max(y))

# (x, y) = (4, 9)
# print(x)

# d = dict()
# d["csev"] = 2
# d["ccwen"] = 4
# for (k, v) in d.items():
#     print(k, v)
#
# tups = d.items()
# print(tups)

c = {"a": 10, "c": 1, "b": 22}
# n = d.items()
# print(n)
# print(sorted(n))
# for k, v in sorted(c.items()):
#     print(k, v)

tmp = []
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)