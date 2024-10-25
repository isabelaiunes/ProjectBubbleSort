# Start #
# Loop1: For each element i in the array of size n #
# Loop2: For each element j in the array of size n-1 (compare the elements again) #
# Conditional: If element i is greater than element j, swap elements i and j #
# Display the sorted array #
# End #

# Consider this list as an example for sorting with Bubble Sort #
list = [6, 3, 12, 7]
# In the first pass of the algorithm, elements i and j are compared, placing the smaller one in the first position #
list = [3, 6, 12, 7]
# In the second pass, the algorithm compares 6 and 12 and does not swap them, since 6 < 12 #
list = [3, 6, 12, 7]
# In the third pass, the algorithm compares 12 and 7 and swaps them, because 7 < 12 #
list = [3, 6, 7, 12]

