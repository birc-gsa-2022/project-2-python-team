[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8783214&assignment_repo_type=AssignmentRepo)
# Project 2: Suffix tree construction

You should implement a suffix tree construction algorithm. You can choose to implement the naive O(n²)-time construction algorithm as discussed in class or McCreight’s O(n) construction algorithm. After that, implement a search algorithm (similar to slow-scan) for finding all occurrences of a pattern. This algorithm should run in O(m+z) where m is the length of the pattern and z the number of occurrences.

Write a program, `st` using the suffix tree exact pattern search algorithm (similar to slow-scan) to report all indices in a string where a given pattern occurs. 

The program should take the same options as in project 1: `st genome.fa reads.fq`. The program should output (almost) the same SAM file. Because a search in a suffix tree is not done from the start to the end of the string the output might be in a different order, but if you sort the output from the previous project and for this program, they should be identical.

## Evaluation

Implement the tool `st` that does exact pattern matching using a suffix tree. Test it to the best of your abilities, and then fill out the report below.

# Report

## Specify if you have used a linear time or quadratic time algorithm.
We ended up with a quadratic time algorithm, we played around with mccreight, but other projects got the better of us, and ate what little time we had left.

## Insights you may have had while implementing and comparing the algorithms.
Our implementation choice on how to handle leaves (in this case they're just ints) sparked a lengthy yet very enlightening discussion on how we interpret and envision abstract data structure in our minds eye, turns out we each have our differences.  

Packing all our functions into the classes might not be the smartes way of doing this (having the bft as a method under SuffixTree make the usage of the method a bit unintuitive.), but it made importing nice and easy.

## Problems encountered if any.
Other than getting one step closer to enlightenment, most problems we encountered were -as usual- temporary strokes of idiocy on our part (indexing -once again- is hard).
Most difficulties we had were in early implemetation choices for our Knæ class, eg. do we want a dictionary or list implementation, and how do we handled it. How much information do we need in each Knæ, and how do we deal with our choice of ints as leaves. 

## Correctness

*Describe experiments that verifies the correctness of your implementations.*

We could not come up with a good idea for testing just the construction, but if the tree is constructed correctly the search should output the same matches as the naive implementation of exact pattern matching. 
We generated test data and compared outputs from our ST implementation with the naive pattern matching, to verifiy correctness. Furthermore we also tried with empty strings, just in case something went wierd. For palindromes, markov, random and single letter, the output seemed correct. biggest problem was that it was not necessarily in the same order, but we don't care about that.


## Running time

*Describe experiments that verifies that your implementation of `st` uses no more time than O(n) or O(n²) (depending on the algorithm) for constructing the suffix tree and no more than O(m) for searching for a given read in it. Remember to explain your choice of test data. What are “best” and “worst” case inputs?*

*If you have graphs that show the running time--you probably should have--you can embed them here like we did in the previous project.*

We generated 2 series of data for the running time, one series using increasing N (input string length), at three different choices of M (pattern length), the other keeping N constant and varying M. The relation between lines in the resulting plots should reveal the time complexity.

When running the code on strings only consisting of 'A's with varying lengths of sequences we see a clear O(n^2) time complexity for the contruction of trees.

![](figs/identical_contruct.png)

The same time complexity is evident for a Markov-chain-generated string (see data_gen.py, DNA_markov() for generation related details), although it is more dependent of the sequence.

![](figs/markov_construct.png)

When looking at time complexities for the search algorithm the results are more obscure. 

![](identical_search.png)

The time complexity should be O(m) (m being pattern length), but it seems the short inputs run faster. We attribute this to the breath-first-traversal in our implimentation of the search algorithm. If the string is short we have to report many more occurences and thus go though more nodes to get there. The same pattern is seen for a markov-chain-generated sequence as shown below.

![](figs/markov_search.png)

Here the shortest pattern appears often in the sequence, and thus takes much longer to report.








