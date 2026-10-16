# heapq

## heapq.merge(*iterables, key=None, reverse=False)

Similar to sorted(itertools.chain(*iterables)) but returns a generator,
does not pull the data into memory all at once, and assumes that each of
the input streams is already sorted (smallest to largest).

>>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
[0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

If *key* is not None, applies a key function to each element to determine
its sort order.

>>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
['dog', 'cat', 'fish', 'horse', 'kangaroo']

## heapq.nlargest(n, iterable, key=None)

Find the n largest elements in a dataset. Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]

## heapq.nsmallest(n, iterable, key=None)

Find the n smallest elements in a dataset. Equivalent to:  sorted(iterable, key=key)[:n]
