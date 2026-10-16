# posix

## posix.DirEntry.inode(self, /)

Return inode of the entry; cached per entry.

## posix.DirEntry.is_dir(self, /, *, follow_symlinks=True)

Return True if the entry is a directory; cached per entry.

## posix.DirEntry.is_file(self, /, *, follow_symlinks=True)

Return True if the entry is a file; cached per entry.

## posix.DirEntry.is_junction(self, /)

Return True if the entry is a junction; cached per entry.

## posix.DirEntry.is_symlink(self, /)

Return True if the entry is a symbolic link; cached per entry.

## posix.DirEntry.stat(self, /, *, follow_symlinks=True)

Return stat_result object for the entry; cached per entry.

## posix.WCOREDUMP(status, /)

Return True if the process returning status was dumped to a core file.

## posix.WEXITSTATUS(status)

Return the process return code from status.

## posix.WIFCONTINUED(status)

Return True if a particular process was continued from a job control stop. Return True if the process returning status was continued from a
job control stop.

## posix.WIFEXITED(status)

Return True if the process returning status exited via the exit() system call.

## posix.WIFSIGNALED(status)

Return True if the process returning status was terminated by a signal.

## posix.WIFSTOPPED(status)

Return True if the process returning status was stopped.

## posix.WSTOPSIG(status)

Return the signal that stopped the process that provided the status value.

## posix.WTERMSIG(status)

Return the signal that terminated the process that provided the status value.

## posix.abort()

Abort the interpreter immediately. This function 'dumps core' or otherwise fails in the hardest way
possible on the hosting operating system.  This function never returns.

## posix.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)

path
    Path to be tested; can be string, bytes, or a path-like object.
  mode
    Operating-system mode bitfield.  Can be F_OK to test existence,
    or the inclusive-OR of R_OK, W_OK, and X_OK.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  effective_ids
    If True, access will use the effective uid/gid instead of
    the real uid/gid.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    access will examine the symbolic link itself instead of the file
    the link points to.

dir_fd, effective_ids, and follow_symlinks may not be implemented
  on your platform.  If they are unavailable, using them will raise a
  NotImplementedError.

Note that most operations will use the effective uid/gid, therefore this
  routine can be used in a suid/sgid environment to test if the invoking user
  has the specified access to the path.

## posix.chdir(path)

path may always be specified as a string.  On some platforms, path may
also be specified as an open file descriptor.  If this functionality is
unavailable, using it raises an exception.

## posix.chmod(...)

path
    Path to be modified.  May always be specified as a str, bytes, or
    a path-like object.  On some platforms, path may also be specified
    as an open file descriptor.  If this functionality is unavailable,
    using it raises an exception.
  mode
    Operating-system mode bitfield.
    Be careful when using number literals for *mode*. The conventional
    UNIX notation for numeric modes uses an octal base, which needs to
    be indicated with a ``0o`` prefix in Python.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    chmod will modify the symbolic link itself instead of the file
    the link points to.

It is an error to use dir_fd or follow_symlinks when specifying path as
  an open file descriptor.
dir_fd and follow_symlinks may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.

## posix.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)

Change the owner and group id of path to the numeric uid and gid. path
    Path to be examined; can be string, bytes, a path-like object, or
    open-file-descriptor int.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    stat will examine the symbolic link itself instead of the file
    the link points to.

path may always be specified as a string.  On some platforms, path may
also be specified as an open file descriptor.  If this functionality is
unavailable, using it raises an exception.
If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.
If follow_symlinks is False, and the last element of the path is
a symbolic link, chown will modify the symbolic link itself instead of
the file the link points to.
It is an error to use dir_fd or follow_symlinks when specifying path as
an open file descriptor.
dir_fd and follow_symlinks may not be implemented on your platform.  If
they are unavailable, using them will raise a NotImplementedError.

## posix.chroot(path)

Change root directory to path.

## posix.close(fd)

Close a file descriptor.

## posix.closerange(fd_low, fd_high, /)

Closes all file descriptors in [fd_low, fd_high), ignoring errors.

