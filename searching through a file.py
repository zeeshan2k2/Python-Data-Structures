# fhand = open("txt1.txt")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("from: ") :
#         print(line)

# different logic
# fhand = open("txt1.txt")
# for line in fhand:
#     line = line.rstrip()
#     if "zee" in line:
#         continue
#     print(line)

#  just a concept that we can use try and except if a user enters a nonexistent file name 
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fhand)
    quit()