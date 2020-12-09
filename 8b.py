from __future__ import annotations
from typing import List
from copy import deepcopy
import re


class Context:
    def __init__(self, opcodes: List[Opcode], acc: int = 0, next_opcode: int = 0):
        self.opcodes = opcodes
        self.acc = acc
        self.next_opcode = next_opcode

    def __repr__(self):
        return f"{self.__class__.__name__}({self.opcodes}, {self.acc}, {self.next_opcode})"

    def __str__(self):
        return f"{self.__class__.__name__}(next={self.opcodes[self.next_opcode]}, {self.acc})"

    def step(self):
        self.opcodes[self.next_opcode].run(self)
        self.next_opcode += 1


class Opcode:
    def __init__(self, arg: int):
        self.arg = arg

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.arg})"

    def run(self, ctx: Context):
        return


class Nop(Opcode):
    pass


class Jmp(Opcode):
    def run(self, ctx: Context):
        ctx.next_opcode += self.arg - 1


class Acc(Opcode):
    def run(self, ctx: Context):
        ctx.acc += self.arg


op_regex = re.compile(r"(acc|jmp|nop) ([+-]\d+)")
opcode_classes = {"acc": Acc, "jmp": Jmp, "nop": Nop}

opcodes = []
with open("8.txt") as f:
    for i in f.readlines():
        opcode, operand = op_regex.match(i).groups()
        opcodes.append(opcode_classes[opcode](int(operand)))

for i, op in enumerate(opcodes):
    if op.name not in {"nop", "jmp"}:
        continue
    ops = deepcopy(opcodes)
    new_op = {"nop": Jmp, "jmp": Nop}[op.name](op.arg)
    ops[i] = new_op
    ctx = Context(ops)
    done = set()
    try:
        while ctx.next_opcode not in done:
            done.add(ctx.next_opcode)
            ctx.step()
    except IndexError:
        print(ctx.acc)