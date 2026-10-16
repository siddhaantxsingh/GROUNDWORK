# gc

## gc.collect(generation=2)

Run the garbage collector. With no arguments, run a full collection.  The optional argument
may be an integer specifying which generation to collect.  A ValueError
is raised if the generation number is invalid.

The number of unreachable objects is returned.

## gc.disable()

Disable automatic garbage collection.

## gc.enable()

Enable automatic garbage collection.

## gc.freeze()

This can be used before a POSIX fork() call to make the gc copy-on-write
friendly.
Note: collection before a POSIX fork() call may free pages for future
allocation which can cause copy-on-write.

## gc.get_count()

Return a three-tuple of the current collection counts.

## gc.get_debug()

Get the garbage collection debugging flags.

## gc.get_freeze_count()

Return the number of objects in the permanent generation.

## gc.get_objects(generation=None)

generation
    Generation to extract the objects from.

If generation is not None, return only the objects tracked by the
collector that are in that generation.

## gc.get_referents(*objs)

Return the list of objects that are directly referred to by 'objs'.

## gc.get_referrers(*objs)

Return the list of objects that directly refer to any of 'objs'.

## gc.get_stats()

Return a list of dictionaries containing per-generation statistics.

## gc.get_threshold()

Return the current collection thresholds.

## gc.is_finalized(obj, /)

Returns true if the object has been already finalized by the GC.

## gc.is_tracked(obj, /)

Returns true if the object is tracked by the garbage collector. Simple atomic objects will return false.

## gc.isenabled()

Returns true if automatic garbage collection is enabled.

## gc.set_debug(flags, /)

flags
    An integer that can have the following bits turned on:
      DEBUG_STATS - Print statistics during collection.
      DEBUG_COLLECTABLE - Print collectable objects found.
      DEBUG_UNCOLLECTABLE - Print unreachable but uncollectable objects
        found.
      DEBUG_SAVEALL - Save objects to gc.garbage rather than freeing them.
      DEBUG_LEAK - Debug leaking programs (everything but STATS).

Debugging information is written to sys.stderr.

## gc.set_threshold(...)

Setting 'threshold0' to zero disables collection.

## gc.unfreeze()

Unfreeze all objects in the permanent generation. Put all objects in the permanent generation back into oldest generation.
