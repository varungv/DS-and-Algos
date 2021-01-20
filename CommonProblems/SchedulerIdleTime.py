# Given a list of timestamps the start and end time of each test. Find the idle time of the scheduler 

# N Resources, T tests.
# t1: {st: x, end: y}
# t2: {st: x+, end: y}
# t3: {st: x, end: y}
#
# 1 test at a time on any resource
# Idle Time
# Time0 to TimeN


# {
#     t1: {10:00 - 10:15},
#     t2: {10:06 - 10:13},
#     t3: {10:10 - 10:18},
#     t4: {10:20 - 10:30}
# }
#
# (10:00-10:15)
# (10:10 - 10:18) -> idel time check -> 0
# (10:20 - 10:30) -> idel time check -> 2mins
# (10:20 - 10:30) -> idel time check -> 2mins
# (10:20 - 10:30) -> idel time check -> 2mins
# (10:20 - 10:30) -> idel time check -> 2mins


exec_time_stamps = [
    {'st': 1000, 'et': 1015},
    {'st': 1006, 'et': 1013},
    {'st': 1010, 'et': 1018},
    {'st': 1020, 'et': 1030},
    {'st': 1150, 'et': 1250}
]


def calc_idle_time(exec_array):
    pivot_time_range = None
    total_idle_time = 0
    for time_range in exec_array:
        if not pivot_time_range:
            pivot_time_range = time_range
            continue

        pivot_time = pivot_time_range['et']
        if time_range['st'] > pivot_time:
            # check idle
            total_idle_time += time_range['st'] - pivot_time

        if time_range['et'] > pivot_time:
            # swap pivot time stamp
            pivot_time_range = time_range

    return total_idle_time


print(calc_idle_time(exec_time_stamps))
