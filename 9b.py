from collections import OrderedDict

preamble = 25
nums = OrderedDict()


def add_num(i: int):
    nums[i] = 0
    if len(nums) > preamble:
        nums.popitem(last=False)


def sum_to(target: int) -> bool:
    for i in nums:
        if target - i in nums and i * 2 != target:
            return True
    return False


target = 0
with open("9.txt") as f:
    all_nums = [int(i) for i in f.readlines()]
for i, num in enumerate(all_nums):
    if i < preamble:
        add_num(num)
    else:
        if not sum_to(num):
            target = num
            all_nums = all_nums[:i]
            break
        add_num(num)
rows = {}

for i, num in enumerate(all_nums):
    rows[i] = num
    for j in range(i):
        rows[j] += num
        if rows[j] == target:
            seq = all_nums[j:i+1]
            print(min(seq) + max(seq))
