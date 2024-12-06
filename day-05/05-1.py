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

def main():
    rules, updates = parse_input('input.txt')
    total_middle_sum = 0
    
    for update in updates:
        if is_correct_order(update, rules):
            total_middle_sum += find_middle_page(update)
    
    print(total_middle_sum)

if __name__ == "__main__":
    main()