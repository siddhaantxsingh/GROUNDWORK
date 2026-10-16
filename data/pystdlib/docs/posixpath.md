# posixpath

## posixpath.abspath(path)

Return an absolute path.

## posixpath.basename(p)

Returns the final component of a pathname

## posixpath.commonpath(paths)

Given a sequence of path names, returns the longest common sub-path.

## posixpath.dirname(p)

Returns the directory component of a pathname

## posixpath.expanduser(path)

Expand ~ and ~user constructions. If user or $HOME is unknown, do nothing.

## posixpath.expandvars(path)

Expand shell variables of form $var and ${var}. Unknown variables are left unchanged.

## posixpath.isabs(s)

Test whether a path is absolute

## posixpath.ismount(path)

Test whether a path is a mount point

## posixpath.join(a, *p)

If any component is an absolute path, all previous path components will be discarded. An empty last part will result in a path that ends with a separator.

## posixpath.normcase(s)

Normalize case of pathname. Has no effect under Posix

## posixpath.realpath(filename, *, strict=False)

Return the canonical path of the specified filename, eliminating any symbolic links encountered in the path.

## posixpath.relpath(path, start=None)

Return a relative version of a path

## posixpath.split(p)

Split a pathname. Returns tuple "(head, tail)" where "tail" is everything after the final slash. Either part may be empty.

## posixpath.splitdrive(p)

Split a pathname into drive and path. On Posix, drive is always empty.

## posixpath.splitext(p)

Split the extension from a pathname. Extension is everything from the last dot to the end, ignoring
leading dots.  Returns "(root, ext)"; ext may be empty.
