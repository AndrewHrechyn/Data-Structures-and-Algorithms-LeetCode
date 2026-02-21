# race_results = input()

def time_to_seconds(h, m, s):
    seconds = h * 3600 + m * 60 + s

    return seconds

def median(nums):

    nums = sorted(nums)

    n = len(nums)

    if n % 2 == 1:
        return nums[n // 2]
    else:
        mid1, mid2 = nums[n // 2 - 1], nums[n // 2]
        return (mid1 + mid2) / 2


def calculate():
    race_results = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

    each_result = race_results.split(', ')

    print(each_result)

    total_seconds = []

    for res in each_result:
        h, m, s = res.split('|')

        h = int(h)
        m = int(m)
        s = int(s)

        total_seconds.append(time_to_seconds(h, m, s))

    total_seconds = sorted(total_seconds)

    print(total_seconds)

    print(f"Range: {max(total_seconds) - min(total_seconds)} Average: {sum(total_seconds) / len(total_seconds)} Mean: {median(total_seconds)}")



calculate()