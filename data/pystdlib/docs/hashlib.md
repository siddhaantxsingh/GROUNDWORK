# hashlib

## hashlib.file_digest(fileobj, digest, /, *, _bufsize=262144)

Returns a digest object.

*fileobj* must be a file-like object opened for reading in binary mode.
It accepts file objects from open(), io.BytesIO(), and SocketIO objects.
The function may bypass Python's I/O and use the file descriptor *fileno*
directly.

*digest* must either be a hash algorithm name as a *str*, a hash
constructor, or a callable that returns a hash object.

## hashlib.new(name, *args, **kwargs)

new(name, data=b'') - Return a new hashing object using the named algorithm; optionally initialized with data (which must be a bytes-like object).
