list1 = [1, 2, 4, 5]
n = max(list1)  # assume list should contain numbers from 1 to max(list)
expected_sum = n * (n + 1) // 2
actual_sum = sum(list1)
missing_number = expected_sum - actual_sum
print("Missing number is:", missing_number)
