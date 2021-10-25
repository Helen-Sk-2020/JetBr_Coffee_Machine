s = list(input())
list_average = []
i = 0
for x in s:
    number = (int(s[i]) + int(s[i + 1])) / 2
    list_average.append(number)
    i += 1
    if i == len(s) - 1:
        break

print(list_average)
