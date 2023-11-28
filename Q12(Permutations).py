#@title Q12)Permutations
from itertools import permutations
def permu(a):
  return list(permutations(a))
#driver
a=[1,2,3]
result=permu(a)
for perm in result:
  print(perm)  
