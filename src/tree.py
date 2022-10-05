from dataclasses import dataclass
from __future__ import annotations


@dataclass
class Knæ:
    parent: Knæ | None
    ben: tuple[int, int] | None
    children: dict[str, Knæ] | int


class SuffixTree:
    root: Knæ | None

    def construct(self, x: str) -> None:
        n = len(n)
        self.root = Knæ(None, None, {})
        current = self.root
        for i, char in enumerate(x):
            if char not in current.children:
                current.children[char] = Knæ(current, (i, n), i)
