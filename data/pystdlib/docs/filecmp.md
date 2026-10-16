# filecmp

## filecmp.clear_cache()

Clear the filecmp cache.

## filecmp.cmp(f1, f2, shallow=True)

Compare two files. Arguments:

f1 -- First file name

f2 -- Second file name

shallow -- treat files as identical if their stat signatures (type, size,
           mtime) are identical. Otherwise, files are considered different
           if their sizes or contents differ.  [default: True]

Return value:

True if the files are the same, False otherwise.

This function uses a cache for past comparisons and the results,
with cache entries invalidated if their stat information
changes.  The cache may be cleared by calling clear_cache().

## filecmp.cmpfiles(a, b, common, shallow=True)

a, b -- directory names
common -- list of file names found in both directories
shallow -- if true, do comparison based solely on stat() information

Returns a tuple of three lists:
  files that compare equal
  files that are different
  filenames that aren't regular files.

## filecmp.dircmp(a, b, ignore=None, hide=None, *, shallow=True)

dircmp(a, b, ignore=None, hide=None, *, shallow=True)
  A and B are directories.
  IGNORE is a list of names to ignore,
    defaults to DEFAULT_IGNORES.
  HIDE is a list of names to hide,
    defaults to [os.curdir, os.pardir].
  SHALLOW specifies whether to just check the stat signature (do not read
    the files).
    defaults to True.

High level usage:
  x = dircmp(dir1, dir2)
  x.report() -> prints a report on the differences between dir1 and dir2
   or
  x.report_partial_closure() -> prints report on differences between dir1
        and dir2, and reports on common immediate subdirectories.
  x.report_full_closure() -> like report_partial_closure,
        but fully recursive.

Attributes:
 left_list, right_list: The files in dir1 and dir2,
    filtered by hide and ignore.
 common: a list of names in both dir1 and dir2.
 left_only, right_only: names only in dir1, dir2.
 common_dirs: subdirectories in both dir1 and dir2.
 common_files: files in both dir1 and dir2.
 common_funny: names in both dir1 and dir2 where the type differs between
    dir1 and dir2, or the name is not stat-able.
 same_files: list of identical files.
 diff_files: list of filenames which differ.
 funny_files: list of files which could not be compared.
 subdirs: a dictionary of dircmp instances (or MyDirCmp instances if this
   object is of type MyDirCmp, a subclass of dircmp), keyed by names
   in common_dirs.
