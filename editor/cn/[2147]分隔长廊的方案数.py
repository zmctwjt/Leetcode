# 在一个图书馆的长廊里，有一些座位和装饰植物排成一列。给你一个下标从 0 开始，长度为 n 的字符串 corridor ，它包含字母 'S' 和 'P' ，其
# 中每个 'S' 表示一个座位，每个 'P' 表示一株植物。 
# 
#  在下标 0 的左边和下标 n - 1 的右边 已经 分别各放了一个屏风。你还需要额外放置一些屏风。每一个位置 i - 1 和 i 之间（1 <= i <=
#  n - 1），至多能放一个屏风。 
# 
#  请你将走廊用屏风划分为若干段，且每一段内都 恰好有两个座位 ，而每一段内植物的数目没有要求。可能有多种划分方案，如果两个方案中有任何一个屏风的位置不同，那
# 么它们被视为 不同 方案。 
# 
#  请你返回划分走廊的方案数。由于答案可能很大，请你返回它对 10⁹ + 7 取余 的结果。如果没有任何方案，请返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：corridor = "SSPPSPS"
# 输出：3
# 解释：总共有 3 种不同分隔走廊的方案。
# 上图中黑色的竖线表示已经放置好的屏风。
# 上图每种方案中，每一段都恰好有 两个 座位。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：corridor = "PPSPSP"
# 输出：1
# 解释：只有 1 种分隔走廊的方案，就是不放置任何屏风。
# 放置任何的屏风都会导致有一段无法恰好有 2 个座位。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：corridor = "S"
# 输出：0
# 解释：没有任何方案，因为总是有一段无法恰好有 2 个座位。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == corridor.length 
#  1 <= n <= 10⁵ 
#  corridor[i] 要么是 'S' ，要么是 'P' 。 
#  
# 
#  Related Topics 数学 字符串 动态规划 👍 35 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

MOD = 10**9+7
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        res = 1
        s = 0
        t = 0
        all_s = 0
        for i,c in enumerate(corridor):
            if c == 'S':
                if i <len(corridor)-1:
                    s += 1
                all_s += 1
            if s == 2:
                t += 1
            elif s > 2:
                res = (res * t) %MOD
                t = 0
                s = 1
        if all_s == 0 or all_s % 2 == 1:
            return 0
        return res % MOD
# leetcode submit region end(Prohibit modification and deletion)
