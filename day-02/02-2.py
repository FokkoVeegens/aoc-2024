def is_safe_report(levels):
    increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def is_safe_with_dampener(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe_report(new_levels):
            return True
    return False

def count_safe_reports(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()
    
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe_report(levels) or is_safe_with_dampener(levels):
            safe_count += 1
    return safe_count

if __name__ == "__main__":
    safe_reports = count_safe_reports('input.txt')
    print(f"Number of safe reports: {safe_reports}")