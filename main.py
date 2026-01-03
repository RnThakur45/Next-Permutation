def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def next_permutation(nums): 
    piv = -1
    n = len(nums)

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            piv = i
            break
    if piv == -1:
        reverse(nums, 0, n-1)
        return nums
    
    for i in range(n-1, piv, -1):
        if nums[i] > nums[piv]:
            nums[i], nums[piv] = nums[piv], nums[i]
            break
    
    i = piv + 1
    j = n - 1

    reverse(nums, i, j)
    return nums

if __name__ == "__main__":
    sample_array = [1,2,3]
    next_perm = next_permutation(sample_array)
    print("Next Permutation:", next_perm)