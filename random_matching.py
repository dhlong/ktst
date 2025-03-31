import random

n = 24
group_sizes = [5, 3, 3, 3]

random.seed(123)

def simulate_tournament(n, group_sizes):
    match_history = {i: set() for i in range(n)}
    groups = []
    for group_size in group_sizes:
        remaining = {i for i in range(n)}
        grouping = []
        for i in range(n):
            if i in remaining:
                new_group = [i]
                picked = i
                remaining.remove(picked)
                pickable = {i for i in remaining}
                while len(new_group) < group_size:
                    pickable = pickable - {picked} - match_history[picked]
                    if len(pickable) == 0:
                        return None
                    picked = random.choice(list(pickable))
                    new_group.append(picked)
                    remaining.remove(picked)
                    if len(remaining) == 0:
                        break
                grouping.append(new_group)
                for k in new_group:
                    for l in new_group:
                        if k != l:
                            match_history[k].add(l)
                            match_history[l].add(k)
        groups.append(grouping)

    return groups

res = None
while res is None:
    res = simulate_tournament(n, group_sizes)


group_names = 'ABCDEFGHK'

index_str = ''
for i in range(n):
    index_str += f"{i+1:<3}"

for i, grouping in enumerate(res):
    print(f"Round {i+1}:")
    group_map = ['' for _ in range(n)]
    for j, group in enumerate(grouping):
        for k in group:
            group_map[k] = group_names[j]
    print(index_str)
    print('  '.join(group_map))
    print("="*3*n)


import pandas as pd

cols = {"ID": [i+1 for i in range(n)]}
for i, grouping in enumerate(res):
    group_map = ['' for _ in range(n)]
    for j, group in enumerate(grouping):
        for k in group:
            group_map[k] = group_names[j]
    cols[f'Round {i+1}'] = group_map

df = pd.DataFrame(cols)

df.to_csv("group_matching_session1.csv", index=False)
