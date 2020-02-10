# 相比于广度优先搜索算法考虑到图中路径的权重信息

# 步骤
# 1.找出“最便宜”的节点，即最短时间内到达的节点
# 2.更新该节点临近节点的开销
# 3.重复这个过程，直到对图中每个点都这样做
# 4.计算最终路径

# 不考虑负权边
# 由于需要存储以下形式
# 起点->A 6
# 起点->B 2
# 所以采用散列表套散列表的形式，第一个散列表相当于寻找子节点，第二个散列表相当于存储权值
graph = {}
graph["start"] = {} # graph["start"]是一个散列表，在散列表graph内
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# print(graph["start"].keys())
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}
# 上面构建好了所有的边的权重
# 接下来需要一个散列表存储每个节点的开销costs
# 节点的开销是指从起点出发前往该点需要的时间
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 还需要一个存储父节点的散列表
# 记录每个节点的父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 最后需要一个数组来记录处理过的节点
processed = []

# 找出开销最低的点的函数
def find_lowest_cost_node(costs):
    # 初始化先设置成无穷大
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且未处理过
            lowest_cost = cost # 将其视为开销最低的节点
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs) #在未处理的节点中找出开销最小的节点
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): #遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: #如果经当前节点前往该邻居更近
            costs[n] = new_cost #就更新邻居的开销
            parents[n] = node #同时将该邻居的父节点设置为当前节点
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(costs["fin"])

# 广度优先搜索用于在非加权图中查找最短路径
# 狄克斯特拉算法用于在加权图中查找最短路径（需要各个权边为正）
# 如果图中包含负权边，使用贝尔曼-福德算法