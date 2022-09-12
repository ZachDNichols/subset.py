string = input ("Enter the string: ")
stringlist = []
for char in string:
    stringlist.append((int(char)))

n = len(stringlist) - 1
k = n

while k >= 0 and stringlist[k] == 1:
    k = k -1

if k >= 0:
    stringlist[k] = 1
    j = k + 1
    while j <= n:
        stringlist[j] = 0
        j = j + 1

print(stringlist)