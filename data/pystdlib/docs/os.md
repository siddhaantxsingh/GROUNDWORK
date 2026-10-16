# os

## os.PathLike()

Abstract base class for implementing the file system path protocol.

## os.execl(file, *args)

Execute the executable file with argument list args, replacing the current process.

## os.execle(file, *args)

Execute the executable file with argument list args and environment env, replacing the current process.

## os.execlp(file, *args)

Execute the executable file (which is searched for along $PATH) with argument list args, replacing the current process.

## os.execlpe(file, *args)

Execute the executable file (which is searched for along $PATH) with argument list args and environment env, replacing the current process.

## os.execvp(file, args)

Execute the executable file (which is searched for along $PATH) with argument list args, replacing the current process. args may be a list or tuple of strings.

## os.execvpe(file, args, env)

Execute the executable file (which is searched for along $PATH) with argument list args and environment env, replacing the current process. args may be a list or tuple of strings.

## os.fsdecode(filename)

Decode filename (an os.PathLike, bytes, or str) from the filesystem encoding with 'surrogateescape' error handler, return str unchanged. On Windows, use 'strict' error handler if the file system encoding is 'mbcs' (which is the default encoding).

## os.fsencode(filename)

Encode filename (an os.PathLike, bytes, or str) to the filesystem encoding with 'surrogateescape' error handler, return bytes unchanged. On Windows, use 'strict' error handler if the file system encoding is 'mbcs' (which is the default encoding).

## os.fwalk(top='.', topdown=True, onerror=None, *, follow_symlinks=False, dir_fd=None)

Directory tree generator. This behaves exactly like walk(), except that it yields a 4-tuple

dirpath, dirnames, filenames, dirfd

`dirpath`, `dirnames` and `filenames` are identical to walk() output,
and `dirfd` is a file descriptor referring to the directory `dirpath`.

The advantage of fwalk() over walk() is that it's safe against symlink
races (when follow_symlinks is False).

If dir_fd is not None, it should be a file descriptor open to
a directory, and top should be relative; top will then be relative to
that directory.  (dir_fd is always supported for fwalk.)

Caution:
Since fwalk() yields file descriptors, those are only valid until the
next iteration step, so you should dup() them if you want to keep them
for a longer period.

Example:

import os
for root, dirs, files, rootfd in os.fwalk('python/Lib/xml'):
    print(root, "consumes", end="")
    print(sum(os.stat(name, dir_fd=rootfd).st_size for name in files),
          end="")
    print("bytes in", len(files), "non-directory files")
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')  # don't visit __pycache__ directories

## os.get_exec_path(env=None)

Returns the sequence of directories that will be searched for the named executable (similar to a shell) when launching a process. *env* must be an environment variable dict or None.  If *env* is None,
os.environ will be used.

## os.getenv(key, default=None)

Get an environment variable, return None if it doesn't exist. The optional second argument can specify an alternate default. key, default and the result are str.

## os.getenvb(key, default=None)

Get an environment variable, return None if it doesn't exist. The optional second argument can specify an alternate default. key, default and the result are bytes.

## os.makedirs(name, mode=511, exist_ok=False)

Works like mkdir, except that any intermediate path segment (not just the rightmost) will be created if it does not exist. If the target directory already exists, raise an OSError if exist_ok is False. Otherwise no exception is raised. This is recursive.

## os.process_cpu_count()

Get the number of CPUs of the current process. Return the number of logical CPUs usable by the calling thread of the
current process. Return None if indeterminable.

## os.removedirs(name)

Works like rmdir except that, if the leaf directory is successfully removed, directories corresponding to rightmost path segments will be pruned away until either the whole path is consumed or an error occurs. Errors during this latter phase are ignored -- they generally mean that a directory was not empty.

## os.renames(old, new)

Works like rename, except creation of any intermediate directories needed to make the new pathname good is attempted first. After the rename, directories corresponding to rightmost path segments of the old name will be pruned until either the whole path is consumed or a nonempty directory is found.

Note: this function can fail with the new directory structure made
if you lack permissions needed to unlink the leaf directory or
file.

## os.spawnl(mode, file, *args)

Execute file with arguments from args in a subprocess. If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnle(mode, file, *args)

If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnlp(mode, file, *args)

Execute file (which is looked for along $PATH) with arguments from args in a subprocess with the supplied environment. If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnlpe(mode, file, *args)

Execute file (which is looked for along $PATH) with arguments from args in a subprocess with the supplied environment. If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnv(mode, file, args)

Execute file with arguments from args in a subprocess. If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnve(mode, file, args, env)

If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnvp(mode, file, args)

If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.spawnvpe(mode, file, args, env)

Execute file (which is looked for along $PATH) with arguments from args in a subprocess with the supplied environment. If mode == P_NOWAIT return the pid of the process. If mode == P_WAIT return the process's exit code if it exits normally; otherwise return -SIG, where SIG is the signal that killed it.

## os.stat_result(iterable=(), /)

This object may be accessed either as a tuple of
  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
or via the attributes st_mode, st_ino, st_dev, st_nlink, and so on.

Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
or st_flags, they are available as attributes only.

See os.stat for more information.

## os.statvfs_result(iterable=(), /)

This object may be accessed either as a tuple of
  (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.

See os.statvfs for more information.

## os.terminal_size(iterable=(), /)

A tuple of (columns, lines) for holding terminal window size

## os.walk(top, topdown=True, onerror=None, followlinks=False)

Directory tree generator. For each directory in the directory tree rooted at top (including top
itself, but excluding '.' and '..'), yields a 3-tuple

dirpath, dirnames, filenames

dirpath is a string, the path to the directory.  dirnames is a list of
the names of the subdirectories in dirpath (including symlinks to
directories, and excluding '.' and '..').
filenames is a list of the names of the non-directory files in dirpath.
Note that the names in the lists are just names, with no path
components.  To get a full path (which begins with top) to a file or
directory in dirpath, do os.path.join(dirpath, name).

If optional arg 'topdown' is true or not specified, the triple for a
directory is generated before the triples for any of its subdirectories
(directories are generated top down).  If topdown is false, the triple
for a directory is generated after the triples for all of its
subdirectories (directories are generated bottom up).

When topdown is true, the caller can modify the dirnames list in-place
(e.g., via del or slice assignment), and walk will only recurse into the
subdirectories whose names remain in dirnames; this can be used to prune
the search, or to impose a specific order of visiting.  Modifying
dirnames when topdown is false has no effect on the behavior of
os.walk(), since the directories in dirnames have already been generated
by the time dirnames itself is generated. No matter the value of
topdown, the list of subdirectories is retrieved before the tuples for
the directory and its subdirectories are generated.

By default errors from the os.scandir() call are ignored.  If
optional arg 'onerror' is specified, it should be a function; it
will be called with one argument, an OSError instance.  It can
report the error to continue with the walk, or raise the exception
to abort the walk.  Note that the filename is available as the
filename attribute of the exception object.

By default, os.walk does not follow symbolic links to subdirectories on
systems that support them.  In order to get this functionality, set the
optional argument 'followlinks' to true.

Caution:  if you pass a relative pathname for top, don't change the
current working directory between resumptions of walk.  walk never
changes the current directory, and assumes that the client doesn't
either.

Example:

import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/xml'):
    print(root, "consumes ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')  # don't visit __pycache__ directories
