def MedianofTwoSortedArrays(array1,array2,m,n):
 #approch one bubble sort o(n^2)
 array3=array1+array2
 all_size=m+n
 i=0
 while i<all_size:
   j=0
   while j<all_size-i-1:
    if array3[j]>array3[j+1]:
     array3[j],array3[j+1]=array3[j+1],array3[j]
    j+=1
   i+=1
 mid = float(((all_size + 1) * 50) / 100) 
 if mid-int(mid)!=0:
  mid1 = all_size//2-1
  mid2 = all_size//2
  median = (array3[mid1] + array3[mid2]) / 2.0
  return median
 else:
  mid = all_size // 2
  median = array3[mid]
  return median
#aproch 2 in work 

array1=[1,2,3]
array2=[4,5,6]
print(MedianofTwoSortedArrays(array1,array2,3,3))