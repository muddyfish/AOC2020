import re


op_regex = re.compile(
    r"(?P<num>\d+)|"
    r"(?P<op>[+*])|"
    r"(?P<close_bracket>\()|"
    r"(?P<open_bracket>\))"
)


def calculate(iterator) -> int:
    def inner(cur, iterator) -> int:
        op_1 = get_op_1(cur, iterator)
        op_type, op = next(iterator, ("close_bracket", ")"))
        if op_type == "close_bracket":
            return op_1
        assert op_type == "op"
        return run_op(op_1, op, iterator)

    def get_op_1(cur, iterator) -> int:
        operator, operand = cur
        if operator == "num":
            return int(operand)
        elif operator == "open_bracket":
            return inner(next(iterator), iterator)
        else:
            assert False

    def run_op(op_1, op, iterator) -> int:
        if op == "+":
            op_2 = get_op_1(next(iterator), iterator)
            return inner(("num", eval(f"{op_1} {op} {op_2}")), iterator)
        else:
            op_2 = calculate(iterator)
            return eval(f"{op_1} {op} {op_2}")

    return inner(next(iterator), iterator)


with open("18.txt") as f:
    print(sum(calculate(reversed([(m.lastgroup, m.group()) for m in op_regex.finditer(i)])) for i in f.readlines()))
