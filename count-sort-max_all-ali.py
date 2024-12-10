#count sort in max algo O(n)
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
#test
array=[-10,-10,4,3]
print(max_product_of_three(array))

#pascode me and time complexity chat and me (;
"""
Function max_product_of_three(array):

    n ← length of array           # O(1)

    max_pro_1 ← 1                 # O(1)
    v ← -1                        # O(1)
    d ← 0                         # O(1)

    # إيجاد القيمة الكبرى والصغرى في المصفوفة - O(n)
    max_val ← array[0]
    min_val ← array[0]
    i ← 1
    While i < n do:               # يتم التكرار (n - 1) مرة
        If array[i] > max_val then:
            max_val ← array[i]
        EndIf
        If array[i] < min_val then:
            min_val ← array[i]
        EndIf
        i ← i + 1
    EndWhile

    # حساب نطاق العناصر - O(1)
    range_of_elements ← max_val - min_val + 1

    # تهيئة مصفوفات العد والإخراج
    count_size ← range_of_elements               # O(1)
    count ← array of zeros with size count_size  # O(k) حيث k = range_of_elements
    output ← array of zeros with size n          # O(n)

    # تخزين تكرار كل عنصر - O(n)
    i ← 0
    While i < n do:
        index ← array[i] - min_val               # O(1)
        count[index] ← count[index] + 1          # O(1)
        i ← i + 1                                # O(1)
    EndWhile

    # تعديل مصفوفة العد لتخزين المجاميع التراكمية - O(k)
    i ← 1
    While i < count_size do:
        count[i] ← count[i] + count[i - 1]       # O(1)
        i ← i + 1                                # O(1)
    EndWhile

    # بناء مصفوفة الإخراج المفرزة - O(n)
    i ← n - 1
    While i ≥ 0 do:
        index ← array[i] - min_val               # O(1)
        count[index] ← count[index] - 1          # O(1)
        output[count[index]] ← array[i]          # O(1)
        i ← i - 1                                # O(1)
    EndWhile

    # نسخ العناصر المفرزة إلى المصفوفة الأصلية - O(n)
    i ← 0
    While i < n do:
        array[i] ← output[i]                     # O(1)
        i ← i + 1                                # O(1)
    EndWhile

    # حساب حاصل ضرب أكبر ثلاثة عناصر - O(1)
    # خيار 1: ضرب آخر ثلاثة عناصر
    While v ≥ -3 do:                             # يتم التكرار 3 مرات
        max_pro_1 ← max_pro_1 × array[v]         # O(1)
        v ← v - 1                                # O(1)
    EndWhile

    # حساب حاصل ضرب أكبر عنصر مع أصغر عنصرين - O(1)
    max_pro_2 ← array[-1]                        # O(1)
    While d < 2 do:                              # يتم التكرار مرتين
        max_pro_2 ← max_pro_2 × array[d]         # O(1)
        d ← d + 1                                # O(1)
    EndWhile

    # إرجاع أكبر حاصل ضرب - O(1)
    If max_pro_2 ≥ max_pro_1 then:
        Return max_pro_2
    Else:
        Return max_pro_1
    EndIf

EndFunction

# إجمالي تعقيد الزمن: O(n + k)
# حيث:
#   n هو عدد العناصر في المصفوفة
#   k هو نطاق القيم (max_val - min_val + 1)
"""