## posix.confstr(name, /)

Return a string-valued system configuration variable.

## posix.copy_file_range(src, dst, count, offset_src=None, offset_dst=None)

src
    Source file descriptor.
  dst
    Destination file descriptor.
  count
    Number of bytes to copy.
  offset_src
    Starting offset in src.
  offset_dst
    Starting offset in dst.

If offset_src is None, then src is read from the current position;
respectively for offset_dst.

## posix.cpu_count()

Return the number of logical CPUs in the system. Return None if indeterminable.

## posix.ctermid()

Return the name of the controlling terminal for this process.

## posix.device_encoding(fd)

Return a string describing the encoding of a terminal's file descriptor. The file descriptor must be attached to a terminal.
If the device is not a terminal, return None.

## posix.dup(fd, /)

Return a duplicate of a file descriptor.

## posix.dup2(fd, fd2, inheritable=True)

Duplicate file descriptor.

## posix.eventfd(initval, flags=524288)

Creates and returns an event notification file descriptor.

## posix.eventfd_read(fd)

Read eventfd value

## posix.eventfd_write(fd, value)

Write eventfd value.

## posix.execv(path, argv, /)

Execute an executable path with arguments, replacing current process. path
  Path of executable file.
argv
  Tuple or list of strings.

## posix.execve(path, argv, env)

Execute an executable path with arguments, replacing current process. path
  Path of executable file.
argv
  Tuple or list of strings.
env
  Dictionary of strings mapping to strings.

## posix.fchdir(fd)

Change to the directory of the given file descriptor. fd must be opened on a directory, not a file.
Equivalent to os.chdir(fd).

## posix.fchmod(fd, mode)

fd
    The file descriptor of the file to be modified.
  mode
    Operating-system mode bitfield.
    Be careful when using number literals for *mode*.  The conventional
    UNIX notation for numeric modes uses an octal base, which needs to
    be indicated with a ``0o`` prefix in Python.

Equivalent to os.chmod(fd, mode).

## posix.fchown(fd, uid, gid)

Change the owner and group id of the file specified by file descriptor. Equivalent to os.chown(fd, uid, gid).

## posix.fdatasync(fd)

Force write of fd to disk without forcing update of metadata.

## posix.fork()

Fork a child process. Return 0 to child process and PID of child to parent process.

## posix.forkpty()

Returns a tuple of (pid, master_fd).
Like fork(), return pid of 0 to the child process,
and pid of child to the parent process.
To both, return fd of newly opened pseudo-terminal.

## posix.fpathconf(fd, name, /)

Return the configuration limit name for the file descriptor fd. If there is no limit, return -1.

## posix.fspath(path)

If the object is str or bytes, then allow it to pass through as-is.  If
the object defines __fspath__(), then return the result of that method.
All other types raise a TypeError.

## posix.fstat(fd)

Perform a stat system call on the given file descriptor. Like stat(), but for an open file descriptor.
Equivalent to os.stat(fd).

## posix.fstatvfs(fd, /)

Perform an fstatvfs system call on the given fd. Equivalent to statvfs(fd).

## posix.fsync(fd)

Force write of fd to disk.

## posix.ftruncate(fd, length, /)

Truncate a file, specified by file descriptor, to a specific length.

## posix.get_blocking(fd, /)

Get the blocking mode of the file descriptor. Return False if the O_NONBLOCK flag is set, True if the flag is cleared.

## posix.get_inheritable(fd, /)

Get the close-on-exe flag of the specified file descriptor.

## posix.get_terminal_size(...)

The optional argument fd (default standard output) specifies
which file descriptor should be queried.

If the file descriptor is not connected to a terminal, an OSError
is thrown.

This function will only be defined if an implementation is
available for this system.

shutil.get_terminal_size is the high-level function which should
normally be used, os.get_terminal_size is the low-level implementation.

## posix.getcwd()

Return a unicode string representing the current working directory.

## posix.getcwdb()

Return a bytes string representing the current working directory.

## posix.getegid()

