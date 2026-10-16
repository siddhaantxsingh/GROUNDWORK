# io

## io.BufferedIOBase()

The main difference with RawIOBase is that the read() method
supports omitting the size argument, and does not have a default
implementation that defers to readinto().

In addition, read(), readinto() and write() may raise
BlockingIOError if the underlying raw stream is in non-blocking
mode and not ready; unlike their raw counterparts, they will never
return None.

A typical implementation should not inherit from a RawIOBase
implementation, but wrap one.

## io.IOBase()

This class provides dummy implementations for many methods that
derived classes can override selectively; the default implementations
represent a file that cannot be read, written or seeked.

Even though IOBase does not declare read, readinto, or write because
their signatures will vary, implementations and clients should
consider those methods part of the interface. Also, implementations
may raise UnsupportedOperation when operations they do not support are
called.

The basic type used for binary data read from or written to a file is
bytes. Other bytes-like objects are accepted as method arguments too.
In some cases (such as readinto), a writable object is required. Text
I/O classes work with str data.

Note that calling any method (except additional calls to close(),
which are ignored) on a closed stream should raise a ValueError.

IOBase (and its subclasses) support the iterator protocol, meaning
that an IOBase object can be iterated over yielding the lines in a
stream.

IOBase also supports the :keyword:`with` statement. In this example,
fp is closed after the suite of the with statement is complete:

with open('spam.txt', 'r') as fp:
    fp.write('Spam and eggs!')

## io.RawIOBase()

Base class for raw binary I/O.

## io.TextIOBase()

Base class for text I/O. This class provides a character and line based interface to stream
I/O. There is no readinto method because Python's character strings
are immutable.
