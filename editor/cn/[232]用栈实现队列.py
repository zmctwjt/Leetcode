# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）： 
# 
#  实现 MyQueue 类： 
# 
#  
#  void push(int x) 将元素 x 推到队列的末尾 
#  int pop() 从队列的开头移除并返回元素 
#  int peek() 返回队列开头的元素 
#  boolean empty() 如果队列为空，返回 true ；否则，返回 false 
#  
# 
#  说明： 
# 
#  
#  你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法
# 的。 
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]
# 
# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
#  
# 
#  
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= x <= 9 
#  最多调用 100 次 push、pop、peek 和 empty 
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作） 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。 
#  
# 
#  Related Topics 栈 设计 队列 👍 1205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self.stack_out = list()
        self.stack_in = list()

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.empty():
            if not self.stack_out:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        if not self.empty():
            if not self.stack_out:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
