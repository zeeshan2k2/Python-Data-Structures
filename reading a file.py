# fhand = open("txt1.txt", "w")
# print(fhand)

# stuff = "Hello \nworld"
# print(stuff)

# fhand = open("txt1.txt")
# count = 0
# for line in fhand:
#     count = count + 1
# print("Line Count:", count)

fhand = open("txt1.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])


