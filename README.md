# trees-brgr5525
trees-brgr5525 created by GitHub Classroom

## Modules
To properly clone the repository with the modules make sure that you run:
```
git submodule update --init
```

## Updates
- added file binary_tree.py that contains a basic implementation of a binary tree
- added insert_key_value_pairs.py that will take data and add it to the chosen data structure
- added data text files as well as a shell for generating such files
- added benchmarking shell and data that compares the time it takes for the different structures to run
- added hash_table and avl submodules
- added unit and funtional testing for the two main .py files mentioned above

## Call to program
Arguments:
--data_structure will take one of the following: binary, hash, or avl
--dataset is the name of the file containing your data
--data_points is the number of searches that will be performed for benchmarking

Sample call:
(produces binary tree from sorted data and performs searches on 100 values)
```
insert_key_value_pairs.py \
--data_structure binary \
--dataset sorted.txt \
--data_points 100
```

## Benchmarking
Benchmarking was used to compare the efficiency of the different data structures with regards to inserting data and searching for data both existent and nonexistent within the created database.

Binary Tree (unbalanced):
```
Time to insert all data:              0.03439807891845703
Time to search for existent keys:     0.00012302398681640625
Time to search for nonexistent keys:  0.0002961158752441406
```

AVL Binary Tree (balanced):
```
Time to insert all data:              0.1697368621826172
Time to search for existent keys:     0.0001850128173828125
Time to search for nonexistent keys:  0.00041604042053222656
```

Hash Table:
```
Time to insert all data:              0.06449198722839355
Time to search for existent keys:     0.0001971721649169922
Time to search for nonexistent keys:  0.00023555755615234375
```
The above data represents structures containing 10000 random key values and searching for a small subset (100 keys)

When comparing the time it takes to insert all 10000 data points into the data structure, the binary tree was the fastest. It was almost twice as fast as the hash table and both the binary tree and hash table were considerably faster than the AVL tree. This is likely due to the time spent rebalancing the tree after every node insertion.
All three data structures were fairly comparable when it came to searing for data that already existed within the structure, with the binary tree being just slightly faster and the hash table being the slowest.
However, when looking for data that did not exist in the structure, the hash table performed the best. The binary tree was just slower than the hash table, but then the AVL tree was almost twice as slow. 


The searching times change alot when looking at the benchmarking results of the sorted data set.

Binary Tree (unbalanced):
```
Time to search for existent keys:     0.00020503997802734375
Time to search for nonexistent keys:  0.000885009765625
```

AVL Binary Tree (balanced):
```
Time to search for existent keys:     0.0002238750457763672
Time to search for nonexistent keys:  0.0003039836883544922
```

Hash Table:
```
Time to search for existent keys:     0.00010538101196289062
Time to search for nonexistent keys:  0.0001327991485595703
```
When searching for data that was in the structure, the hash table can be seen as being twice as fast as both of the tree structures. 
The hash table was also the best at searching for data that was nonexistent. It was over twice as fast as the AVL tree and both it and the AVL were significantly faster than the binary tree. 

Differences can also be seen in the relative efficiencies when searching for subsets of 100 vs much larger subset of 9000. The general trends seem to stay the same for the different structures. All the benchmarking data can be found in ```benchmarking.txt``` and further tests could be run using ```benchmarking.sh```. Overall, the hash table structure appeared to be the 'best' in the most situations. 



