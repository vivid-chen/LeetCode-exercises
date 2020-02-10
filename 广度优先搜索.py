# 包含队列和图

# 散列表格子表示中心节点，映射数组表示临近节点
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

# 检查一个人的名字是不是以m结尾的函数
def person_is_m(name):
    return name[-1] == 'm'

# 广度优先搜索主体函数
# 找到路径最短的m结尾的人名
def search(name):
    # 创建一个队列
    # 队列相当于查找顺序，弹出一个搜索一个，需要搜索的放入队列尾
    search_queue = deque()

    # 自己不用找，直接从自己的临近节点开始找
    # 将自己的临近节点压入队列
    search_queue += graph[name]
    searched = [] # 这个数组用来保存检查过的人，防止无限循环
    while search_queue:
        person = search_queue.popleft()
        if person not in searched: # 当这个人没在检查过的名单里才检查
            if person_is_m(person):
                print(person + " is a final M!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) # 将这个人标记为检查过的人名

    return False

search("you")

# 这个算法的弊端就是寻找的是段数最少的路径，而没有考虑每一段的权重，相当于所有的权重是1

