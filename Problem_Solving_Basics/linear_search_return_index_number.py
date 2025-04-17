#Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. 
#Return the index of the first occurrence of x in the array, or -1 if it doesn’t exist.

arr = [1, 2, 3, 4, 5, 6, 7, 8]

num = int(input("Number to Check: "))

#length = len(arr)+1

def Lsearch(n):
  for i in range(len(n)):
    if num == n[i]:
      break
      return i
    else:
      return -1

print("Index of the number you asked for: ", Lsearch(arr))
