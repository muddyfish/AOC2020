import re


field_regex = re.compile(
    r"byr:(?P<byr>\d{4})\b|"
    r"iyr:(?P<iyr>\d{4})\b|"
    r"eyr:(?P<eyr>\d{4})\b|"
    r"hgt:(?P<hgt>\d{2,3}(?:in|cm))\b|"
    r"hcl:(?P<hcl>#[0-9a-f]{6})\b|"
    r"ecl:(?P<ecl>(?:amb|blu|brn|gry|grn|hzl|oth))\b|"
    r"pid:(?P<pid>\d{9})\b|"
    r"cid:(?P<cid>\S+)\b"
)
print(field_regex.pattern)

valid = 0

with open("4.txt") as f:
    lines = [""]
    for i in f.readlines():
        i = i.strip()
        if i:
            lines[-1] += " " + i
        else:
            lines.append("")

ppd = []
for line in lines:
    ppd.append({m.lastgroup: m.group().replace(f"{m.lastgroup}:", "", 1) for m in field_regex.finditer(line)})

for pp in ppd:
    def fix(key, min, max):
        return min <= int(pp[key]) <= max

    present = set(pp.keys()) - {"cid"}
    if len(present) >= 7:
        if fix("byr", 1920, 2002) and fix("iyr", 2010, 2020) and fix("eyr", 2020, 2030):
            h = pp["hgt"]
            if h.endswith("cm"):
                b = 150, 193
            else:
                b = 59, 76
            pp["hgt"] = pp["hgt"][:-2]
            if fix("hgt", *b):
                valid += 1

print(valid)
