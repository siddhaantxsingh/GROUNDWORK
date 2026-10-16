# glob

## glob.escape(pathname)

Escape all special characters.

## glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

The pattern may contain simple shell-style wildcards a la
fnmatch. Unlike fnmatch, filenames starting with a
dot are special cases that are not matched by '*' and '?'
patterns by default.

The order of the returned list is undefined. Sort it if you need a
particular order.

If `root_dir` is not None, it should be a path-like object specifying
the root directory for searching.  It has the same effect as changing
the current directory before calling it (without actually changing it).
If pathname is relative, the result will contain paths relative to
`root_dir`.

If `dir_fd` is not None, it should be a file descriptor referring to a
directory, and paths will then be relative to that directory.

If `include_hidden` is true, wildcards can match path segments beginning
with a dot ('.').

If `recursive` is true, the pattern '**' will match any files and
zero or more directories and subdirectories.

## glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

The pattern may contain simple shell-style wildcards a la
fnmatch. However, unlike fnmatch, filenames starting with a
dot are special cases that are not matched by '*' and '?'
patterns.

The order of the returned paths is undefined. Sort them if you need a
particular order.

If `root_dir` is not None, it should be a path-like object specifying
the root directory for searching.  It has the same effect as changing
the current directory before calling it (without actually changing it).
If pathname is relative, the result will contain paths relative to
`root_dir`.

If `dir_fd` is not None, it should be a file descriptor referring to a
directory, and paths will then be relative to that directory.

If `include_hidden` is true, wildcards can match path segments beginning
with a dot ('.').

If `recursive` is true, the pattern '**' will match any files and
zero or more directories and subdirectories.

## glob.translate(pat, *, recursive=False, include_hidden=False, seps=None)

If `recursive` is true, the pattern segment '**' will match any number
of path segments.

If `include_hidden` is true, wildcards can match path segments beginning
with a dot ('.').

If a sequence of separator characters is given to `seps`, they will be
used to split the pattern into segments and match path separators.  If
not given, os.path.sep and os.path.altsep (where available) are used.
