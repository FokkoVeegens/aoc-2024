def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    rules = []
    updates = []
    is_update_section = False
    
    for line in lines:
        if line == '':
            is_update_section = True
            continue
        
        if is_update_section:
            updates.append(list(map(int, line.split(','))))
        else:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
    
    return rules, updates

def is_correct_order(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def find_middle_page(update):
    n = len(update)
    return update[n // 2]

def sort_update(update, rules):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def main():
    rules, updates = parse_input('input.txt')
    total_middle_sum = 0
    
    for update in updates:
        if not is_correct_order(update, rules):
            sorted_update = sort_update(update, rules)
            total_middle_sum += find_middle_page(sorted_update)
    
    print(total_middle_sum)

if __name__ == "__main__":
    main()