Return the current process's effective group id.

## posix.geteuid()

Return the current process's effective user id.

## posix.getgid()

Return the current process's group id.

## posix.getgrouplist(user, group, /)

Returns a list of groups to which a user belongs. user
  username to lookup
group
  base group id of the user

## posix.getgroups()

Return list of supplemental group IDs for the process.

## posix.getloadavg()

Return the number of processes in the system run queue averaged over
the last 1, 5, and 15 minutes as a tuple of three floats.
Raises OSError if the load average was unobtainable.

## posix.getlogin()

Return the actual login name.

## posix.getpgid(pid)

Call the system call getpgid(), and return the result.

## posix.getpgrp()

Return the current process group id.

## posix.getpid()

Return the current process id.

## posix.getppid()

Return the parent's process id. If the parent process has already exited, Windows machines will still
return its id; others systems will return the id of the 'init' proces
(1).

## posix.getpriority(which, who)

Return program scheduling priority.

## posix.getrandom(size, flags=0)

Obtain a series of random bytes.

## posix.getresgid()

Return a tuple of the current process's real, effective, and saved group ids.

## posix.getresuid()

Return a tuple of the current process's real, effective, and saved user ids.

## posix.getsid(pid, /)

Call the system call getsid(pid) and return the result.

## posix.getuid()

Return the current process's user id.

## posix.getxattr(path, attribute, *, follow_symlinks=True)

path may be either a string, a path-like object, or an open file
descriptor.
If follow_symlinks is False, and the last element of the path is
a symbolic link, getxattr will examine the symbolic link itself
instead of the file the link points to.

## posix.grantpt(fd, /)

Grant access to the slave pseudo-terminal device. fd
    File descriptor of a master pseudo-terminal device.

Performs a grantpt() C function call.

## posix.initgroups(username, gid, /)

Initialize the group access list. Call the system initgroups() to initialize the group access list with
all of the groups of which the specified username is a member, plus the
specified group id.

## posix.isatty(fd, /)

Return True if the fd is connected to a terminal. Return True if the file descriptor is an open file descriptor
connected to the slave end of a terminal.

## posix.kill(pid, signal, /)

Kill a process with a signal.

## posix.killpg(pgid, signal, /)

Kill a process group with a signal.

## posix.lchown(path, uid, gid)

Change the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links.
Equivalent to os.chown(path, uid, gid, follow_symlinks=False).

## posix.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)

If either src_dir_fd or dst_dir_fd is not None, it should be a file
descriptor open to a directory, and the respective path string (src or
dst) should be relative; the path will then be relative to that
directory.
If follow_symlinks is False, and the last element of src is a symbolic
link, link will create a link to the symbolic link itself instead of the
file the link points to.
src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on
your platform.  If they are unavailable, using them will raise
a NotImplementedError.

## posix.listdir(path=None)

path can be specified as either str, bytes, or a path-like object.  If
path is bytes, the filenames returned will also be bytes; in all other
circumstances the filenames returned will be str.
If path is None, uses the path='.'.
On some platforms, path may also be specified as an open file
descriptor; the file descriptor must refer to a directory.  If this
functionality is unavailable, using it raises NotImplementedError.

The list is in arbitrary order.  It does not include the special
entries '.' and '..' even if they are present in the directory.

## posix.listxattr(path=None, *, follow_symlinks=True)

path may be either None, a string, a path-like object, or an open file
descriptor.  If path is None, listxattr will examine the current
directory.
If follow_symlinks is False, and the last element of the path is
a symbolic link, listxattr will examine the symbolic link itself instead
of the file the link points to.

## posix.lockf(fd, command, length, /)

fd
  An open file descriptor.
command
  One of F_LOCK, F_TLOCK, F_ULOCK or F_TEST.
length
  The number of bytes to lock, starting at the current position.

## posix.login_tty(fd, /)

Make the calling process a session leader; make the tty the
controlling tty, the stdin, the stdout, and the stderr of the
calling process; close fd.

## posix.lseek(fd, position, whence, /)

