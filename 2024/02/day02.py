from resources.levels import *

def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return (increasing or decreasing) and valid_differences

def count_safe_reports(data):
    reports = [list(map(int, line.split())) for line in data]
    results = sum(is_safe_report(report) for report in reports)

    return results

test_reports = test_levels.splitlines()
test_safe_count = count_safe_reports(test_reports)
print(test_safe_count)

if test_safe_count == 2:
    print(f'Test passed!')
    reports = levels.splitlines()
    safe_count = count_safe_reports(reports)
    print(f'safe reports = {safe_count}')
else: 
    print(f'Test faiiled!')