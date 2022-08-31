f = open('inputFile.txt', 'r')
passFile = open('failFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'F':
        passFile.write(line)
f.close()