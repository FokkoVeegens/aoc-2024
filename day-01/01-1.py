def read_location_ids(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

if __name__ == "__main__":
    left_list, right_list = read_location_ids('input.txt')
    total_distance = calculate_total_distance(left_list, right_list)
    print(f'Total distance: {total_distance}')