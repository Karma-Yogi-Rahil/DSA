nums1 = [1,2]
nums2 = [3,4]

nums1=(nums1+nums2)
nums1.sort()
print(len(nums1))
 
if len(nums1)%2 == 0: 
    n1 = nums1[int(len(nums1)/2)]
    n2 = nums1[int(len(nums1)/2 -1)]
    print((n1+n2) / 2)
    

else:
    print(nums1[int(len(nums1)/2)])
