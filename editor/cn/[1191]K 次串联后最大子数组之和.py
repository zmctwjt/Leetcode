# 给定一个整数数组 arr 和一个整数 k ，通过重复 k 次来修改数组。 
# 
#  例如，如果 arr = [1, 2] ，
#  k = 3 ，那么修改后的数组将是 [1, 2, 1, 2, 1, 2] 。 
# 
#  返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，在这种情况下它的总和也是 0。 
# 
#  由于 结果可能会很大，需要返回的
#  10⁹ + 7 的 模 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2], k = 3
# 输出：9
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,-2,1], k = 5
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [-1,-2], k = 7
# 输出：0
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  1 <= arr.length <= 10⁵ 
#  1 <= k <= 10⁵ 
#  -10⁴ <= arr[i] <= 10⁴ 
#  
# 
#  Related Topics 数组 动态规划 👍 173 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
MOD = 10**9+7

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        f = 0
        ans = 0
        for _ in range(min(2,k)):
            for num in arr:
                f = max(num,f+num)
                ans = max(ans,f)
        if k > 2:
            ans += max(sum(arr),0) * (k-2)
        return ans % MOD
# leetcode submit region end(Prohibit modification and deletion)
