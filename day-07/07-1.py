from itertools import product

def evaluate_expression_left_to_right(numbers, operators):
    result = numbers[0]
    expression = str(numbers[0])
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
            expression += f" + {numbers[i]}"
        elif operators[i-1] == '*':
            result *= numbers[i]
            expression += f" * {numbers[i]}"
    return result, expression

def can_be_true(test_value, numbers):
    if len(numbers) == 1:
        if numbers[0] == test_value:
            return str(numbers[0])
        return None
    
    operators = ['+', '*']
    for ops in product(operators, repeat=len(numbers)-1):
        result, expression = evaluate_expression_left_to_right(numbers, ops)
        if result == test_value:
            return expression
    return None

def main(print_to_console=True):
    total_calibration_result = 0
    
    with open('input.txt', 'r') as file:
        for line in file:
            test_value, numbers = line.split(':')
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers.strip().split()))
            
            expression = can_be_true(test_value, numbers)
            if expression:
                total_calibration_result += test_value
                if print_to_console:
                    print(f"{test_value}: {expression}")
    
    print(f"Total Calibration Result: {total_calibration_result}")
    return total_calibration_result

if __name__ == "__main__":
    main(False)