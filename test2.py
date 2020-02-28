def array123(nums):
  a = "".join(nums)
  if a.count("abc") > 0:
    return True
  else:
    return False
  
print(array123([1,2,0,4,3,9]))