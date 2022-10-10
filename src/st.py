import argparse
from tree import Knæ

def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using a suffix tree")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    print(f"Find every reads in {args.reads.name} " +
          f"in genome {args.genome.name}")

def make_suffix_tree(x: str) -> None:
    n = len(x)
    root = Knæ(None, (0,0), {})
    current = root
    for i, char in enumerate(x):
        lam=0
        j=0
        while True:
            if lam==current.ben[1]-current.ben[0] and current.ben[1]!=n-1:
                if x[i] in current.children and x[i]!="$":
                    current=current.children[x[i]]
                    lam=0
                else:
                    current.children[x[i]]=Knæ(current,(i,n-1),i)
                    while current.parent:
                        current=current.parent
                    break
            if x[current.ben[0]+lam]==x[i] and x[i]!="$":
                i+=1
                j+=1
                lam+=1
            else:
                current.parent.children[x[current.ben[0]]]=Knæ(current.parent, (current.ben[0],current.ben[0]+lam-1),{x[current.ben[0]+lam]:current})
                current.parent=current.parent.children[x[current.ben[0]]]
                current.ben=(current.ben[0]+lam,current.ben[1])
                current=current.parent
                current.children[x[i]]=Knæ(current, (i,n-1),i-j)
                while current.parent:
                    current=current.parent
                break

    return current

            
print(make_suffix_tree("BBBABA$"))



if __name__ == '__main__':
    main()
