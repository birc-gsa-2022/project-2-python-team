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

    def bft(self, knæ: Knæ | None = None) -> Iterable[int]:
        kø = deque([])
        if knæ is None:
            kø.append(self.root)
        else:
            kø.append(knæ)
        while kø:
            element = kø.popleft()
            match element:
                case Knæ(_, _, child):
                    if type(child) == int:
                        kø.append(child)
                    else:
                        kø.extend([(child[key]) for key in child])
                case int():
                    yield element
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
