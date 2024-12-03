def max_proProductofThree(array, n): 
 #best case  
 max_pro=1
 if n<=3:
  while i<n:
   max_pro *= array[i]
   i+=1
  return max_pro
 else:
  """ # Bubble Sort O(n^2) for the easy approach and we have to know the size
  max_pro_1=1
  i=0
  v=-1
  d=0
  while i<n:
   j=0
   while j<n-i-1:
    if array[j]>array[j+1]:
     array[j],array[j+1]=array[j+1],array[j]
    j+=1
   i+= 1
 while v>=-3:
  max_pro_1*=array[v]
  v-=1
 max_pro_2=array[-1]
 while d<2:
  max_pro_2*=array[d]
  d+=1
 if max_pro_2>=max_pro_1:
  return max_pro_2
 else:
  return max_pro_1"""
#secand approch forward O(n) and we dont have to know the size
 max1 = max2 = max3 =-1000000
 min1 = min2 = 1000000
 for item in array:
  if item > max1:
   max3 = max2
   max2 = max1
   max1 = item
  elif item > max2:
   max3 = max2
   max2 = item 
  elif item > max3:
   max3 = item
  if item < min1:
   min2 = min1
   min1 = item
  elif item < min2:
   min2 = item
 max_pro_1 = max1 * max2 * max3
 max_pro_2 = max1 * min1 * min2

 if max_pro_1>=max_pro_2:
   return max_pro_1
 else:
   return max_pro_2

#thered approch in work
"""max_pro_int=-1000000
  smal_int=100000
  array1=array
  array2=array
  c=n
  r=n
  for d in range(3):
   for e in range(c):
    if max_pro_int<=array1[e]:
     max_pro_int=array1[e]
   for t in range(r):
    if smal_int>=array2[t]:
     smal_int=array2[t]
   max_pro_item1.append(max_pro_int)
   max_pro_item2.append(smal_int)
   array1.remove(max_pro_int)
   c-=1
   array2.remove(smal_int)
   r-=1
   max_pro_int=-1000000
   smal_int=100000


  for v in range(3):
   max_pro*=max_pro_item1[v]
  max_pro2=max_pro_item1[0]
  for g in range(2):
   max_pro2*=max_pro_item2[g]
  if(max_pro>=max_pro2):
   return max_pro
  else:
   return max_pro2"""
array=[1,2,3,4]
print(max_proProductofThree(array,8))