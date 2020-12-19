import re


def regex_for_rule(rule_id):
    rule = rules[rule_id]
    if rule_id == "8":
        return f"(?:{regex_for_rule('42')})+"
    if rule_id == "11":
        rule_42 = regex_for_rule("42")
        rule_31 = regex_for_rule("31")
        return "(?:"+"|".join(f"(?:{(rule_42*i)+(rule_31*i)})" for i in range(1, 6))+")"

    if '"' in rule:
        return rule[1:-1]
    elif "|" in rule:
        return "(?:"+"|".join(f"(?:{''.join(map(regex_for_rule, subrule.split()))})" for subrule in rule.split("|"))+")"
    else:
        return "".join(map(regex_for_rule, rule.split()))


with open("19.txt") as f:
    rules_str, messages_str = f.read().split("\n\n")

    rules = {}
    for rule in rules_str.split("\n"):
        k, v = rule.split(": ")
        rules[k] = v

    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"

    regex = re.compile("^"+regex_for_rule("0")+"$")
    print(regex.pattern)

    messages = messages_str.split("\n")
    for message in messages:
        print(message, bool(regex.match(message)))

    print(sum(bool(regex.match(message)) for message in messages))
