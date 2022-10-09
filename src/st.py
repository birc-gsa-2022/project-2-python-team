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
    n = len(n)
    root = Knæ(None, None, {})
    current = root
    for i, char in enumerate(x):
        lam=0
        j=0
        while True:
            # if x[i]=="$":
            #     current.children=i
            #     break
            if lam==current.ben[1]-current.ben[0] or current.ben==None:
                if x[i] in current.children and x[i]!="$":
                    i+=1
                    j+=1
                    lam=0
                    current=current.children[x[i]]
                else:
                    current.children[x[i]]=Knæ(current,(i,n-i-1),i)
                    current=root
                    break
            if x[current.ben[0]+lam]==x[i]:
                i+=1
                j+=1
                lam+=1
            else:                
                current.parent.children[x[current.ben[0]]]=Knæ(current.parent, (current.ben[0],current.ben[0]+lam-1),{x[current.ben[0]+lam]:current})
                current.parent=current.parent.children[x[current.ben[0]]]
                current.ben=(current.ben[0]+lam,current.ben[1])
                current=current.parent
                current.children[x[i]]=Knæ(current, (i,n-i-1),i-j)
                current=root
                break

            
make_suffix_tree("BBBABA")

if __name__ == '__main__':
    main()
