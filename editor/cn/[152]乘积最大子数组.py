# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  测试用例的答案是一个 32-位 整数。 
# 
#  请注意，一个只包含一个元素的数组的乘积是这个元素的值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  nums 的任何子数组的乘积都 保证 是一个 32-位 整数 
#  
# 
#  Related Topics 数组 动态规划 👍 2560 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_f = min_f = 1
        ans=-inf
        for num in nums:
            if num < 0:
                max_f,min_f = min_f,max_f
            max_f = max(max_f*num,num)
            min_f = min(min_f*num,num)
            ans = max(ans,max_f)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
