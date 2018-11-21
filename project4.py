# project4.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

from Indexer import *
from DerivedMultimaps import *
import sys
import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='This is project4 driver.')
    
    parser.add_argument('original', help='Original text file name.')
    parser.add_argument('preprocessed', 
            help='preprocessed file name for indexing.')
    parser.add_argument('--map', dest='mapType', 
            help='Map type used for the multimap.')
    parser.add_argument('--index', dest='indexFile',
            help='File for the indexed output')
    
    args = parser.parse_args()
    
    myIndexer = Indexer(args)
    myIndexer.index()
    
    run = True
    while (run):
        toSearch = input("Enter a word to search for: ")
        toSearch = toSearch.strip('\n')
        myIndexer.search(toSearch)
            
        quit = input("Quit? (y/n): ")
           
        if(quit=='y'):
            run = False
            if(args.indexFile):
                myIndexer.writeIndex()
            else:
                run = False
        else:
            continue
        
            
