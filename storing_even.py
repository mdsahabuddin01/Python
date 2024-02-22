import array as arr

a = arr.array('i', [7, 3, 1, 11, 69, 100, 200])

b = arr.array('i')

for i in range(0, len(a)):
    if a[i]%2 == 0:
        b.append(a[i])

print(b)
