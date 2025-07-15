# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [4,2,3,4]
# 输出: 4 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 1000 
#  
# 
#  Related Topics 贪心 数组 双指针 二分查找 排序 👍 631 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for k in range(len(nums)-2):
            if nums[k] == 0:
                continue
            l,r = k+1,k+2
            while l < len(nums) and r < len(nums):
                if nums[r] - nums[l] >= nums[k]:
                    l += 1
                else:
                    ans += r-l
                    r += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
