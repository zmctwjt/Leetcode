# 写一个 RecentCounter 类来计算特定时间范围内最近的请求。 
# 
#  请你实现 RecentCounter 类： 
# 
#  
#  RecentCounter() 初始化计数器，请求数为 0 。 
#  int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求
# ）。确切地说，返回在 [t-3000, t] 内发生的请求数。 
#  
# 
#  保证 每次对 ping 的调用都使用比之前更大的 t 值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# 输出：
# [null, 1, 2, 3, 3]
# 
# 解释：
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
# recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 
# 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= t <= 10⁹ 
#  保证每次对 ping 调用所使用的 t 值都 严格递增 
#  至多调用 ping 方法 10⁴ 次 
#  
# 
#  Related Topics 设计 队列 数据流 👍 275 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# leetcode submit region end(Prohibit modification and deletion)
