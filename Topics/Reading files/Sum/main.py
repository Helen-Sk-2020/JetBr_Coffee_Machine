# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    line = line.split()
    print(int(line[0]) + int(line[1]))
file.close()
