# subprocess

## subprocess.CalledProcessError(returncode, cmd, output=None, stderr=None)

Raised when run() is called with check=True and the process returns a non-zero exit status. Attributes:
  cmd, returncode, stdout, stderr, output

## subprocess.CompletedProcess(args, returncode, stdout=None, stderr=None)

This is returned by run().

Attributes:
  args: The list or str args passed to run().
  returncode: The exit code of the process, negative for signals.
  stdout: The standard output (None if not captured).
  stderr: The standard error (None if not captured).

## subprocess.CompletedProcess.check_returncode(self)

Raise CalledProcessError if the exit code is non-zero.

## subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, user=None, group=None, extra_groups=None, encoding=None, errors=None, text=None, umask=-1, pipesize=-1, process_group=None)

For a complete description of the arguments see the Python documentation.

Arguments:
  args: A string, or a sequence of program arguments.

bufsize: supplied as the buffering argument to the open() function when
      creating the stdin/stdout/stderr pipe file objects

executable: A replacement program to execute.

stdin, stdout and stderr: These specify the executed programs' standard
      input, standard output and standard error file handles, respectively.

preexec_fn: (POSIX only) An object to be called in the child process
      just before the child is executed.

close_fds: Controls closing or inheriting of file descriptors.

shell: If true, the command will be executed through the shell.

cwd: Sets the current directory before the child is executed.

env: Defines the environment variables for the new process.

text: If true, decode stdin, stdout and stderr using the given encoding
      (if set) or the system default otherwise.

universal_newlines: Alias of text, provided for backwards compatibility.

startupinfo and creationflags (Windows only)

restore_signals (POSIX only)

start_new_session (POSIX only)

process_group (POSIX only)

group (POSIX only)

extra_groups (POSIX only)

user (POSIX only)

umask (POSIX only)

pass_fds (POSIX only)

encoding and errors: Text mode encoding and error handling to use for
      file objects stdin, stdout and stderr.

Attributes:
    stdin, stdout, stderr, pid, returncode

## subprocess.Popen.communicate(self, input=None, timeout=None)

Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate.

The optional "input" argument should be data to be sent to the
child process, or None, if no data should be sent to the child.
communicate() returns a tuple (stdout, stderr).

By default, all communication is in bytes, and therefore any
"input" should be bytes, and the (stdout, stderr) will be bytes.
If in text mode (indicated by self.text_mode), any "input" should
be a string, and (stdout, stderr) will be strings decoded
according to locale encoding, or by "encoding" if set. Text mode
is triggered by setting any of text, encoding, errors or
universal_newlines.

## subprocess.Popen.kill(self)

Kill the process with SIGKILL

## subprocess.Popen.poll(self)

Check if child process has terminated. Set and return returncode attribute.

## subprocess.Popen.send_signal(self, sig)

Send a signal to the process.

## subprocess.Popen.terminate(self)

Terminate the process with SIGTERM

## subprocess.Popen.wait(self, timeout=None)

Wait for child process to terminate; returns self.returncode.

## subprocess.TimeoutExpired(cmd, timeout, output=None, stderr=None)

This exception is raised when the timeout expires while waiting for a child process. Attributes:
    cmd, output, stdout, stderr, timeout

## subprocess.call(*popenargs, timeout=None, **kwargs)

Run command with arguments. Wait for command to complete or for timeout seconds, then return the returncode attribute.

The arguments are the same as for the Popen constructor.  Example:

retcode = call(["ls", "-l"])

## subprocess.check_call(*popenargs, **kwargs)

Run command with arguments. Wait for command to complete. If the exit code was zero then return, otherwise raise CalledProcessError. The CalledProcessError object will have the return code in the returncode attribute.

The arguments are the same as for the call function.  Example:

check_call(["ls", "-l"])

## subprocess.check_output(*popenargs, timeout=None, **kwargs)

If the exit code was non-zero it raises a CalledProcessError.  The
CalledProcessError object will have the return code in the returncode
attribute and output in the output attribute.

The arguments are the same as for the Popen constructor.  Example:

>>> check_output(["ls", "-l", "/dev/null"])
b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

The stdout argument is not allowed as it is used internally.
To capture standard error in the result, use stderr=STDOUT.

>>> check_output(["/bin/sh", "-c",
...               "ls -l non_existent_file ; exit 0"],
...              stderr=STDOUT)
b'ls: non_existent_file: No such file or directory\n'

There is an additional optional argument, "input", allowing you to
pass a string to the subprocess's stdin.  If you use this argument
you may not also use the Popen constructor's "stdin" argument, as
it too will be used internally.  Example:

>>> check_output(["sed", "-e", "s/foo/bar/"],
...              input=b"when in the course of fooman events\n")
b'when in the course of barman events\n'

By default, all communication is in bytes, and therefore any "input"
should be bytes, and the return value will be bytes.  If in text mode,
any "input" should be a string, and the return value will be a string
decoded according to locale encoding, or by "encoding" if set. Text mode
is triggered by setting any of text, encoding, errors or universal_newlines.

## subprocess.getoutput(cmd, *, encoding=None, errors=None)

Like getstatusoutput(), except the exit status is ignored and the return
value is a string containing the command's output.  Example:

>>> import subprocess
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'

## subprocess.getstatusoutput(cmd, *, encoding=None, errors=None)

Execute the string 'cmd' in a shell with 'check_output' and
return a 2-tuple (status, output). The locale encoding is used
to decode the output and process newlines.

A trailing newline is stripped from the output.
The exit status for the command can be interpreted
according to the rules for the function 'wait'. Example:

>>> import subprocess
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')
>>> subprocess.getstatusoutput('cat /bin/junk')
(1, 'cat: /bin/junk: No such file or directory')
>>> subprocess.getstatusoutput('/bin/junk')
(127, 'sh: /bin/junk: not found')
>>> subprocess.getstatusoutput('/bin/kill $$')
(-15, '')

## subprocess.list2cmdline(seq)

1) Arguments are delimited by white space, which is either a
   space or a tab.

2) A string surrounded by double quotation marks is
   interpreted as a single argument, regardless of white space
   contained within.  A quoted string can be embedded in an
   argument.

3) A double quotation mark preceded by a backslash is
   interpreted as a literal double quotation mark.

4) Backslashes are interpreted literally, unless they
   immediately precede a double quotation mark.

5) If backslashes immediately precede a double quotation mark,
   every pair of backslashes is interpreted as a literal
   backslash.  If the number of backslashes is odd, the last
   backslash escapes the next double quotation mark as
   described in rule 3.

## subprocess.run(*popenargs, input=None, capture_output=False, timeout=None, check=False, **kwargs)

The returned instance will have attributes args, returncode, stdout and
stderr. By default, stdout and stderr are not captured, and those attributes
will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
or pass capture_output=True to capture both.

If check is True and the exit code was non-zero, it raises a
CalledProcessError. The CalledProcessError object will have the return code
in the returncode attribute, and output & stderr attributes if those streams
were captured.

If timeout (seconds) is given and the process takes too long,
 a TimeoutExpired exception will be raised.

There is an optional argument "input", allowing you to
pass bytes or a string to the subprocess's stdin.  If you use this argument
you may not also use the Popen constructor's "stdin" argument, as
it will be used internally.

By default, all communication is in bytes, and therefore any "input" should
be bytes, and the stdout and stderr will be bytes. If in text mode, any
"input" should be a string, and stdout and stderr will be strings decoded
according to locale encoding, or by "encoding" if set. Text mode is
triggered by setting any of text, encoding, errors or universal_newlines.

The other arguments are the same as for the Popen constructor.
