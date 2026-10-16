# collections

## collections.ChainMap(*maps)

The underlying mappings are stored in a list.  That list is public and can
be accessed or updated using the *maps* attribute.  There is no other
state.

Lookups search the underlying mappings successively until a key is found.
In contrast, writes, updates, and deletions only operate on the first
mapping.

## collections.ChainMap.clear(self)

Clear maps[0], leaving maps[1:] intact.

## collections.ChainMap.copy(self)

New ChainMap or subclass with a new copy of maps[0] and refs to maps[1:]

## collections.ChainMap.fromkeys(...)

Create a new ChainMap with keys from iterable and values set to value.

## collections.ChainMap.new_child(self, m=None, **kwargs)

New ChainMap with a new map followed by all previous maps. If no map is provided, an empty dict is used. Keyword arguments update the map or new empty dict.

## collections.ChainMap.pop(self, key, *args)

Remove *key* from maps[0] and return its value. Raise KeyError if *key* not in maps[0].

## collections.ChainMap.popitem(self)

Remove and return an item pair from maps[0]. Raise KeyError is maps[0] is empty.

## collections.Counter(iterable=None, /, **kwds)

Sometimes called a bag or multiset. Elements are stored as dictionary keys and their counts are stored as dictionary values.

When constructed from a Mapping or Counter, the original object's
values will be used as the initial counts.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string

>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15

>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0

>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9

>>> c.clear()                       # empty the counter
>>> c
Counter()

Note:  If a count is set to zero or reduced to zero, it will remain
in the counter until the entry is deleted or the counter is cleared:

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                     # reduce the count of 'b' by two
>>> c.most_common()                 # 'b' is still in, but its count is zero
[('a', 3), ('c', 1), ('b', 0)]

## collections.Counter.copy(self)

Return a shallow copy.

## collections.Counter.elements(self)

>>> c = Counter('ABCABC')
>>> sorted(c.elements())
['A', 'A', 'B', 'B', 'C', 'C']

Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1

>>> import math
>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> math.prod(prime_factors.elements())
1836

Note, if an element's count has been set to zero or is a negative
number, elements() will ignore it.

## collections.Counter.most_common(self, n=None)

List the n most common elements and their counts from the most common to the least. If n is None, then list all element counts.

>>> Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]

## collections.Counter.subtract(self, iterable=None, /, **kwds)

Counts can be reduced below zero. Both the inputs and outputs are allowed to contain zero and negative counts.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.subtract('witch')             # subtract elements from another iterable
>>> c.subtract(Counter('watch'))    # subtract elements from another counter
>>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
0
>>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
-1

## collections.Counter.total(self)

Sum of the counts

## collections.Counter.update(self, iterable=None, /, **kwds)

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.update('witch')           # add elements from another iterable
>>> d = Counter('watch')
>>> c.update(d)                 # add elements from another counter
>>> c['h']                      # four 'h' in which, witch, and watch
4

## collections.OrderedDict(...)

Dictionary that remembers insertion order

## collections.OrderedDict.clear(self, /)

od.clear() -> None. Remove all items from od.

## collections.OrderedDict.copy(self, /)

od.copy() -> a shallow copy of od

## collections.OrderedDict.fromkeys(type, /, iterable, value=None)

Create a new ordered dictionary with keys from iterable and values set to value.

## collections.OrderedDict.move_to_end(self, /, key, last=True)

Move an existing element to the end (or beginning if last is false). Raise KeyError if the element does not exist.

## collections.OrderedDict.pop(...)

If the key is not found, return the default if given; otherwise, raise a KeyError.

## collections.OrderedDict.popitem(self, /, last=True)

Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order if last is true or FIFO order if
false.

## collections.OrderedDict.setdefault(self, /, key, default=None)

Insert key with a value of default if key is not in the dictionary. Return the value for key if key is in the dictionary, else default.

## collections.UserList(initlist=None)

A more or less complete user-defined wrapper around list objects.

## collections.defaultdict(...)

The default factory is called without arguments to produce
a new value when a key is not present, in __getitem__ only.
A defaultdict compares equal to a dict with the same items.
All remaining arguments are treated the same as if they were
passed to the dict constructor, including keyword arguments.

## collections.defaultdict.copy(self, /)

D.copy() -> a shallow copy of D.

## collections.deque(...)

A list-like sequence optimized for data accesses near its endpoints.

## collections.deque.append(self, item, /)

Add an element to the right side of the deque.

## collections.deque.appendleft(self, item, /)

Add an element to the left side of the deque.

## collections.deque.clear(self, /)

Remove all elements from the deque.

## collections.deque.copy(self, /)

Return a shallow copy of a deque.

## collections.deque.count(self, value, /)

Return number of occurrences of value.

## collections.deque.extend(self, iterable, /)

Extend the right side of the deque with elements from the iterable.

## collections.deque.extendleft(self, iterable, /)

Extend the left side of the deque with elements from the iterable.

## collections.deque.index(...)

Return first index of value. Raises ValueError if the value is not present.

## collections.deque.insert(self, index, value, /)

Insert value before index.

## collections.deque.pop(self, /)

Remove and return the rightmost element.

## collections.deque.popleft(self, /)

Remove and return the leftmost element.

## collections.deque.remove(self, value, /)

Remove first occurrence of value.

## collections.deque.reverse(self, /)

Reverse *IN PLACE*.

## collections.deque.rotate(self, n=1, /)

Rotate the deque n steps to the right. If n is negative, rotates left.

## collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)
