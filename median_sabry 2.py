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

def input_and_validate_integer_arrays():
  """
  This function takes two arrays of integer numbers as input from the user. 
  It validates that only integer numbers are entered and prompts the user to 
  re-enter the invalid array if invalid input is provided.

  Returns:
    A tuple containing two lists of integers.
  """

  while True:
    try:
      # Get input for the first array
      array1_str = input("Enter the first array of integers (comma-separated): ")
      array1 = []
      i = 0
      while i < my_len(array1_str):
        if array1_str[i] != ' ' and array1_str[i] != ',': 
          start = i
          while i < my_len(array1_str) and array1_str[i] != ' ' and array1_str[i] != ',':
            i += 1
          my_append(array1, int(array1_str[start:i]))
        i += 1

      # Get input for the second array
      array2_str = input("Enter the second array of integers (comma-separated): ")
      array2 = []
      i = 0
      while i < my_len(array2_str):
        if array2_str[i] != ' ' and array2_str[i] != ',': 
          start = i
          while i < my_len(array2_str) and array2_str[i] != ' ' and array2_str[i] != ',':
            i += 1
          my_append(array2, int(array2_str[start:i]))
        i += 1

      return array1, array2

    except ValueError:
      print("Invalid input. Please re-enter the last array.") 
      continue  # Continue to the next iteration of the loop 

# Example usage
array1, array2 = input_and_validate_integer_arrays()
print("Array 1:", array1)
print("Array 2:", array2) 

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

median = find_median_of_merged_arrays([5, 6], [1, 2]) 
print("Median:", median)