n = open("swaoutput.txt","r")  # open file, read-only
s = open("swasorter.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()