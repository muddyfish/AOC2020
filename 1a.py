nums = set()

with open("1a_input.txt") as f:
    for i in f.readlines():
        nums.add(int(i))

for i in nums:
    if 2020 - i in nums:
        print(i * (2020-i))
