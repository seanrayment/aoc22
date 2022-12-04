def interval_contains(interval1, interval2):
    if (interval1[0] >= interval2[0] and interval1[1] <= interval2[1]):
        return True
    elif (interval2[0] >= interval1[0] and interval2[1] <= interval1[1]):
        return True
    return False


def interval_from_string(interval_str):
    interval_list = interval_str.split('-')
    return (int(interval_list[0]), int(interval_list[1]))


assignments = open('input.txt')
count = 0
for pair in assignments:
    intervals = pair.strip().split(',')
    interval1 = interval_from_string(intervals[0])
    interval2 = interval_from_string(intervals[1])
    if interval_contains(interval1, interval2):
        count += 1

print(count)
