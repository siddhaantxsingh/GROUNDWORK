# zipfile

## zipfile.LargeZipFile(...)

Raised when writing a zipfile, the zipfile requires ZIP64 extensions and those extensions are disabled.

## zipfile.PyZipFile(file, mode='r', compression=0, allowZip64=True, optimize=-1)

Class to create ZIP archives with Python library files and packages.

## zipfile.PyZipFile.writepy(self, pathname, basename='', filterfunc=None)

If pathname is a package directory, search the directory and
all package subdirectories recursively for all *.py and enter
the modules into the archive.  If pathname is a plain
directory, listdir *.py and enter all modules.  Else, pathname
must be a Python *.py file and the module will be put into the
archive.  Added modules are always module.pyc.
This method will compile the module.py into module.pyc if
necessary.
If filterfunc(pathname) is given, it is called with every argument.
When it is False, the file or directory is skipped.

## zipfile.ZipExtFile(fileobj, mode, zipinfo, pwd=None, close_fileobj=False)

File-like object for reading an archive member. Is returned by ZipFile.open().

## zipfile.ZipExtFile.peek(self, n=1)

Returns buffered bytes without advancing the position.

## zipfile.ZipExtFile.read(self, n=-1)

Read and return up to n bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached.

## zipfile.ZipExtFile.read1(self, n)

Read up to n bytes with at most one read() system call.

## zipfile.ZipExtFile.readline(self, limit=-1)

Read and return a line from the stream. If limit is specified, at most limit bytes will be read.

## zipfile.ZipFile(file, mode='r', compression=0, allowZip64=True, compresslevel=None, *, strict_timestamps=True, metadata_encoding=None)

z = ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True,
            compresslevel=None)

file: Either the path to the file, or a file-like object.
      If it is a path, the file will be opened and closed by ZipFile.
mode: The mode can be either read 'r', write 'w', exclusive create 'x',
      or append 'a'.
compression: ZIP_STORED (no compression), ZIP_DEFLATED (requires zlib),
      ZIP_BZIP2 (requires bz2) or ZIP_LZMA (requires lzma).
allowZip64: if True ZipFile will create files with ZIP64 extensions
      when needed, otherwise it will raise an exception when this
      would be necessary.
compresslevel: None (default for the given compression type) or
      an integer specifying the level to pass to the compressor.
      When using ZIP_STORED or ZIP_LZMA this keyword has no effect.
      When using ZIP_DEFLATED integers 0 through 9 are accepted.
      When using ZIP_BZIP2 integers 1 through 9 are accepted.

## zipfile.ZipFile.close(self)

Close the file, and for mode 'w', 'x' and 'a' write the ending records.

## zipfile.ZipFile.extract(self, member, path=None, pwd=None)

Extract a member from the archive to the current working directory, using its full name. Its file information is extracted as accurately as possible. `member' may be a filename or a ZipInfo object. You can specify a different directory using `path'. You can specify the password to decrypt the file using 'pwd'.

## zipfile.ZipFile.extractall(self, path=None, members=None, pwd=None)

Extract all members from the archive to the current working directory. `path' specifies a different directory to extract to. `members' is optional and must be a subset of the list returned by namelist(). You can specify the password to decrypt all files using 'pwd'.

## zipfile.ZipFile.getinfo(self, name)

Return the instance of ZipInfo given 'name'.

## zipfile.ZipFile.infolist(self)

Return a list of class ZipInfo instances for files in the archive.

## zipfile.ZipFile.mkdir(self, zinfo_or_directory_name, mode=511)

Creates a directory inside the zip archive.

## zipfile.ZipFile.namelist(self)

Return a list of file names in the archive.

## zipfile.ZipFile.open(self, name, mode='r', pwd=None, *, force_zip64=False)

Return file-like object for 'name'. name is a string for the file name within the ZIP file, or a ZipInfo
object.

mode should be 'r' to read a file already in the ZIP file, or 'w' to
write to a file newly added to the archive.

pwd is the password to decrypt files (only used for reading).

When writing, if the file size is not known in advance but may
exceed 2 GiB, pass force_zip64 to use the ZIP64 format, which can
handle large files.  If the size is known in advance, it is best to
pass a ZipInfo instance for name, with zinfo.file_size set.

## zipfile.ZipFile.printdir(self, file=None)

Print a table of contents for the zip file.

## zipfile.ZipFile.read(self, name, pwd=None)

Return file bytes for name. 'pwd' is the password to decrypt encrypted files.

## zipfile.ZipFile.setpassword(self, pwd)

Set default password for encrypted files.

## zipfile.ZipFile.testzip(self)

Read all the files and check the CRC. Return None if all files could be read successfully, or the name
of the offending file otherwise.

## zipfile.ZipFile.write(self, filename, arcname=None, compress_type=None, compresslevel=None)

Put the bytes from filename into the archive under the name arcname.

## zipfile.ZipFile.writestr(self, zinfo_or_arcname, data, compress_type=None, compresslevel=None)

The contents is 'data', which may be either a 'str' or a 'bytes' instance; if it is a 'str', it is encoded as UTF-8 first. 'zinfo_or_arcname' is either a ZipInfo instance or the name of the file in the archive.

## zipfile.ZipInfo(filename='NoName', date_time=(1980, 1, 1, 0, 0, 0))

Class with attributes describing each file in the ZIP archive.

## zipfile.ZipInfo.FileHeader(self, zip64=None)

Return the per-file header as a bytes object. When the optional zip64 arg is None rather than a bool, we will
decide based upon the file_size and compress_size, if known,
False otherwise.

## zipfile.ZipInfo.from_file(...)

filename should be the path to a file or directory on the
filesystem.

arcname is the name which it will have within the archive (by
default, this will be the same as filename, but without a drive
letter and with leading path separators removed).

## zipfile.ZipInfo.is_dir(self)

Return True if this archive member is a directory.

## zipfile.is_zipfile(filename)

Quickly see if a file is a ZIP file by checking the magic number. The filename argument may be a file or file-like object too.
