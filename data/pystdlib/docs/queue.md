# queue

## queue.Full(...)

Exception raised by Queue.put(block=0)/put_nowait().

## queue.LifoQueue(maxsize=0)

Variant of Queue that retrieves most recently added entries first.

## queue.PriorityQueue(maxsize=0)

Variant of Queue that retrieves open entries in priority order (lowest first). Entries are typically tuples of the form:  (priority number, data).

## queue.Queue(maxsize=0)

Create a queue object with a given maximum size. If maxsize is <= 0, the queue size is infinite.

## queue.Queue.empty(self)

This method is likely to be removed at some point.  Use qsize() == 0
as a direct substitute, but be aware that either approach risks a race
condition where a queue can grow before the result of empty() or
qsize() can be used.

To create code that needs to wait for all queued tasks to be
completed, the preferred technique is to use the join() method.

## queue.Queue.full(self)

This method is likely to be removed at some point.  Use qsize() >= n
as a direct substitute, but be aware that either approach risks a race
condition where a queue can shrink before the result of full() or
qsize() can be used.

## queue.Queue.get(self, block=True, timeout=None)

If optional args 'block' is true and 'timeout' is None (the default),
block if necessary until an item is available. If 'timeout' is
a non-negative number, it blocks at most 'timeout' seconds and raises
the Empty exception if no item was available within that time.
Otherwise ('block' is false), return an item if one is immediately
available, else raise the Empty exception ('timeout' is ignored
in that case).

Raises ShutDown if the queue has been shut down and is empty,
or if the queue has been shut down immediately.

## queue.Queue.get_nowait(self)

Remove and return an item from the queue without blocking. Only get an item if one is immediately available. Otherwise
raise the Empty exception.

## queue.Queue.join(self)

The count of unfinished tasks goes up whenever an item is added to the
queue. The count goes down whenever a consumer thread calls task_done()
to indicate the item was retrieved and all work on it is complete.

When the count of unfinished tasks drops to zero, join() unblocks.

## queue.Queue.put(self, item, block=True, timeout=None)

If optional args 'block' is true and 'timeout' is None (the default),
block if necessary until a free slot is available. If 'timeout' is
a non-negative number, it blocks at most 'timeout' seconds and raises
the Full exception if no free slot was available within that time.
Otherwise ('block' is false), put an item on the queue if a free slot
is immediately available, else raise the Full exception ('timeout'
is ignored in that case).

Raises ShutDown if the queue has been shut down.

## queue.Queue.put_nowait(self, item)

Put an item into the queue without blocking. Only enqueue the item if a free slot is immediately available.
Otherwise raise the Full exception.

## queue.Queue.qsize(self)

Return the approximate size of the queue (not reliable!).

## queue.Queue.shutdown(self, immediate=False)

By default, gets will only raise once the queue is empty. Set
'immediate' to True to make gets raise immediately instead.

All blocked callers of put() and get() will be unblocked.

If 'immediate', the queue is drained and unfinished tasks
is reduced by the number of drained tasks.  If unfinished tasks
is reduced to zero, callers of Queue.join are unblocked.

## queue.Queue.task_done(self)

Used by Queue consumer threads.  For each get() used to fetch a task,
a subsequent call to task_done() tells the queue that the processing
on the task is complete.

If a join() is currently blocking, it will resume when all items
have been processed (meaning that a task_done() call was received
for every item that had been put() into the queue).

Raises a ValueError if called more times than there were items
placed in the queue.

## queue.ShutDown(...)

Raised when put/get with shut-down queue.
