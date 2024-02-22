import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
"""for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)
"""
largest = [a[i] for x in range(1, len(a)) if a[i]>largest : largest=a[i]]

print ("Largest number:", largest)