from __future__ import annotations
from collections import deque
from typing import Iterable
from dataclasses import dataclass


@dataclass
class Knæ:
    parent: Knæ | None
    ben: tuple[int, int] | None
    children: dict[str, Knæ] | int


class SuffixTree:
    root: Knæ
    x: str

    def __init__(self, x: str) -> None:
        self.x = x + '$'
        self.root = Knæ(None, (0, 0), {})
        n = len(self.x)
        current = self.root
        for i, _ in enumerate(x):
            lam = 0
            j = 0
            while i < n:
                if lam == current.ben[1]-current.ben[0] and current.ben[1] != n-1:
                    if self.x[i] in current.children:
                        current = current.children[self.x[i]]
                        lam = 0
                    else:
                        current.children[self.x[i]] = Knæ(
                            current, (i, n-1), i-j)
                        current = self.root
                        break
                if x[current.ben[0]+lam] == self.x[i]:
                    i += 1
                    j += 1
                    lam += 1
                else:
                    current.parent.children[self.x[current.ben[0]]] = Knæ(
                        current.parent, (current.ben[0], current.ben[0]+lam), {x[current.ben[0]+lam]: current})
                    current.parent = current.parent.children[self.x[current.ben[0]]]
                    current.ben = (current.ben[0]+lam, current.ben[1])
                    current.parent.children[self.x[i]] = Knæ(
                        current.parent, (i, n-1), i-j)
                    current = self.root
                    break

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

    def search_for_pattern(self, p: str) -> list[int]:
        current = self.root
        P = len(p)
        if P == 0:
            return []
        i = 0
        lam = 0
        while i < P:
            if type(current.children) == int:
                return [current.children]
            elif lam == current.ben[1]-current.ben[0] and p[i] in current.children:
                current = current.children[p[i]]
                lam = 0
            if self.x[current.ben[0]+lam] == p[i]:
                i += 1
                lam += 1
            else:
                return []
        return list(self.bft(current))
