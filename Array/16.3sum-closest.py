"""
16. 最接近的三数之和
中等
https://leetcode-cn.com/problems/3sum-closest/
"""

from typing import List

class Solution:
    # 方法一：排序+双指针
    # 152 ms	38.11%
    # 13.8 MB   
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = sum(nums[:3])
        distance = abs(res - target)
        length = len(nums)
        for i in range(length - 2):
            num_i = nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                tempSum = num_i + nums[j] + nums[k]
                tempDistance = abs(tempSum - target)

                if tempDistance == 0:
                    return tempSum

                if tempDistance < distance:
                    distance = tempDistance # 提交错误时，遗漏此行代码
                    res = tempSum

                if tempSum >= target:
                    while k - 1 >= j:
                        if nums[k - 1] != nums[k]:
                            k -= 1
                            break
                        else:
                            k -= 1
                else:
                    while j + 1 <= k:
                        if nums[j + 1] != nums[j]:
                            j += 1
                            break
                        else:
                            j += 1
        return res

if __name__ == "__main__":
    su = Solution()
    # print(su.threeSumClosest([-1, 2, 1, -4], 1))
    print(su.threeSumClosest([0,2,1,-3], 1)) # leetcode 提交错误