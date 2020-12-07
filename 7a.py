from typing import List, Tuple
import re
from graphviz import Digraph

bag_regex = re.compile(r"(?P<initial_colour>.*? bags? contain )|(?P<bag_type>\d .*? bags?[,.] ?)|(?P<no_other>no other bags.)")


class Bag:
    def __init__(self, colour: str, contains: List[Tuple[int, str]]):
        self.colour = colour
        self.contains = contains

    def __str__(self):
        if self.contains:
            return f"{self.colour} bags contain " + ", ".join(f"{amount} {type} bag{'' if amount == 1 else 's'}" for amount, type in self.contains) + "."
        return f"{self.colour} bags contain no other bags."

    def __contains__(self, item):
        if item in (i[1] for i in self.contains):
            return True
        for amount, type in self.contains:
            if item in rules[type]:
                return True
        return False


rules = {}
with open("7.txt") as f:
    for i in f.readlines():
        match = [(m.lastgroup, m.group()) for m in bag_regex.finditer(i)]
        bag_type = None
        contains = []
        for type, group in match:
            if type == "initial_colour":
                bag_type = group[:-len(" bags contain ")]
            elif type == "no_other":
                pass
            else:
                assert type == "bag_type"
                amount = int(group[0])
                colour = group.strip()[2:-5].strip(" ")
                contains.append((amount, colour))
        assert bag_type
        bag = Bag(bag_type, contains)
        assert str(bag) == i.strip(), (str(bag), i.strip())
        rules[bag.colour] = bag

print(sum("shiny gold" in bag for bag in rules.values()))

"""
graph = Digraph()

for bag in rules.values():
    graph.node(bag.colour, bag.colour)

for bag in rules.values():
    for num, edge in bag.contains:
        graph.edge(edge, bag.colour)

graph.render("day_7.png", view=True)
"""