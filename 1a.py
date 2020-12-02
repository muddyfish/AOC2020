nums = set()

with open("1a_input.txt") as f:
    for i in f.readlines():
        nums.add(int(i))

for i in nums:
    for j in nums:
        if 2020 - i - j in nums:
            print(i * j * (2020-i-j))
