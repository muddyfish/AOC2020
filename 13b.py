with open("13.txt") as f:
    f.readline()
    busses = sorted(((int(i), j) for j, i in enumerate(f.readline().split(",")) if i != "x"), reverse=True)


def str_constraint(every: int, offset: int) -> str:
    if offset:
        return f"(x-{every-offset}) mod {every}"
    return f"(x-0) mod {every}"


print(" = ".join(str_constraint(*i) for i in busses) + " = 0")
