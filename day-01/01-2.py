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

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = {}
    for number in right_list:
        if number in right_count:
            right_count[number] += 1
        else:
            right_count[number] = 1
    
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        if number in right_count:
            similarity_score += number * right_count[number]
    
    return similarity_score

if __name__ == "__main__":
    left_list, right_list = read_location_ids('input.txt')
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f'Similarity score: {similarity_score}')