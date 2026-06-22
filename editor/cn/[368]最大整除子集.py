# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[
# j]) 都应当满足：
# 
#  
#  answer[i] % answer[j] == 0 ，或 
#  answer[j] % answer[i] == 0 
#  
# 
#  如果存在多个有效解子集，返回其中任何一个均可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 2 * 10⁹ 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 数学 动态规划 排序 👍 656 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        ans = -1
        for i,num in enumerate(nums):
            for j in range(i):
                if  num % nums[j]  == 0:
                    dp[i] = dp[j].copy() if len(dp[j]) > len(dp[i]) else dp[i]
            dp[i].append(num)
            ans = i if len(dp[i]) > len(dp[ans]) else ans
        return dp[ans]
# leetcode submit region end(Prohibit modification and deletion)
