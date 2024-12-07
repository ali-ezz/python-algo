#forward O(n)
"""
def max_product_of_three(array):
    n = 0 
    for idex in array: 
     n += 1  
    # Best case
    if n <= 3:
        max_pro = 1
        i = 0 
        while i < n:
            max_pro *= array[i]
            i += 1
        return max_pro
    else:
        # Second approach forward O(n)
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
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

        if max_pro_1 >= max_pro_2:
            return max_pro_1
        else:
            return max_pro_2
array=[1,10,2,6,5,3]
print(max_product_of_three(array))

#count sort O(n)
"""
#count sort O(n)
"""
def max_product_of_three(array):
    n = 0 
    for idex in array: 
     n += 1 
    max_pro_1 = 1
    v = -1
    d = 0

    max_val = array[0]
    min_val = array[0]
    i = 1
    while i < n:
        if array[i] > max_val:
            max_val = array[i]
        if array[i] < min_val:
            min_val = array[i]
        i += 1
    range_of_elements = max_val - min_val + 1

    count_size = range_of_elements
    count = [0] * count_size  
    output = [0] * n          

    i = 0
    while i < n:
        index = array[i] - min_val
        count[index] += 1
        i += 1

    i = 1
    while i < count_size:
        count[i] += count[i - 1]
        i += 1

    i = n - 1
    while i >= 0:
        index = array[i] - min_val
        count[index] -= 1
        output[count[index]] = array[i]
        i -= 1

    i = 0
    while i < n:
        array[i] = output[i]
        i += 1

    while v >= -3:
        max_pro_1 *= array[v]
        v -= 1

    max_pro_2 = array[-1]
    while d < 2:
        max_pro_2 *= array[d]
        d += 1

    if max_pro_2 >= max_pro_1:
        return max_pro_2
    else:
        return max_pro_1

array=[-10,-10,4,3]
print(max_product_of_three(array))
"""
# Bubble Sort O(n^2) for the easy approach and we have to know the size
"""
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
   i+=1
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
  return max_pro_1
"""
