# tarfile

## tarfile.CompressionError(...)

Exception for unavailable compression methods.

## tarfile.EOFHeaderError(...)

Exception for end of file headers.

## tarfile.EmptyHeaderError(...)

Exception for empty headers.

## tarfile.ExtractError(...)

General exception for extract errors.

## tarfile.HeaderError(...)

Base exception for header errors.

## tarfile.InvalidHeaderError(...)

Exception for invalid headers.

## tarfile.ReadError(...)

Exception for unreadable tar archives.

## tarfile.StreamError(...)

Exception for unsupported operations on stream-like TarFiles.

## tarfile.SubsequentHeaderError(...)

Exception for missing and invalid extended headers.

## tarfile.TarError(...)

Base exception.

## tarfile.TarFile(name=None, mode='r', fileobj=None, format=None, tarinfo=None, dereference=None, ignore_zeros=None, encoding=None, errors='surrogateescape', pax_headers=None, debug=None, errorlevel=None, copybufsize=None, stream=False)

The TarFile Class provides an interface to tar archives.

## tarfile.TarFile.add(self, name, arcname=None, recursive=True, *, filter=None)

If given, `arcname' specifies an alternative name for the file in the archive. Directories are added recursively by default. This can be avoided by setting `recursive' to False. `filter' is a function that expects a TarInfo object argument and returns the changed TarInfo object, if it returns None the TarInfo object will be excluded from the archive.

## tarfile.TarFile.addfile(self, tarinfo, fileobj=None)

If `tarinfo' represents a non zero-size regular file, the `fileobj'
argument should be a binary file, and tarinfo.size bytes are read
from it and added to the archive. You can create TarInfo objects
directly, or by using gettarinfo().

## tarfile.TarFile.bz2open(...)

Open bzip2 compressed tar archive name for reading or writing. Appending is not allowed.

## tarfile.TarFile.chmod(self, tarinfo, targetpath)

Set file permissions of targetpath according to tarinfo.

## tarfile.TarFile.chown(self, tarinfo, targetpath, numeric_owner)

Set owner of targetpath according to tarinfo. If numeric_owner is True, use .gid/.uid instead of .gname/.uname. If numeric_owner is False, fall back to .gid/.uid when the search based on name fails.

## tarfile.TarFile.close(self)

Close the TarFile. In write-mode, two finishing zero blocks are appended to the archive.

## tarfile.TarFile.extract(self, member, path='', set_attrs=True, *, numeric_owner=False, filter=None)

Extract a member from the archive to the current working directory, using its full name. Its file information is extracted as accurately as possible. `member' may be a filename or a TarInfo object. You can specify a different directory using `path'. File attributes (owner, mtime, mode) are set unless `set_attrs' is False. If `numeric_owner` is True, only the numbers for user/group names are used and not the names.

The `filter` function will be called before extraction.
It can return a changed TarInfo or None to skip the member.
String names of common filters are accepted.

## tarfile.TarFile.extractall(self, path='.', members=None, *, numeric_owner=False, filter=None)

If `numeric_owner` is True, only the numbers for user/group names are used and not the names.

The `filter` function will be called on each member just
before extraction.
It can return a changed TarInfo or None to skip the member.
String names of common filters are accepted.

## tarfile.TarFile.extractfile(self, member)

If `member' is a regular file or a link, an io.BufferedReader object is returned. For all other existing members, None is returned. If `member' does not appear in the archive, KeyError is raised.

## tarfile.TarFile.getmember(self, name)

If `name' can not be found in the archive, KeyError is raised. If a member occurs more than once in the archive, its last occurrence is assumed to be the most up-to-date version.

## tarfile.TarFile.getmembers(self)

Return the members of the archive as a list of TarInfo objects. The list has the same order as the members in the archive.

## tarfile.TarFile.getnames(self)

Return the members of the archive as a list of their names. It has the same order as the list returned by getmembers().

## tarfile.TarFile.gettarinfo(self, name=None, arcname=None, fileobj=None)

The file is either named by `name', or specified as a file object `fileobj' with a file descriptor. If given, `arcname' specifies an alternative name for the file in the archive, otherwise, the name is taken from the 'name' attribute of 'fileobj', or the 'name' argument. The name should be a text string.

## tarfile.TarFile.gzopen(...)

Open gzip compressed tar archive name for reading or writing. Appending is not allowed.

## tarfile.TarFile.list(self, verbose=True, *, members=None)

If `verbose' is False, only the names of the members are printed.
If it is True, an `ls -l'-like output is produced. `members' is
optional and must be a subset of the list returned by getmembers().

## tarfile.TarFile.makedev(self, tarinfo, targetpath)

Make a character or block device called targetpath.

## tarfile.TarFile.makedir(self, tarinfo, targetpath)

Make a directory called targetpath.

## tarfile.TarFile.makefifo(self, tarinfo, targetpath)

Make a fifo called targetpath.

## tarfile.TarFile.makefile(self, tarinfo, targetpath)

Make a file called targetpath.

## tarfile.TarFile.makelink_with_filter(self, tarinfo, targetpath, filter_function, extraction_root)

If it cannot be created (platform limitation), we try to make a copy of the referenced file instead of a link.

filter_function is only used when extracting a *different*
member (e.g. as fallback to creating a link).

## tarfile.TarFile.makeunknown(self, tarinfo, targetpath)

Make a file from a TarInfo object with an unknown type at targetpath.

## tarfile.TarFile.next(self)

