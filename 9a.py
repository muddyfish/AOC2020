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


with open("9.txt") as f:
    for i, num in enumerate(map(int, f.readlines())):
        if i < preamble:
            add_num(num)
        else:
            if not sum_to(num):
                print(num)
                break
            add_num(num)
