# gzip

## gzip.BadGzipFile(...)

Exception raised in some cases for invalid gzip files.

## gzip.GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None)

The GzipFile class simulates most of the methods of a file object with the exception of the truncate() method. This class only supports opening files in binary mode.  If you need to
open a compressed file in text mode, use the gzip.open() function.

## gzip.GzipFile.fileno(self)

Invoke the underlying file object's fileno() method. This will raise AttributeError if the underlying file object
doesn't support fileno().

## gzip.GzipFile.read1(self, size=-1)

Implements BufferedIOBase.read1() Reads up to a buffer's worth of data if size is negative.

## gzip.GzipFile.rewind(self)

Return the uncompressed stream file position indicator to the beginning of the file

## gzip.compress(data, compresslevel=9, *, mtime=None)

compresslevel sets the compression level in range of 0-9.
mtime can be used to set the modification time. The modification time is
set to the current time by default.

## gzip.decompress(data)

Decompress a gzip compressed string in one shot. Return the decompressed string.

## gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)

The filename argument can be an actual filename (a str or bytes object),
or an existing file object to read from or write to.

The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab"
for binary mode, or "rt", "wt", "xt" or "at" for text mode.  The default
mode is "rb", and the default compresslevel is 9.

For binary mode, this function is equivalent to the GzipFile
constructor: GzipFile(filename, mode, compresslevel).  In this case,
the encoding, errors and newline arguments must not be provided.

For text mode, a GzipFile object is created, and wrapped in an
io.TextIOWrapper instance with the specified encoding, error handling
behavior, and line ending(s).
