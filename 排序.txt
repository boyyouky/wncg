#选择
s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

# select_sort
for i in range(0, len(s) - 1):
    index = i
    for j in range(i + 1, len(s)):
        if s[index] > s[j]:
            index = j
    s[i], s[index] = s[index], s[i]

# print sort result.
for m in range(0, len(s)):
    print(s[m])
	
	#冒泡
def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]

print bubbleSort(nums)
# 折半

def binarySearch(x, arr, low, high):#迭代算法
    while low <= high:
        mid = (low+high)/2
        if x == arr[mid]:
            break
        elif x < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    else:
        return -1
		
