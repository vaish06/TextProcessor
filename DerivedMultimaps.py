# DerivedMultimaps.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

from multi_map import *
from avl_tree import *
from unsorted_table_map import *
from sorted_table_map import *
from chain_hash_map import *
from probe_hash_map import *
from splay_tree import *
from red_black_tree import *
import collections

class AvlTreeMultiMap(MultiMap):
    '''Subclass of Multimap with avl tree storage.'''
    _MapType = AVLTreeMap       # Map type;
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    def add(self, k, v):
        super(AvlTreeMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(AvlTreeMultiMap, self).__iter__()
    
    def find(self, k):
        return super(AvlTreeMultiMap, self).find(k)
                
class UnsortedTableMultiMap(MultiMap):
    '''Subclass of Multimap'''
    _MapType = UnsortedTableMap
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    
    def add(self, k, v):
        super(UnsortedTableMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(UnsortedTableMultiMap, self).__iter__()
    
    def find(self, k):
        return super(UnsortedTableMultiMap, self).find(k)
    
class SortedTableMultiMap(MultiMap):
    '''    '''
    _MapType = SortedTableMap
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    def add(self, k, v):
        super(SortedTableMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(SortedTableMultiMap, self).__iter__()
    
    def find(self, k):
        return super(SortedTableMultiMap, self).find(k)

class ChainHashMultiMap(MultiMap):
    '''    '''
    _MapType = ChainHashMap
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
   
    def add(self, k, v):
        super(ChainHashMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(ChainHashMultiMap, self).__iter__()
    
    def find(self, k):
        return super(ChainHashMultiMap, self).find(k)
    
class ProbeHashMultiMap(MultiMap):
    '''    '''
    _MapType = ProbeHashMap
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    
    def add(self, k, v):
        super(ProbeHashMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(ProbeHashMultiMap, self).__iter__()
    
    def find(self, k):
        return super(ProbeHashMultiMap, self).find(k)
        
class SplayTreeMultiMap(MultiMap):
    '''    '''
    _MapType = SplayTreeMap
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    
    def add(self, k, v):
        super(SplayTreeMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(SplayTreeMultiMap, self).__iter__()
    
    def find(self, k):
        return super(SplayTreeMultiMap, self).find(k)
        
class RedBlackTreeMultiMap(MultiMap):
    '''    '''
    _MapType = RedBlackTreeMap
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    
    def add(self, k, v):
        super(RedBlackTreeMultiMap, self).add(k,v)
        
    def __iter__(self):
        super(RedBlackTreeMultiMap, self).__iter__()
    
    def find(self, k):
        return super(RedBlackTreeMultiMap, self).find(k)

class DictMultimap(MultiMap):
    '''    '''
    _MapType = dict
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    
    def add(self, k, v):
        super(DictMultimap, self).add(k,v)
        
    def __iter__(self):
        super(DictMultimap, self).__iter__()
    
    def find(self, k):
        return super(DictMultimap, self).find(k)
        
class ODMultimap(MultiMap):
    '''    '''
    _MapType = collections.OrderedDict 
    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()          # create map instance for storage
        self._n = 0
    
    def add(self, k, v):
        super(ODMultimap, self).add(k,v)
        
    def __iter__(self):
        super(ODMultimap, self).__iter__()
    
    def find(self, k):
        return super(ODMultimap, self).find(k)
 
