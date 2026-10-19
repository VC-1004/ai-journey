nums = [10, 20, 30, 40]

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[-1])
print(len(nums))

for x in nums:
    print(x)

for i in range(len(nums)):
    print(i, nums[i])

total = 0
for x in nums:
    total = total + x
print(total)

result = []
result.append(10)
result.append(20)
result.append(30)
print(result)

warmuplist1 = [8, 3, 10, 1, 6]
smallest = warmuplist1[0]
for x in warmuplist1:
    if x < smallest:
        smallest = x
print(smallest)

warmuplist2 = [8, 3, 10, 1, 6]
count = 0
for x in warmuplist2:
    if x > 5:
        count = count + 1
print(count)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for x in nums:
            total = total + x
            result.append(total)
        return result

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maximum = 0
        for x in nums:
            if x == 1:
                count = count + 1
                if maximum < count:
                    maximum = count
            else:
                count = 0
        return maximum