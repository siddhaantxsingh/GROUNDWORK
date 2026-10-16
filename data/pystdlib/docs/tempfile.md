# tempfile

## tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None, delete_on_close=True)

Create and return a temporary file. Arguments: 'prefix', 'suffix', 'dir' -- as for mkstemp. 'mode' -- the mode argument to io.open (default "w+b"). 'buffering' -- the buffer size argument to io.open (default -1). 'encoding' -- the encoding argument to io.open (default None) 'newline' -- the newline argument to io.open (default None) 'delete' -- whether the file is automatically deleted (default True). 'delete_on_close' -- if 'delete', whether the file is deleted on close (default True) or otherwise either on context manager exit (if context manager was used) or on object finalization. . 'errors' -- the errors argument to io.open (default None) The file is created as mkstemp() would do it.

Returns an object with a file-like interface; the name of the file
is accessible as its 'name' attribute.  The file will be automatically
deleted when it is closed unless the 'delete' argument is set to False.

On POSIX, NamedTemporaryFiles cannot be automatically deleted if
the creating process is terminated abruptly with a SIGKILL signal.
Windows can delete the file even in this case.

## tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

Temporary file wrapper, specialized to switch from BytesIO or StringIO to a real file when it exceeds a certain size or when a fileno is needed.

## tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None, ignore_cleanup_errors=False, *, delete=True)

This has the same behavior as mkdtemp but can be used as a context manager. For example:

with TemporaryDirectory() as tmpdir:
        ...

Upon exiting the context, the directory and everything contained
in it are removed (unless delete=False is passed or an exception
is raised during cleanup and ignore_cleanup_errors is not True).

Optional Arguments:
    suffix - A str suffix for the directory name.  (see mkdtemp)
    prefix - A str prefix for the directory name.  (see mkdtemp)
    dir - A directory to create this temp dir in.  (see mkdtemp)
    ignore_cleanup_errors - False; ignore exceptions during cleanup?
    delete - True; whether the directory is automatically deleted.

## tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

Create and return a temporary file. Arguments: 'prefix', 'suffix', 'dir' -- as for mkstemp. 'mode' -- the mode argument to io.open (default "w+b"). 'buffering' -- the buffer size argument to io.open (default -1). 'encoding' -- the encoding argument to io.open (default None) 'newline' -- the newline argument to io.open (default None) 'errors' -- the errors argument to io.open (default None) The file is created as mkstemp() would do it.

Returns an object with a file-like interface.  The file has no
name, and will cease to exist when it is closed.

## tempfile.gettempdir()

Returns tempfile.tempdir as str.

## tempfile.gettempdirb()

Returns tempfile.tempdir as bytes.

## tempfile.gettempprefix()

The default prefix for temporary directories as string.

## tempfile.gettempprefixb()

The default prefix for temporary directories as bytes.

## tempfile.mkdtemp(suffix=None, prefix=None, dir=None)

The return value is the pathname of the directory.

Arguments are as for mkstemp, except that the 'text' argument is
not accepted.

The directory is readable, writable, and searchable only by the
creating user.

Caller is responsible for deleting the directory when done with it.

## tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)

The return value is a pair (fd, name) where fd is the file descriptor returned by os.open, and name is the filename.

If 'suffix' is not None, the file name will end with that suffix,
otherwise there will be no suffix.

If 'prefix' is not None, the file name will begin with that prefix,
otherwise a default prefix is used.

If 'dir' is not None, the file will be created in that directory,
otherwise a default directory is used.

If 'text' is specified and true, the file is opened in text
mode.  Else (the default) the file is opened in binary mode.

If any of 'suffix', 'prefix' and 'dir' are not None, they must be the
same type.  If they are bytes, the returned name will be bytes; str
otherwise.

The file is readable and writable only by the creating user ID.
If the operating system uses permission bits to indicate whether a
file is executable, the file is executable by no one. The file
descriptor is not inherited by children of this process.

Caller is responsible for deleting the file when done with it.

## tempfile.mktemp(suffix='', prefix='tmp', dir=None)

The file is not created.

Arguments are similar to mkstemp, except that the 'text' argument is
not accepted, and suffix=None, prefix=None and bytes file names are not
supported.

THIS FUNCTION IS UNSAFE AND SHOULD NOT BE USED.  The file name may
refer to a file that did not exist at some point, but by the time
you get around to creating it, someone else may have beaten you to
the punch.