Return the next member of the archive as a TarInfo object, when TarFile is opened for reading. Return None if there is no more available.

## tarfile.TarFile.open(...)

Return an appropriate TarFile class.

mode:
'r' or 'r:*' open for reading with transparent compression
'r:'         open for reading exclusively uncompressed
'r:gz'       open for reading with gzip compression
'r:bz2'      open for reading with bzip2 compression
'r:xz'       open for reading with lzma compression
'a' or 'a:'  open for appending, creating the file if necessary
'w' or 'w:'  open for writing without compression
'w:gz'       open for writing with gzip compression
'w:bz2'      open for writing with bzip2 compression
'w:xz'       open for writing with lzma compression

'x' or 'x:'  create a tarfile exclusively without compression, raise
             an exception if the file is already created
'x:gz'       create a gzip compressed tarfile, raise an exception
             if the file is already created
'x:bz2'      create a bzip2 compressed tarfile, raise an exception
             if the file is already created
'x:xz'       create an lzma compressed tarfile, raise an exception
             if the file is already created

'r|*'        open a stream of tar blocks with transparent compression
'r|'         open an uncompressed stream of tar blocks for reading
'r|gz'       open a gzip compressed stream of tar blocks
'r|bz2'      open a bzip2 compressed stream of tar blocks
'r|xz'       open an lzma compressed stream of tar blocks
'w|'         open an uncompressed stream for writing
'w|gz'       open a gzip compressed stream for writing
'w|bz2'      open a bzip2 compressed stream for writing
'w|xz'       open an lzma compressed stream for writing

## tarfile.TarFile.taropen(...)

Open uncompressed tar archive name for reading or writing.

## tarfile.TarFile.utime(self, tarinfo, targetpath)

Set modification time of targetpath according to tarinfo.

## tarfile.TarFile.xzopen(...)

Open lzma compressed tar archive name for reading or writing. Appending is not allowed.

## tarfile.TarInfo(name='')

Informational class which holds the details about an archive member given by a tar header block. TarInfo objects are returned by TarFile.getmember(), TarFile.getmembers() and TarFile.gettarinfo() and are usually created internally.

## tarfile.TarInfo.create_gnu_header(self, info, encoding, errors)

Return the object as a GNU header block sequence.

## tarfile.TarInfo.create_pax_global_header(...)

Return the object as a pax global header block sequence.

## tarfile.TarInfo.create_pax_header(self, info, encoding)

Return the object as a ustar header block. If it cannot be represented this way, prepend a pax extended header sequence with supplement information.

## tarfile.TarInfo.create_ustar_header(self, info, encoding, errors)

Return the object as a ustar header block.

## tarfile.TarInfo.frombuf(...)

Construct a TarInfo object from a 512 byte bytes object. To support the old v7 tar format AREGTYPE headers are
transformed to DIRTYPE headers if their name ends in '/'.

## tarfile.TarInfo.fromtarfile(...)

Return the next TarInfo object from TarFile object tarfile.

## tarfile.TarInfo.get_info(self)

Return the TarInfo's attributes as a dictionary.

## tarfile.TarInfo.isblk(self)

Return True if it is a block device.

## tarfile.TarInfo.ischr(self)

Return True if it is a character device.

## tarfile.TarInfo.isdev(self)

Return True if it is one of character device, block device or FIFO.

## tarfile.TarInfo.isdir(self)

Return True if it is a directory.

## tarfile.TarInfo.isfifo(self)

Return True if it is a FIFO.

## tarfile.TarInfo.isfile(self)

Return True if the Tarinfo object is a regular file.

## tarfile.TarInfo.islnk(self)

Return True if it is a hard link.

## tarfile.TarInfo.isreg(self)

Return True if the Tarinfo object is a regular file.

## tarfile.TarInfo.issym(self)

Return True if it is a symbolic link.

## tarfile.TarInfo.replace(self, *, name=<object object at 0x7fc8a19217d0>, mtime=<object object at 0x7fc8a19217d0>, mode=<object object at 0x7fc8a19217d0>, linkname=<object object at 0x7fc8a19217d0>, uid=<object object at 0x7fc8a19217d0>, gid=<object object at 0x7fc8a19217d0>, uname=<object object at 0x7fc8a19217d0>, gname=<object object at 0x7fc8a19217d0>, deep=True, _KEEP=<object object at 0x7fc8a19217d0>)

Return a deep copy of self with the given attributes replaced.

## tarfile.TarInfo.tobuf(self, format=2, encoding='utf-8', errors='surrogateescape')

Return a tar header as a string of 512 byte blocks.

## tarfile.TruncatedHeaderError(...)

Exception for truncated headers.

## tarfile.calc_chksums(buf)

According to the GNU tar sources, some tars (Sun and NeXT) calculate chksum with signed char, which will be different if there are chars in the buffer with the high bit set. So we calculate two checksums, unsigned and signed.

## tarfile.copyfileobj(src, dst, length=None, exception=<class 'OSError'>, bufsize=None)

Copy length bytes from fileobj src to fileobj dst. If length is None, copy the entire content.

## tarfile.is_tarfile(name)

Return True if name points to a tar archive that we are able to handle, else return False. 'name' should be a string, file, or file-like object.

## tarfile.itn(n, digits=8, format=2)

Convert a python number to a number field.

## tarfile.nti(s)

Convert a number field to a python number.

## tarfile.nts(s, encoding, errors)

Convert a null-terminated bytes object to a string.

## tarfile.stn(s, length, encoding, errors)

Convert a string to a null-terminated bytes object.