Return the new position.

fd
    An open file descriptor, as returned by os.open().
  position
    Position, interpreted relative to 'whence'.
  whence
    The relative position to seek from. Valid values are:
    - SEEK_SET: seek from the start of the file.
    - SEEK_CUR: seek from the current file position.
    - SEEK_END: seek from the end of the file.

The return value is the number of bytes relative to the beginning of
the file.

## posix.lstat(path, *, dir_fd=None)

Perform a stat system call on the given path, without following symbolic links. Like stat(), but do not follow symbolic links.
Equivalent to stat(path, follow_symlinks=False).

## posix.major(device, /)

Extracts a device major number from a raw device number.

## posix.makedev(major, minor, /)

Composes a raw device number from the major and minor device numbers.

## posix.minor(device, /)

Extracts a device minor number from a raw device number.

## posix.mkdir(path, mode=511, *, dir_fd=None)

Create a directory. If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.
dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

The mode argument is ignored on Windows.  Where it is used, the current
umask value is first masked out.

## posix.mkfifo(path, mode=438, *, dir_fd=None)

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.
dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

## posix.mknod(path, mode=384, device=0, *, dir_fd=None)

Create a node in the file system (file, device special file or named
pipe) at path.  mode specifies both the permissions to use and the
type of node to be created, being combined (bitwise OR) with one of
S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO.  If S_IFCHR or S_IFBLK is set
on mode, device defines the newly created device special file (probably
using os.makedev()).  Otherwise device is ignored.

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative
to that directory.
dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

## posix.nice(increment, /)

Add increment to the priority of process and return the new priority.

## posix.open(path, flags, mode=511, *, dir_fd=None)

Returns a file descriptor (integer).

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.
dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

## posix.openpty()

Open a pseudo-terminal. Return a tuple of (master_fd, slave_fd) containing open file descriptors
for both the master and slave ends.

## posix.pathconf(path, name)

If there is no limit, return -1.
On some platforms, path may also be specified as an open file
descriptor.  If this functionality is unavailable, using it raises
an exception.

## posix.pidfd_open(pid, flags=0)

Return a file descriptor referring to the process *pid*. The descriptor can be used to perform process management without races
and signals.

## posix.pipe()

Create a pipe. Returns a tuple of two file descriptors:
  (read_fd, write_fd)

## posix.pipe2(flags, /)

Create a pipe with flags set atomically. Returns a tuple of two file descriptors:
  (read_fd, write_fd)

flags can be constructed by ORing together one or more of these values:
O_NONBLOCK, O_CLOEXEC.

## posix.posix_fadvise(fd, offset, length, advice, /)

Announce an intention to access data in a specific pattern, thus
allowing the kernel to make optimizations.
The advice applies to the region of the file specified by fd starting at
offset and continuing for length bytes.
advice is one of POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL,
POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, or
POSIX_FADV_DONTNEED.

## posix.posix_fallocate(fd, offset, length, /)

Ensure a file has allocated at least a particular number of bytes on disk. Ensure that the file specified by fd encompasses a range of bytes
starting at offset bytes from the beginning and continuing for length
bytes.

## posix.posix_openpt(oflag, /)

Performs a posix_openpt() C function call. The oflag argument is used to
set file status flags and file access modes as specified in the manual
page of posix_openpt() of your system.

## posix.posix_spawn(path, argv, env, /, *, file_actions=(), setpgroup=None, resetids=False, setsid=False, setsigmask=(), setsigdef=(), scheduler=None)

Execute the program specified by path in a new process. path
  Path of executable file.
argv
  Tuple or list of strings.
env
  Dictionary of strings mapping to strings.
file_actions
  A sequence of file action tuples.
setpgroup
  The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
resetids
  If the value is `true` the POSIX_SPAWN_RESETIDS will be activated.
setsid
  If the value is `true` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP
  will be activated.
setsigmask
  The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
setsigdef
  The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
scheduler
  A tuple with the scheduler policy (optional) and parameters.

