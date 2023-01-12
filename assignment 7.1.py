
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
n = 0
x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line[20:]
    x = x + 1
    n = n + float(line)

print("Average spam confidence:", n/x)
