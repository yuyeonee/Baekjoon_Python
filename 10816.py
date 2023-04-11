n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
answer = []

for num in nums2:
    answer.append(nums1.count(num))

print(*answer)