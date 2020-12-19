import re


def regex_for_rule(rule_id):
    rule = rules[rule_id]
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

    regex = re.compile("^"+regex_for_rule("0")+"$")
    print(regex.pattern)

    messages = messages_str.split("\n")
    for message in messages:
        print(message, bool(regex.match(message)))

    print(sum(bool(regex.match(message)) for message in messages))
