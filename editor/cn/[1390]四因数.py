# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。如果数组中不存在满足题意的整数，则返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [21,4,7]
# 输出：32
# 解释：
# 21 有 4 个因数：1, 3, 7, 21
# 4 有 3 个因数：1, 2, 4
# 7 有 2 个因数：1, 7
# 答案仅为 21 的所有因数的和。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [21,21]
# 输出: 64
#  
# 
#  示例 3: 
# 
#  
# 输入: nums = [1,2,3,4,5]
# 输出: 0 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  1 <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics 数组 数学 👍 47 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from math import floor


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            y = 0
            t = 0
            for i in range(2,floor(num**0.5)+1):
                if num % i == 0:
                    if i == num/i:
                        y += 1
                        t += i
                    else:
                        y += 2
                        t += i+num/i
                if y > 2:
                    break
            else:
                if y == 2:
                    res += t + num + 1
        return int(res)


# leetcode submit region end(Prohibit modification and deletion)
