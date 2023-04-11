from collections import Counter

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

c = Counter(nums1)

print(' '.join(f'{c[m]}' if m in c else '0' for m in nums2))