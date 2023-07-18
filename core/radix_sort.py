def radix_sort(arr):
    # Determine the maximum number of digits in the array
    max_digit = len(str(max(arr)))
    
    # Iterate over each digit from the least significant to the most significant
    for i in range(max_digit):
        # Create 10 buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]
        # Place each element in its corresponding bucket based on the ith digit
        for num in arr:
            digit = (num // 10**i) % 10
            buckets[digit].append(num)
        
        # Reorder the array based on the order of the buckets
        arr = []
        for bucket in buckets:
            for num in bucket:
                arr.append(num)
    return arr

my_arr = [170, 45, 75, 90, 802, 24, 2, 66, 593, 49, 30, 1001]
print(radix_sort(my_arr))