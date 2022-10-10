from dataclasses import dataclass
from __future__ import annotations
from collections import deque
from typing import Iterable


@dataclass
class Knæ:
    parent: Knæ | None
    ben: tuple[int, int] | None
    children: dict[str, Knæ] | int


class SuffixTree:
    root: Knæ

    def bft(self) -> Iterable[tuple[int, int]]:
        kø = deque([self.root])
        while kø:
            match kø.popleft():
                case Knæ(_, ben, child):
                    kø.append(ben)
                    if child is not int:
                        kø.append([child[key] for key in child])
                case tuple(i, j):
                    yield (i, j)
                case _:
                    pass


def construct_suffix_tree(x: str) -> None:
    n = len(x)
    tree = SuffixTree()
    tree.root = Knæ(None, None, {})
    current = tree.root
    for i, char in enumerate(x):
        if char not in current.children:
            current.children[char] = Knæ(current, (i, n), i)
