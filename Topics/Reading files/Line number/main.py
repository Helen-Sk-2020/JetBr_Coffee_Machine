file = open('sample.txt', 'r')
# n = 0
# for line in file:
#     n += 1
# print(n)
print(len(file.readlines()))
file.close()
