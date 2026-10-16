# linecache

## linecache.checkcache(filename=None)

Discard cache entries that are out of date. (This is not checked upon each call!)

## linecache.clearcache()

Clear the cache entirely.

## linecache.getline(filename, lineno, module_globals=None)

Get a line for a Python source file from the cache. Update the cache if it doesn't contain an entry for this file already.

## linecache.getlines(filename, module_globals=None)

Get the lines for a Python source file from the cache. Update the cache if it doesn't contain an entry for this file already.

## linecache.lazycache(filename, module_globals)

The module loader will be asked for the source only when getlines is
called, not immediately.

If there is an entry in the cache already, it is not altered.

:return: True if a lazy load is registered in the cache,
    otherwise False. To register such a load a module loader with a
    get_source method must be found, the filename must be a cacheable
    filename, and the filename must not be already cached.

## linecache.updatecache(filename, module_globals=None)

Update a cache entry and return its list of lines. If something's wrong, print a message, discard the cache entry, and return an empty list.
