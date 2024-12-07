def my_len(sequence):
    """Calculates the length of a sequence.

    Args:
        sequence: The sequence to calculate the length of.

    Returns:
        The length of the sequence.
    """
    count = 0  # Initialize a counter to store the length
    for _ in sequence:  # Iterate over each element in the sequence
        count += 1  # Increment the counter for each element
    return count  # Return the final count

def my_append(lst, element):
    """Appends an element to the end of a list.

    Args:
        lst: The list to append to.
        element: The element to append.
    """
    lst[my_len(lst):] = [element]  # Use slicing to insert the element at the end

def merge_sorted_arrays(arr1, arr2):
    """Merges two sorted arrays without using built-in functions.

    Args:
        arr1: The first sorted array.
        arr2: The second sorted array.

    Returns:
        The merged sorted array.
    """

    merged_arr = []  # Create an empty list to store the merged array
    i, j = 0, 0  # Initialize pointers for both arrays

    while i < my_len(arr1) and j < my_len(arr2):  # Iterate while both arrays have elements
        if arr1[i] < arr2[j]:  # If the current element in arr1 is smaller
            my_append(merged_arr, arr1[i])  # Append the smaller element to the merged array
            i += 1  # Move the pointer for arr1 to the next element
        else:  # If the current element in arr2 is smaller or equal
            my_append(merged_arr, arr2[j])  # Append the smaller element to the merged array
            j += 1  # Move the pointer for arr2 to the next element

    # Append the remaining elements from arr1 (if any)
    while i < my_len(arr1):
        my_append(merged_arr, arr1[i])
        i += 1

    # Append the remaining elements from arr2 (if any)
    while j < my_len(arr2):
        my_append(merged_arr, arr2[j])
        j += 1

    print(merged_arr)
    return merged_arr

def find_median(merged_arr):
    """Finds the median of a sorted array without using built-in functions.

    Args:
        merged_arr: The sorted array.

    Returns:
        The median of the array.
    """

    n = my_len(merged_arr)  # Get the length of the merged array
    if n % 2 == 0:  # If the length is even
        return (merged_arr[n // 2 - 1] + merged_arr[n // 2]) / 2  # Calculate the average of the middle two elements
    else:  # If the length is odd
        return merged_arr[n // 2]  # Return the middle element

def find_median_of_merged_arrays(arr1, arr2):
    """Merges two sorted arrays and finds the median without using built-in functions.

    Args:
        arr1: The first sorted array.
        arr2: The second sorted array.

    Returns:
        The median of the merged array.
    """

    merged_arr = merge_sorted_arrays(arr1, arr2)  # Merge the two arrays
    return find_median(merged_arr)  # Find the median of the merged array

print(find_median_of_merged_arrays([1,2,3,7],[1,4,5,6]))
