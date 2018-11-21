# Indexer.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

from DerivedMultimaps import *
import time
import string

class Indexer():
    '''This class indexes the preprocessed text into a map.'''
    
    def __init__(self, args):
        self._original = args.original
        self._preprocessed = args.preprocessed
        if args.mapType:
            self._mapType = args.mapType
        else:
            self._mapType = "avl"
        if args.indexFile:
            self._indexFile = args.indexFile
        self._map = AvlTreeMultiMap()
            
    def createMap(self):
        if self._mapType:
            if (self._mapType == "avl"):
                self._map = AvlTreeMultiMap()
            elif (self._mapType == "unsorted"):
                self._map = UnsortedTableMultiMap()
            elif (self._mapType == "sorted"):
                self._map = SortedTableMultiMap()
            elif (self._mapType == "chain"):
                self._map = ChainHashMultiMap()
            elif (self._mapType == "probe"):
                self._map = ProbeHashMultiMap()
            elif (self._mapType == "splay"):
                self._map = SplayTreeMultiMap()
            elif (self._mapType == "rb"):
                self._map = RedBlackTreeMultiMap()
            elif (self._mapType == "dict"):
                self._map = DictMultimap()
            else:
                self._map = ODMultimap()
        else:
            self._map = AvlTreeMultiMap()
    
    def index(self):
        freq = {}
        start = time.time()
        self.createMap()
        infile = open(self._preprocessed, 'r')
        lineNum = 0
        for line in infile:
            lineNum += 1
            tmp=[word.strip() for word in (line.split(" "))]
            for word in tmp:
                self._map.add(word, lineNum)
                freq[word] = 1 + freq.get(word, 0)              
        end = time.time()
        timeIndex = end - start
        count = 0
        f = []
        for(w,c) in freq.items():
            count += c
            f.append(c)
        average = count / len(freq)
        f.sort()
        median = f[int(len(f)/2)]
        self.printStats(timeIndex, average, median)
        
    def printStats(self, timeIndex, average, median):
        print ("---------------------------------------")
        print ("Stats for {}".format(self._original))
        print ("Index took {:.2f} seconds to create.".format(timeIndex))
        print ("Map type used for indexing: {:>11}".format(self._mapType))
        print ("Total number of indexed terms: {:>8}".format(len(self._map)))
        print ("Average word frequency: {:15.2f}".format(average))
        print ("Median word frequency: {:>16}".format(median))
        print ("---------------------------------------")
        
    def search(self, k):
        if(self._map.find(k)):
            startF = time.time()
            values = self._map.find(k)
            infile = open(self._original, 'r')
            lineNum = 0
            index = 0
            print ("\nLines from the original text containing {}:".format(k))
            for line in infile:
                lineNum += 1
                if (values[index] == lineNum):
                    print(line)
                    if(index < len(values)-1):
                        index += 1
                    else:
                        break
            endF = time.time()
            print ("Number of occurances of {}: {}".format(k, len(values)))
            timeFind = endF - startF
            print ("Index took {:.4f} seconds to find.".format(timeFind)) 
            
    
    def writeIndex(self):
        outfile = open(self._indexFile, 'w')
        p = self._map._map.first()
        p = self._map._map.after(p)
        while p is not None:
            outfile.write(p.key()+' '
                + ', '.join(str(v) for v in p.value())+"\n")
            p = self._map._map.after(p)