## posix.posix_spawnp(path, argv, env, /, *, file_actions=(), setpgroup=None, resetids=False, setsid=False, setsigmask=(), setsigdef=(), scheduler=None)

Execute the program specified by path in a new process. path
  Path of executable file.
argv
  Tuple or list of strings.
env
  Dictionary of strings mapping to strings.
file_actions
  A sequence of file action tuples.
setpgroup
  The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
resetids
  If the value is `True` the POSIX_SPAWN_RESETIDS will be activated.
setsid
  If the value is `True` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP
  will be activated.
setsigmask
  The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
setsigdef
  The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
scheduler
  A tuple with the scheduler policy (optional) and parameters.

## posix.pread(fd, length, offset, /)

Read a number of bytes from a file descriptor starting at a particular offset. Read length bytes from file descriptor fd, starting at offset bytes from
the beginning of the file.  The file offset remains unchanged.

## posix.preadv(fd, buffers, offset, flags=0, /)

Combines the functionality of readv() and pread().  As readv(), it will
transfer data into each buffer until it is full and then move on to the
next buffer in the sequence to hold the rest of the data.  Its fourth
argument, specifies the file offset at which the input operation is to
be performed.  It will return the total number of bytes read (which can
be less than the total capacity of all the objects).

The flags argument contains a bitwise OR of zero or more of the
following flags:

- RWF_HIPRI
- RWF_NOWAIT

Using non-zero flags requires Linux 4.6 or newer.

## posix.ptsname(fd, /)

fd
    File descriptor of a master pseudo-terminal device.

If the ptsname_r() C function is available, it is called;
otherwise, performs a ptsname() C function call.

## posix.putenv(name, value, /)

Change or add an environment variable.

## posix.pwrite(fd, buffer, offset, /)

Write buffer to fd, starting at offset bytes from the beginning of
the file.  Returns the number of bytes written.  Does not change the
current file offset.

## posix.pwritev(fd, buffers, offset, flags=0, /)

Combines the functionality of writev() and pwrite(). All buffers must be
a sequence of bytes-like objects.  Buffers are processed in array order.
Entire contents of first buffer is written before proceeding to second,
and so on. The operating system may set a limit (sysconf() value
SC_IOV_MAX) on the number of buffers that can be used.
This function writes the contents of each object to the file descriptor
and returns the total number of bytes written.

The flags argument contains a bitwise OR of zero or more of the
following flags:

- RWF_DSYNC
- RWF_SYNC
- RWF_APPEND

Using non-zero flags requires Linux 4.7 or newer.

## posix.read(fd, length, /)

Read from a file descriptor. Returns a bytes object.

## posix.readlink(path, *, dir_fd=None)

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.

dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

## posix.readv(fd, buffers, /)

The buffers should be mutable buffers accepting bytes.
readv will transfer data into each buffer until it is full
and then move on to the next buffer in the sequence to hold
the rest of the data.

readv returns the total number of bytes read,
which may be less than the total capacity of all the buffers.

## posix.register_at_fork(...)

before
    A callable to be called in the parent before the fork() syscall.
  after_in_child
    A callable to be called in the child after fork().
  after_in_parent
    A callable to be called in the parent after fork().

'before' callbacks are called in reverse order.
'after_in_child' and 'after_in_parent' callbacks are called in order.

## posix.remove(path, *, dir_fd=None)

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative
to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.

## posix.removexattr(path, attribute, *, follow_symlinks=True)

path may be either a string, a path-like object, or an open file
descriptor.
If follow_symlinks is False, and the last element of the path is
a symbolic link, removexattr will modify the symbolic link itself
instead of the file the link points to.

## posix.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

Rename a file or directory. If either src_dir_fd or dst_dir_fd is not None, it should be a file
descriptor open to a directory, and the respective path string (src or
dst) should be relative; the path will then be relative to that
directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
If they are unavailable, using them will raise a NotImplementedError.

## posix.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

If either src_dir_fd or dst_dir_fd is not None, it should be a file
descriptor open to a directory, and the respective path string (src or
dst) should be relative; the path will then be relative to that
directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
If they are unavailable, using them will raise a NotImplementedError.

