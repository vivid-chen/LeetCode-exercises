# 广播集合覆盖问题

# 算法流程，选择一个广播台覆盖了最多未覆盖的州。即使这个广播台覆盖了一些已经覆盖的州也没有关系
# 重复第一步，直到覆盖了所有的州

# 运行时间O（n^2）

# 需要覆盖的州的集合
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 广播台散列表
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv","ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 最后需要一个集合才存储最后选择的广播台
final_stations = set()

# 当还有州没有覆盖时循环
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        # 将一个广播台覆盖的州与需要覆盖的州取交集
        covered = states_needed & states
        if len(covered) > len(states_covered): # 取每次交集大的广播台
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)