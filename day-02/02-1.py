def is_safe_report(report):
    levels = list(map(int, report.split()))
    increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def count_safe_reports(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()
    
    safe_count = sum(1 for report in reports if is_safe_report(report.strip()))
    return safe_count

if __name__ == "__main__":
    safe_reports = count_safe_reports('input.txt')
    print(f"Number of safe reports: {safe_reports}")