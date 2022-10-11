import argparse
from tree import SuffixTree, Knæ

def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using a suffix tree")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    print(f"Find every reads in {args.reads.name} " +
          f"in genome {args.genome.name}")

def make_suffix_tree(x: str) -> SuffixTree:
    n = len(x)
    tree=SuffixTree()
    root = Knæ(None, (0,0), {})
    current = root
    for i, char in enumerate(x):
        lam=0
        j=0
        while i<n:
            if lam==current.ben[1]-current.ben[0] and current.ben[1]!=n-1:
                if x[i] in current.children:
                    current=current.children[x[i]]
                    lam=0
                else:
                    current.children[x[i]]=Knæ(current,(i,n-1),i-j)
                    current=root
                    break
            if x[current.ben[0]+lam]==x[i]:
                i+=1
                j+=1
                lam+=1
            else:
                current.parent.children[x[current.ben[0]]]=Knæ(current.parent, (current.ben[0],current.ben[0]+lam),{x[current.ben[0]+lam]:current})
                current.parent=current.parent.children[x[current.ben[0]]]
                current.ben=(current.ben[0]+lam,current.ben[1])
                current.parent.children[x[i]]=Knæ(current.parent, (i,n-1), i-j)
                current=root
                break
    tree.root=root
    return tree

def search_for_Knæ(tree:SuffixTree,x:str,p:str) -> Knæ:
    current=tree.root
    P=len(p)
    i=0
    lam=0
    while i<P:
            if lam==current.ben[1]-current.ben[0] and p[i] in current.children:
                current=current.children[p[i]]
                lam=0
            if x[current.ben[0]+lam]==p[i]:
                i+=1
                lam+=1
            else:
                return None
    return current




if __name__ == '__main__':
    x="BB$"
    yes=make_suffix_tree("BB$")
    print(yes)
    print(search_for_Knæ(yes,x,"B"))
