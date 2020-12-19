import re


op_regex = re.compile(
    r"(?P<num>\d+)|"
    r"(?P<op>[+\-/*])|"
    r"(?P<close_bracket>\()|"
    r"(?P<open_bracket>\))"
)


def calculate(iterator) -> int:
    def inner(cur, iterator) -> int:
        operator, operand = cur
        if operator == "num":
            op_1 = int(operand)
        elif operator == "open_bracket":
            op_1 = inner(next(iterator), iterator)
        else:
            assert False
        op_type, op = next(iterator, ("close_bracket", ")"))
        if op_type == "close_bracket":
            return op_1
        assert op_type == "op"
        op_2 = calculate(iterator)
        print(f"{op_1} {op} {op_2}")
        return eval(f"{op_1} {op} {op_2}")

    return inner(next(iterator), iterator)


with open("18.txt") as f:
    print(sum(calculate(reversed([(m.lastgroup, m.group()) for m in op_regex.finditer(i)])) for i in f.readlines()))
