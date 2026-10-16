# itertools

## itertools.accumulate(iterable, func=None, *, initial=None)

Return series of accumulated sums (or other binary function results).

## itertools.batched(iterable, n, *, strict=False)

The last batch may be shorter than n.

Loops over the input iterable and accumulates data into tuples
up to size n.  The input is consumed lazily, just enough to
fill a batch.  The result is yielded as soon as a batch is full
or when the input iterable is exhausted.

>>> for batch in batched('ABCDEFG', 3):
    ...     print(batch)
    ...
    ('A', 'B', 'C')
    ('D', 'E', 'F')
    ('G',)

If "strict" is True, raises a ValueError if the final batch is shorter
than n.

## itertools.chain(*iterables)

Return a chain object whose .__next__() method returns elements from the first iterable until it is exhausted, then elements from the next iterable, until all of the iterables are exhausted.

## itertools.chain.from_iterable(type, iterable, /)

Alternative chain() constructor taking a single iterable argument that evaluates lazily.

## itertools.combinations(iterable, r)

Return successive r-length combinations of elements in the iterable. combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

## itertools.combinations_with_replacement(iterable, r)

Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats. combinations_with_replacement('ABC', 2) --> ('A','A'), ('A','B'), ('A','C'), ('B','B'), ('B','C'), ('C','C')

## itertools.compress(data, selectors)

Return data elements corresponding to true selector elements. Forms a shorter iterator from selected data elements using the selectors
to choose the data elements.

## itertools.count(start=0, step=1)

Return a count object whose .__next__() method returns consecutive values. Equivalent to:
    def count(firstval=0, step=1):
        x = firstval
        while 1:
            yield x
            x += step

## itertools.cycle(iterable, /)

Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.

## itertools.dropwhile(predicate, iterable, /)

Drop items from the iterable while predicate(item) is true. Afterwards, return every element until the iterable is exhausted.

## itertools.filterfalse(function, iterable, /)

Return those items of iterable for which function(item) is false. If function is None, return the items that are false.

## itertools.groupby(iterable, key=None)

iterable
  Elements to divide into groups according to the key function.
key
  A function for computing the group category for each element.
  If the key function is not specified or is None, the element itself
  is used for grouping.

## itertools.islice(...)

Return an iterator whose next() method returns selected values from an
iterable.  If start is specified, will skip all preceding elements;
otherwise, start defaults to zero.  Step defaults to one.  If
specified as another value, step determines how many values are
skipped between successive calls.  Works like a slice() on a list
but returns an iterator.

## itertools.pairwise(iterable, /)

Return an iterator of overlapping pairs taken from the input iterator. s -> (s0,s1), (s1,s2), (s2, s3), ...

## itertools.permutations(iterable, r=None)

Return successive r-length permutations of elements in the iterable. permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)

## itertools.product(*iterables, repeat=1)

Cartesian product of input iterables. Equivalent to nested for-loops.

For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
The leftmost iterators are in the outermost for-loop, so the output tuples
cycle in a manner similar to an odometer (with the rightmost element changing
on every iteration).

To compute the product of an iterable with itself, specify the number
of repetitions with the optional repeat keyword argument. For example,
product(A, repeat=4) means the same as product(A, A, A, A).

product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

## itertools.repeat(...)

repeat(object [,times]) -> create an iterator which returns the object for the specified number of times. If not specified, returns the object endlessly.

## itertools.starmap(function, iterable, /)

Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.

## itertools.takewhile(predicate, iterable, /)

Return successive entries from an iterable as long as the predicate evaluates to true for each entry.

## itertools.tee(iterable, n=2, /)

Returns a tuple of n independent iterators.

## itertools.zip_longest(*iterables, fillvalue=None)

The .__next__() method continues until the longest iterable in the argument sequence is exhausted and then it raises StopIteration. When the shorter iterables are exhausted, the fillvalue is substituted in their place. The fillvalue defaults to None or can be specified by a keyword argument.
