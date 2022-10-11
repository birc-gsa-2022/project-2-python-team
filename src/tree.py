from __future__ import annotations
from collections import deque
from typing import Iterable
from dataclasses import dataclass

from st import make_suffix_tree


@dataclass
class Knæ:
    parent: Knæ | None
    ben: tuple[int, int] | None
    children: dict[str, Knæ] | int


class SuffixTree:
    root: Knæ

    def bft(self) -> Iterable[int]:
        kø = deque([])
        kø.append(self.root)
        while kø:
            element = kø.popleft()
            match element:
                case Knæ(_, _, child):
                    print("er knæ")
                    if type(child) == int:
                        print("er int")
                        kø.append(child)
                    else:
                        print("ikke int")
                        kø.extend([(child[key]) for key in child])
                case int():
                    yield element
                case _:
                    pass
            print(kø)


def construct_suffix_tree(x: str) -> None:
    n = len(x)
    tree = SuffixTree()
    tree.root = Knæ(None, None, {})
    current = tree.root
    for i, char in enumerate(x):
        if char not in current.children:
            current.children[char] = Knæ(current, (i, n), i)
