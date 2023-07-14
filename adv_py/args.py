def addition(*args):
  result = 0
  for arg in args:
    result += arg
  return result

def main():
  nums1 = [1,2,3,4,5,6,7,8,9]
  nums2 = [10,20,30,40,50]
  sum = addition(nums1, nums2)
  print(sum)

