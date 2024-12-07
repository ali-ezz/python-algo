def dominator_max(array,n):
    i=0
    j=0
    count=0
    max_count=-1000000000
    index_num_count=0
    while i<n:
     while j<n:
      if array[i]==array[j]:
        count+=1
        j+=1
      else:
       j+=1
     i+=1
     if max_count<=count:
       max_count=count
       index_num_count=i
       i+=1
       count=0
     else:
       i+=1
       count=0
    if max_count>(n/2):
     print(max_count)
     print(index_num_count) 
    else: print('-1')

dominator_max([1,4,4],3)

      
