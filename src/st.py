import argparse
from tree import Knæ, SuffixTree
from parsers import parse_fasta, parse_fastq


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using a suffix tree")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    print(f"Find every reads in {args.reads.name} " +
          f"in genome {args.genome.name}")

    genome = parse_fasta(args.genome)
    reads = parse_fastq(args.reads)

    out = []
    for chr in genome:
        tree = SuffixTree(genome[chr])
        for read in reads:
            hits = tree.search_for_pattern(reads[read])
            if hits:
                for hit in hits:
                    out.append(
                        f'{read}\t{chr}\t{hit+1}\t{len(reads[read])}M\t{reads[read]}')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
