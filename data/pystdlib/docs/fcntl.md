# fcntl

## fcntl.fcntl(fd, cmd, arg=0, /)

The values used for cmd are operating system dependent, and are
available as constants in the fcntl module, using the same names as used
in the relevant C header files.  The argument arg is optional, and
defaults to 0; it may be an integer, a bytes-like object or a string.
If arg is given as a string, it will be encoded to binary using the
UTF-8 encoding.

If the arg given is an integer or if none is specified, the result value
is an integer corresponding to the return value of the fcntl() call in
the C code.

If arg is given as a bytes-like object, the return value of fcntl() is a
bytes object of that length, containing the resulting value put in the
arg buffer by the operating system.  The length of the arg buffer is not
allowed to exceed 1024 bytes.

## fcntl.flock(fd, operation, /)

Perform the lock operation on file descriptor fd. See the Unix manual page for flock(2) for details (On some systems, this
function is emulated using fcntl()).

## fcntl.ioctl(fd, request, arg=0, mutate_flag=True, /)

The values used for request are operating system dependent, and are
available as constants in the fcntl or termios library modules, using
the same names as used in the relevant C header files.

The argument arg is optional, and defaults to 0; it may be an integer, a
bytes-like object or a string.  If arg is given as a string, it will be
encoded to binary using the UTF-8 encoding.

If the arg given is an integer or if none is specified, the result value
is an integer corresponding to the return value of the ioctl() call in
the C code.

If the argument is a mutable buffer (such as a bytearray) and the
mutate_flag argument is true (default) then the buffer is (in effect)
passed to the operating system and changes made by the OS will be
reflected in the contents of the buffer after the call has returned.
The return value is the integer returned by the ioctl() system call.

If the argument is a mutable buffer and the mutable_flag argument is
false, the behavior is as if an immutable buffer had been passed.

If the argument is an immutable buffer then a copy of the buffer is
passed to the operating system and the return value is a bytes object of
the same length containing whatever the operating system put in the
buffer.  The length of the arg buffer in this case is not allowed to
exceed 1024 bytes.

## fcntl.lockf(fd, cmd, len=0, start=0, whence=0, /)

fd is the file descriptor of the file to lock or unlock, and operation
is one of the following values:

LOCK_UN - unlock
    LOCK_SH - acquire a shared lock
    LOCK_EX - acquire an exclusive lock

When operation is LOCK_SH or LOCK_EX, it can also be bitwise ORed with
LOCK_NB to avoid blocking on lock acquisition.  If LOCK_NB is used and
the lock cannot be acquired, an OSError will be raised and the exception
will have an errno attribute set to EACCES or EAGAIN (depending on the
operating system -- for portability, check for either value).

len is the number of bytes to lock, with the default meaning to lock to
EOF.  start is the byte offset, relative to whence, to that the lock
starts.  whence is as with fileobj.seek(), specifically:

0 - relative to the start of the file (SEEK_SET)
    1 - relative to the current buffer position (SEEK_CUR)
    2 - relative to the end of the file (SEEK_END)
