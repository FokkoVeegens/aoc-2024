import re

def main():
    # Read the content of input.txt
    with open('input.txt', 'r') as file:
        content = file.read()

    # Regular expression to find valid mul(X,Y), do(), and don't() instructions
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)')

    # Find all matches
    matches = pattern.finditer(content)

    # Initialize the sum and the enabled flag
    total_sum = 0
    enabled = True

    # Process each match
    for match in matches:
        instruction = match.group()
        if instruction == 'do()':
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:  # mul(X,Y) instruction
            if enabled:
                x, y = map(int, re.findall(r'\d+', instruction))
                total_sum += x * y

    # Print the final sum
    print(total_sum)

if __name__ == "__main__":
    main()