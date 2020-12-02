import re
regex = re.compile("(\d+)-(\d+) (\w): (\w+)")
correct = 0
with open("2a_input.txt") as f:
    for i in f.readlines():
        match = regex.match(i)
        start, end, char, string = match.groups()
        correct += int(start) <= string.count(char) <= int(end)

print(correct)