## posix.rmdir(path, *, dir_fd=None)

Remove a directory. If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative
to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.

## posix.scandir(path=None)

path can be specified as either str, bytes, or a path-like object.  If
path is bytes, the names of yielded DirEntry objects will also be bytes;
in all other circumstances they will be str.

If path is None, uses the path='.'.

## posix.sched_get_priority_max(policy)

Get the maximum scheduling priority for policy.

## posix.sched_get_priority_min(policy)

Get the minimum scheduling priority for policy.

## posix.sched_getaffinity(pid, /)

Return the affinity of the process identified by pid (or the current process if zero). The affinity is returned as a set of CPU identifiers.

## posix.sched_getparam(pid, /)

Returns scheduling parameters for the process identified by pid. If pid is 0, returns parameters for the calling process.
Return value is an instance of sched_param.

## posix.sched_getscheduler(pid, /)

Get the scheduling policy for the process identified by pid. Passing 0 for pid returns the scheduling policy for the calling process.

## posix.sched_param(sched_priority)

Currently has only one field: sched_priority sched_priority
  A scheduling parameter.

## posix.sched_rr_get_interval(pid, /)

Return the round-robin quantum for the process identified by pid, in seconds. Value returned is a float.

## posix.sched_setaffinity(pid, mask, /)

Set the CPU affinity of the process identified by pid to mask. mask should be an iterable of integers identifying CPUs.

## posix.sched_setparam(pid, param, /)

Set scheduling parameters for the process identified by pid. If pid is 0, sets parameters for the calling process.
param should be an instance of sched_param.

## posix.sched_setscheduler(pid, policy, param, /)

Set the scheduling policy for the process identified by pid. If pid is 0, the calling process is changed.
param is an instance of sched_param.

## posix.sched_yield()

Voluntarily relinquish the CPU.

## posix.sendfile(out_fd, in_fd, offset, count)

Copy count bytes from file descriptor in_fd to file descriptor out_fd.

## posix.set_blocking(fd, blocking, /)

Set the blocking mode of the specified file descriptor. Set the O_NONBLOCK flag if blocking is False,
clear the O_NONBLOCK flag otherwise.

## posix.set_inheritable(fd, inheritable, /)

Set the inheritable flag of the specified file descriptor.

## posix.setegid(egid, /)

Set the current process's effective group id.

## posix.seteuid(euid, /)

Set the current process's effective user id.

## posix.setgid(gid, /)

Set the current process's group id.

## posix.setgroups(groups, /)

Set the groups of the current process to list.

## posix.setns(fd, nstype=0)

Move the calling thread into different namespaces. fd
  A file descriptor to a namespace.
nstype
  Type of namespace.

## posix.setpgid(pid, pgrp, /)

Call the system call setpgid(pid, pgrp).

## posix.setpgrp()

Make the current process the leader of its process group.

## posix.setpriority(which, who, priority)

Set program scheduling priority.

## posix.setregid(rgid, egid, /)

Set the current process's real and effective group ids.

## posix.setresgid(rgid, egid, sgid, /)

Set the current process's real, effective, and saved group ids.

## posix.setresuid(ruid, euid, suid, /)

Set the current process's real, effective, and saved user ids.

## posix.setreuid(ruid, euid, /)

Set the current process's real and effective user ids.

## posix.setsid()

Call the system call setsid().

## posix.setuid(uid, /)

Set the current process's user id.

## posix.setxattr(path, attribute, value, flags=0, *, follow_symlinks=True)

path may be either a string, a path-like object,  or an open file
descriptor.
If follow_symlinks is False, and the last element of the path is
a symbolic link, setxattr will modify the symbolic link itself instead
of the file the link points to.

## posix.splice(src, dst, count, offset_src=None, offset_dst=None, flags=0)

src
    Source file descriptor.
  dst
    Destination file descriptor.
  count
    Number of bytes to copy.
  offset_src
    Starting offset in src.
  offset_dst
    Starting offset in dst.
  flags
    Flags to modify the semantics of the call.

