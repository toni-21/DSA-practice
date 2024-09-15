def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    res = []

    res.append(list(set1-set2))
    res.append(list(set2-set1))
    return res


answer = findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6])
print("answer is:")
print(answer)
