# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from tree import SuffixTree, Knæ

x = 'BBBABA'
p = 'BA'

tree = SuffixTree(x)

print(tree.search_for_pattern(p))
