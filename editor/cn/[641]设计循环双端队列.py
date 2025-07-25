# 设计实现双端队列。 
# 
#  实现 MyCircularDeque 类: 
# 
#  
#  MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。 
#  boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。 
#  boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。 
#  boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。 
#  boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。 
#  int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。 
#  int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。 
#  boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false 。 
#  boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", 
# "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# 输出
# [null, true, true, true, false, 2, true, true, true, 4]
# 
# 解释
# MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#   
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= 1000 
#  0 <= value <= 1000 
#  insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty,
#  isFull 调用次数不大于 2000 次 
#  
# 
#  Related Topics 设计 队列 数组 链表 👍 251 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque:

    def __init__(self, k: int):
        self.MAX_SIZE = k
        self.q = [None]*self.MAX_SIZE
        self.size = 0
        self.head = -1
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.head] = value
            self.size += 1
            self.head = (self.head-1) % self.MAX_SIZE
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.tail] = value
            self.size += 1
            self.tail = (self.tail+1) % self.MAX_SIZE
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.head = (self.head+1) % self.MAX_SIZE
            self.size -=1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.tail = (self.tail-1) % self.MAX_SIZE
            self.size -=1
            return True
        return False

    def getFront(self) -> int:
        return self.q[(self.head+1)%self.MAX_SIZE] if self.size else -1

    def getRear(self) -> int:
        return self.q[(self.tail-1)%self.MAX_SIZE] if self.size else -1

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.MAX_SIZE


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
