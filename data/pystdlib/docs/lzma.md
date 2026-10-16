# lzma

## lzma.LZMAFile(filename=None, mode='r', *, format=None, check=-1, preset=None, filters=None)

An LZMAFile can act as a wrapper for an existing file object, or
refer directly to a named file on disk.

Note that LZMAFile provides a *binary* file interface - data read
is returned as bytes, and data to be written must be given as bytes.

## lzma.LZMAFile.close(self)

Flush and close the file. May be called more than once without error. Once the file is
closed, any other operation on it will raise a ValueError.

## lzma.LZMAFile.fileno(self)

Return the file descriptor for the underlying file.

## lzma.LZMAFile.peek(self, size=-1)

Return buffered data without advancing the file position. Always returns at least one byte of data, unless at EOF.
The exact number of bytes returned is unspecified.

## lzma.LZMAFile.read(self, size=-1)

Read up to size uncompressed bytes from the file. If size is negative or omitted, read until EOF is reached.
Returns b"" if the file is already at EOF.

## lzma.LZMAFile.read1(self, size=-1)

Read up to size uncompressed bytes, while trying to avoid making multiple reads from the underlying stream. Reads up to a buffer's worth of data if size is negative.

Returns b"" if the file is at EOF.

## lzma.LZMAFile.readable(self)

Return whether the file was opened for reading.

## lzma.LZMAFile.readline(self, size=-1)

Read a line of uncompressed bytes from the file. The terminating newline (if present) is retained. If size is
non-negative, no more than size bytes will be read (in which
case the line may be incomplete). Returns b'' if already at EOF.

## lzma.LZMAFile.seek(self, offset, whence=0)

Change the file position. The new position is specified by offset, relative to the
position indicated by whence. Possible values for whence are:

0: start of stream (default): offset must not be negative
    1: current stream position
    2: end of stream; offset must not be positive

Returns the new file position.

Note that seeking is emulated, so depending on the parameters,
this operation may be extremely slow.

## lzma.LZMAFile.seekable(self)

Return whether the file supports seeking.

## lzma.LZMAFile.tell(self)

Return the current file position.

## lzma.LZMAFile.writable(self)

Return whether the file was opened for writing.

## lzma.LZMAFile.write(self, data)

Returns the number of uncompressed bytes written, which is
always the length of data in bytes. Note that due to buffering,
the file on disk may not reflect the data written until close()
is called.

## lzma.compress(data, format=1, check=-1, preset=None, filters=None)

Compress a block of data. Refer to LZMACompressor's docstring for a description of the
optional arguments *format*, *check*, *preset* and *filters*.

For incremental compression, use an LZMACompressor instead.

## lzma.decompress(data, format=0, memlimit=None, filters=None)

Decompress a block of data. Refer to LZMADecompressor's docstring for a description of the
optional arguments *format*, *check* and *filters*.

For incremental decompression, use an LZMADecompressor instead.

## lzma.open(filename, mode='rb', *, format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

filename can be either an actual file name (given as a str, bytes,
or PathLike object), in which case the named file is opened, or it
can be an existing file object to read from or write to.

The mode argument can be "r", "rb" (default), "w", "wb", "x", "xb",
"a", or "ab" for binary mode, or "rt", "wt", "xt", or "at" for text
mode.

The format, check, preset and filters arguments specify the
compression settings, as for LZMACompressor, LZMADecompressor and
LZMAFile.

For binary mode, this function is equivalent to the LZMAFile
constructor: LZMAFile(filename, mode, ...). In this case, the
encoding, errors and newline arguments must not be provided.

For text mode, an LZMAFile object is created, and wrapped in an
io.TextIOWrapper instance with the specified encoding, error
handling behavior, and line ending(s).
