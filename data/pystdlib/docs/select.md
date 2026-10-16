# select

## select.epoll(...)

Returns an epolling object sizehint must be a positive integer or -1 for the default size. The
sizehint is used to optimize internal data structures. It doesn't limit
the maximum number of monitored events.

## select.epoll.close(self, /)

Close the epoll control file descriptor. Further operations on the epoll object will raise an exception.

## select.epoll.fileno(self, /)

Return the epoll control file descriptor.

## select.epoll.fromfd(type, fd, /)

Create an epoll object from a given control fd.

## select.epoll.modify(self, /, fd, eventmask)

Modify event mask for a registered file descriptor. fd
  the target file descriptor of the operation
eventmask
  a bit set composed of the various EPOLL constants

## select.epoll.poll(self, /, timeout=None, maxevents=-1)

timeout
    the maximum time to wait in seconds (as float);
    a timeout of None or -1 makes poll wait indefinitely
  maxevents
    the maximum number of events returned; -1 means no limit

Returns a list containing any descriptors that have events to
report, as a list of (fd, events) 2-tuples.

## select.epoll.register(...)

fd
    the target file descriptor of the operation
  eventmask
    a bit set composed of the various EPOLL constants

The epoll interface supports all file descriptors that support poll.

## select.epoll.unregister(self, /, fd)

Remove a registered file descriptor from the epoll object. fd
  the target file descriptor of the operation

## select.poll()

Returns a polling object. This object supports registering and unregistering file descriptors, and
then polling them for I/O events.

## select.select(rlist, wlist, xlist, timeout=None, /)

The first three arguments are iterables of file descriptors to be waited
for:
rlist -- wait until ready for reading
wlist -- wait until ready for writing
xlist -- wait for an "exceptional condition"
If only one kind of condition is required, pass [] for the other lists.

A file descriptor is either a socket or file object, or a small integer
gotten from a fileno() method call on one of those.

The optional 4th argument specifies a timeout in seconds; it may be
a floating-point number to specify fractions of seconds.  If it is absent
or None, the call will never time out.

The return value is a tuple of three lists corresponding to the first
three arguments; each contains the subset of the corresponding file
descriptors that are ready.

*** IMPORTANT NOTICE ***
On Windows, only sockets are supported; on Unix, all file
descriptors can be used.
