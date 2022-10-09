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
            if char in current.children:
                lam=0
                j=0
                while True:
                    if lam==current.ben[1]:
                        lam=0
                        if x[i+j] in current.children:
                            current=current.children[x[i+j]]
                        else:
                            current.children[x[i+j]]=Knæ(current,(j),{})
                    if x[current.ben[0]+lam]==x[i+j]:
                        j+=1
                        lam+=1
                    else:

                    

            



                    
                            
