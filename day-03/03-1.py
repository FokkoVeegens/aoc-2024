import re

def main():
    # Read the content of input.txt
    with open('input.txt', 'r') as file:
        content = file.read()

    # Regular expression to find valid mul(X,Y) instructions
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    # Find all matches
    matches = pattern.findall(content)

    # Initialize the sum
    total_sum = 0

    # Process each match
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y

    # Print the final sum
    print(total_sum)

if __name__ == "__main__":
    main()