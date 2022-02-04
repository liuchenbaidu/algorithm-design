a = [1,2,3,4,5,6]

def reverse(l:list):
    # 首尾不停的交换

    left =0
    right = len(l)-1

    while left<right:
        l[left],l[right] = l[right],l[left]
        left+=1
        right-=1

    return l

result = reverse(a)
print(result)