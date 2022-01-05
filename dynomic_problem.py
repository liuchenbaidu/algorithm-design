# 最长递增子序列
a = [1,5,3,2,4]

def L(nums,i):
    max_L = 0
    if i==len(nums)-1:
        return 1

    for j in range(i+1,len(nums)):
        if nums[j]> nums[i]:
          max_L =  max(max_L,L(nums,j)+1)
    return max_L

def get_lth(nums):
    return  max([L(nums,i) for i in range(0,len(nums))])

print(max(a))

print(L(a,0))

import  time
print(get_lth(a))
