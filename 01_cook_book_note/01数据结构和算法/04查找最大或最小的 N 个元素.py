# 问题： 怎样从一个集合中获得最大或者最小的 N 个元素列表？
# 解决方案
# heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。
# 需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势（如果N 快接近集合大小了，那么使用排序操作会更好些）
import heapq

# 简易数据类型
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))

print(heapq.nsmallest(3, nums))

# 复杂数据类型
portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65},
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])
print(cheap)
print(expensive)


# 如果你想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，
# 那么这些函数提供了很好的性能。因为在底层实现里面，首先会先将集合数据进行堆排
# 序后放入一个列表中
print("=" * 30)
heap = list(nums)
print(heap)
heapq.heapify(heap)
print(heap)

# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素
# 如果想要查找最小的 3 个元素，你可以这样做
for i in range(3):
    print(heapq.heappop(heap), ":", heap)