If offset_src is None, then src is read from the current position;
respectively for offset_dst. The offset associated to the file
descriptor that refers to a pipe must be None.

## posix.stat(path, *, dir_fd=None, follow_symlinks=True)

path
    Path to be examined; can be string, bytes, a path-like object or
    open-file-descriptor int.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be a relative string; path will then be relative to
    that directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    stat will examine the symbolic link itself instead of the file
    the link points to.

dir_fd and follow_symlinks may not be implemented
  on your platform.  If they are unavailable, using them will raise a
  NotImplementedError.

It's an error to use dir_fd or follow_symlinks when specifying path as
  an open file descriptor.

## posix.statvfs(path)

path may always be specified as a string.
On some platforms, path may also be specified as an open file
descriptor.  If this functionality is unavailable, using it raises
an exception.

## posix.strerror(code, /)

Translate an error code to a message string.

## posix.symlink(src, dst, target_is_directory=False, *, dir_fd=None)

target_is_directory is required on Windows if the target is to be
interpreted as a directory.  (On Windows, symlink requires Windows 6.0
or greater, and raises a NotImplementedError otherwise.)
target_is_directory is ignored on non-Windows platforms.

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative
to that directory.
dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.

## posix.sync()

Force write of everything to disk.

## posix.sysconf(name, /)

Return an integer-valued system configuration variable.

## posix.system(command)

Execute the command in a subshell.

## posix.tcgetpgrp(fd, /)

Return the process group associated with the terminal specified by fd.

## posix.tcsetpgrp(fd, pgid, /)

Set the process group associated with the terminal specified by fd.

## posix.timerfd_create(clockid, /, *, flags=0)

clockid
  A valid clock ID constant as timer file descriptor.

time.CLOCK_REALTIME
  time.CLOCK_MONOTONIC
  time.CLOCK_BOOTTIME
flags
  0 or a bit mask of os.TFD_NONBLOCK or os.TFD_CLOEXEC.

os.TFD_NONBLOCK
      If *TFD_NONBLOCK* is set as a flag, read doesn't blocks.
      If *TFD_NONBLOCK* is not set as a flag, read block until the timer fires.

os.TFD_CLOEXEC
      If *TFD_CLOEXEC* is set as a flag, enable the close-on-exec flag

## posix.timerfd_gettime(fd, /)

Return a tuple of a timer file descriptor's (next expiration, interval) in float seconds. fd
  A timer file descriptor.

## posix.timerfd_gettime_ns(fd, /)

Return a tuple of a timer file descriptor's (next expiration, interval) in nanoseconds. fd
  A timer file descriptor.

## posix.timerfd_settime(fd, /, *, flags=0, initial=0.0, interval=0.0)

fd
  A timer file descriptor.
flags
  0 or a bit mask of TFD_TIMER_ABSTIME or TFD_TIMER_CANCEL_ON_SET.
initial
  The initial expiration time, in seconds.
interval
  The timer's interval, in seconds.

## posix.timerfd_settime_ns(fd, /, *, flags=0, initial=0, interval=0)

fd
  A timer file descriptor.
flags
  0 or a bit mask of TFD_TIMER_ABSTIME or TFD_TIMER_CANCEL_ON_SET.
initial
  initial expiration timing in nanoseconds.
interval
  interval for the timer in nanoseconds.

## posix.times()

Return a collection containing process timing information. The object returned behaves like a named tuple with these fields:
  (utime, stime, cutime, cstime, elapsed_time)
All fields are floating-point numbers.

## posix.times_result(iterable=(), /)

times_result: Result from os.times(). This object may be accessed either as a tuple of
  (user, system, children_user, children_system, elapsed),
or via the attributes user, system, children_user, children_system,
and elapsed.

See os.times for more information.

## posix.truncate(path, length)

Truncate a file, specified by path, to a specific length. On some platforms, path may also be specified as an open file
descriptor.  If this functionality is unavailable, using it raises
an exception.

