n = int(input())
a = input()
l = []
for i in range (1,n):
    l = a.split()
l = [int(i) for i in l]
l2 = list()
for item in l:
    if item not in l2:
        l2.append(item)
l2.sort()
print(l2[-2])