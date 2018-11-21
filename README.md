# TextProcessor
Text Processor using Binary Trees
Description:

This project takes a text file, preprocesses it in a preprocessor module, and then indexes unique words from the preprocessed file using map data structures. 

Dependencies:
Files written by me:
- project4.py
- Indexer.py
- DerivedMultimaps.py

Files used in this project:
- multi_map.py
- avl_tree.py
- unsorted_table_map.py
- sorted_table_map.py
- chain_hash_map.py
- probe_hash_map.py
- splay_tree.py
- red_black_tree.py



Requirements:

- Python 3

- time
- sys
- collections
- string
- argparse
input files: 
- orginal text 
- preprocessed text 
- optional _MapType 
- optional index output 

Run as:
 python3 project4.py <original> <preprocessed> <--map map> <--index index>


Output:

Stats for SomeNovel.txt
Index took 13.25 seconds to create.
Total number of indexed terms:     53241
Average word frequency:             5.57
Median word frequency:                 4