## posix.ttyname(fd, /)

Return the name of the terminal device connected to 'fd'. fd
  Integer file descriptor handle.

## posix.umask(mask, /)

Set the current numeric umask and return the previous umask.

## posix.uname()

Return an object identifying the current operating system. The object behaves like a named tuple with the following fields:
  (sysname, nodename, release, version, machine)

## posix.uname_result(iterable=(), /)

uname_result: Result from os.uname(). This object may be accessed either as a tuple of
  (sysname, nodename, release, version, machine),
or via the attributes sysname, nodename, release, version, and machine.

See os.uname for more information.

## posix.unlink(path, *, dir_fd=None)

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.

## posix.unlockpt(fd, /)

Unlock a pseudo-terminal master/slave pair. fd
    File descriptor of a master pseudo-terminal device.

Performs an unlockpt() C function call.

## posix.unsetenv(name, /)

Delete an environment variable.

## posix.unshare(flags)

Disassociate parts of a process (or thread) execution context. flags
  Namespaces to be unshared.

## posix.urandom(size, /)

Return a bytes object containing random bytes suitable for cryptographic use.

## posix.utime(...)

path may always be specified as a string.  On some platforms, path may
also be specified as an open file descriptor.  If this functionality is
unavailable, using it raises an exception.

If times is not None, it must be a tuple (atime, mtime);
atime and mtime should be expressed as float seconds since the epoch.
If ns is specified, it must be a tuple (atime_ns, mtime_ns);
atime_ns and mtime_ns should be expressed as integer nanoseconds
since the epoch.
If times is None and ns is unspecified, utime uses the current time.
Specifying tuples for both times and ns is an error.

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.
If follow_symlinks is False, and the last element of the path is
a symbolic link, utime will modify the symbolic link itself instead of
the file the link points to.
It is an error to use dir_fd or follow_symlinks when specifying path as
an open file descriptor.
dir_fd and follow_symlinks may not be available on your platform.
If they are unavailable, using them will raise a NotImplementedError.

## posix.wait()

Wait for completion of a child process. Returns a tuple of information about the child process:
    (pid, status)

## posix.wait3(options)

Wait for completion of a child process. Returns a tuple of information about the child process:
  (pid, status, rusage)

## posix.wait4(pid, options)

Wait for completion of a specific child process. Returns a tuple of information about the child process:
  (pid, status, rusage)

## posix.waitid(idtype, id, options, /)

idtype
    Must be one of be P_PID, P_PGID or P_ALL.
  id
    The id to wait on.
  options
    Constructed from the ORing of one or more of WEXITED, WSTOPPED
    or WCONTINUED and additionally may be ORed with WNOHANG or WNOWAIT.

Returns either waitid_result or None if WNOHANG is specified and there
are no children in a waitable state.

## posix.waitid_result(iterable=(), /)

waitid_result: Result from waitid. This object may be accessed either as a tuple of
  (si_pid, si_uid, si_signo, si_status, si_code),
or via the attributes si_pid, si_uid, and so on.

See os.waitid for more information.

## posix.waitpid(pid, options, /)

Wait for completion of a given child process. Returns a tuple of information regarding the child process:
    (pid, status)

The options argument is ignored on Windows.

## posix.waitstatus_to_exitcode(status)

On Unix:

* If WIFEXITED(status) is true, return WEXITSTATUS(status).
* If WIFSIGNALED(status) is true, return -WTERMSIG(status).
* Otherwise, raise a ValueError.

On Windows, return status shifted right by 8 bits.

On Unix, if the process is being traced or if waitpid() was called with
WUNTRACED option, the caller must first check if WIFSTOPPED(status) is
true.  This function must not be called if WIFSTOPPED(status) is true.

## posix.write(fd, data, /)

Write a bytes object to a file descriptor.

## posix.writev(fd, buffers, /)

Iterate over buffers, and write the contents of each to a file descriptor. Returns the total number of bytes written.
buffers must be a sequence of bytes-like objects.
