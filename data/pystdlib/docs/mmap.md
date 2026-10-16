# mmap

## mmap.mmap(...)

Maps length bytes from the file specified by the file handle fileno,
and returns a mmap object.  If length is larger than the current size
of the file, the file is extended to contain length bytes.  If length
is 0, the maximum length of the map is the current size of the file,
except that if the file is empty Windows raises an exception (you cannot
create an empty mapping on Windows).

Unix: mmap(fileno, length[, flags[, prot[, access[, offset[, trackfd]]]]])

Maps length bytes from the file specified by the file descriptor fileno,
and returns a mmap object.  If length is 0, the maximum length of the map
will be the current size of the file when mmap is called.
flags specifies the nature of the mapping. MAP_PRIVATE creates a
private copy-on-write mapping, so changes to the contents of the mmap
object will be private to this process, and MAP_SHARED creates a mapping
that's shared with all other processes mapping the same areas of the file.
The default value is MAP_SHARED.

To map anonymous memory, pass -1 as the fileno (both versions).
