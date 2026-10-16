# ftplib

## ftplib.FTP(host='', user='', passwd='', acct='', timeout=<object object at 0x7fc8a19208c0>, source_address=None, *, encoding='utf-8')

An FTP client class. To create a connection, call the class using these arguments:
        host, user, passwd, acct, timeout, source_address, encoding

The first four arguments are all strings, and have default value ''.
The parameter ´timeout´ must be numeric and defaults to None if not
passed, meaning that no timeout will be set on any ftp socket(s).
If a timeout is passed, then this is now the default timeout for all ftp
socket operations for this instance.
The last parameter is the encoding of filenames, which defaults to utf-8.

Then use self.connect() with optional host and port argument.

To download a file, use ftp.retrlines('RETR ' + filename),
or ftp.retrbinary() with slightly different arguments.
To upload a file, use ftp.storlines() or ftp.storbinary(),
which have an open file as argument (see their definitions
below for details).
The download/upload functions first issue appropriate TYPE
and PORT or PASV commands.

## ftplib.FTP.abort(self)

Abort a file transfer. Uses out-of-band data. This does not follow the procedure from the RFC to send Telnet IP and Synch; that doesn't seem to work with the servers I've tried. Instead, just send the ABOR command as OOB data.

## ftplib.FTP.acct(self, password)

Send new account name.

## ftplib.FTP.close(self)

Close the connection without assuming anything about it.

## ftplib.FTP.connect(self, host='', port=0, timeout=-999, source_address=None)

Connect to host. Arguments are: - host: hostname to connect to (string, default previous host) - port: port to connect to (integer, default previous port) - timeout: the timeout to set against the ftp socket(s) - source_address: a 2-tuple (host, port) for the socket to bind to as its source address before connecting.

## ftplib.FTP.cwd(self, dirname)

Change to a directory.

## ftplib.FTP.debug(self, level)

Set the debugging level. The required argument level means: 0: no debugging output (default) 1: print commands and responses but not body text etc. 2: also print raw lines read and sent before stripping CR/LF

## ftplib.FTP.delete(self, filename)

Delete a file.

## ftplib.FTP.dir(self, *args)

By default list current directory to stdout. Optional last argument is callback function; all non-empty arguments before it are concatenated to the LIST command. (This *should* only be used for a pathname.)

## ftplib.FTP.getwelcome(self)

Get the welcome message from the server. (this is read and squirreled away by connect())

## ftplib.FTP.login(self, user='', passwd='', acct='')

Login, default anonymous.

## ftplib.FTP.makepasv(self)

Internal: Does the PASV or EPSV handshake -> (address, port)

## ftplib.FTP.makeport(self)

Create a new socket and send a PORT command for it.

## ftplib.FTP.mkd(self, dirname)

Make a directory, return its full pathname.

## ftplib.FTP.mlsd(self, path='', facts=[])

If path is omitted the current directory is assumed. "facts" is a list of strings representing the type of information desired (e.g. ["type", "size", "perm"]).

Return a generator object yielding a tuple of two elements
for every file found in path.
First element is the file name, the second one is a dictionary
including a variable number of "facts" depending on the server
and whether "facts" argument has been provided.

## ftplib.FTP.nlst(self, *args)

Return a list of files in a given directory (default the current).

## ftplib.FTP.ntransfercmd(self, cmd, rest=None)

If the transfer is active, send a port command and the
transfer command, and accept the connection.  If the server is
passive, send a pasv command, connect to it, and start the
transfer command.  Either way, return the socket for the
connection and the expected size of the transfer.  The
expected size may be None if it could not be determined.

Optional `rest' argument can be a string that is sent as the
argument to a REST command.  This is essentially a server
marker used to tell the server to skip over any data up to the
given marker.

## ftplib.FTP.pwd(self)

Return current working directory.

## ftplib.FTP.quit(self)

Quit, and close the connection.

## ftplib.FTP.rename(self, fromname, toname)

Rename a file.

## ftplib.FTP.retrbinary(self, cmd, callback, blocksize=8192, rest=None)

Retrieve data in binary mode. A new port is created for you.

Args:
  cmd: A RETR command.
  callback: A single parameter callable to be called on each
            block of data read.
  blocksize: The maximum number of bytes to read from the
             socket at one time.  [default: 8192]
  rest: Passed to transfercmd().  [default: None]

Returns:
  The response code.

## ftplib.FTP.retrlines(self, cmd, callback=None)

Retrieve data in line mode. A new port is created for you.

Args:
  cmd: A RETR, LIST, or NLST command.
  callback: An optional single parameter callable that is called
            for each line with the trailing CRLF stripped.
            [default: print_line()]

Returns:
  The response code.

## ftplib.FTP.rmd(self, dirname)

Remove a directory.

## ftplib.FTP.sendcmd(self, cmd)

Send a command and return the response.

## ftplib.FTP.sendeprt(self, host, port)

Send an EPRT command with the current host and the given port number.

## ftplib.FTP.sendport(self, host, port)

Send a PORT command with the current host and the given port number.

## ftplib.FTP.set_debuglevel(self, level)

Set the debugging level. The required argument level means: 0: no debugging output (default) 1: print commands and responses but not body text etc. 2: also print raw lines read and sent before stripping CR/LF

## ftplib.FTP.set_pasv(self, val)

Use passive or active mode for data transfers. With a false argument, use the normal PORT mode, With a true argument, use the PASV command.

## ftplib.FTP.size(self, filename)

Retrieve the size of a file.

## ftplib.FTP.storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None)

A new port is created for you.

Args:
  cmd: A STOR command.
  fp: A file-like object with a read(num_bytes) method.
  blocksize: The maximum data size to read from fp and send over
             the connection at once.  [default: 8192]
  callback: An optional single parameter callable that is called on
            each block of data after it is sent.  [default: None]
  rest: Passed to transfercmd().  [default: None]

Returns:
  The response code.

## ftplib.FTP.storlines(self, cmd, fp, callback=None)

A new port is created for you.

Args:
  cmd: A STOR command.
  fp: A file-like object with a readline() method.
  callback: An optional single parameter callable that is called on
            each line after it is sent.  [default: None]

Returns:
  The response code.

## ftplib.FTP.transfercmd(self, cmd, rest=None)

Like ntransfercmd() but returns only the socket.

## ftplib.FTP.voidcmd(self, cmd)

Send a command and expect a response beginning with '2'.

## ftplib.FTP.voidresp(self)

Expect a response beginning with '2'.

## ftplib.FTP_TLS(host='', user='', passwd='', acct='', *, context=None, timeout=<object object at 0x7fc8a19208c0>, source_address=None, encoding='utf-8')

Connect as usual to port 21 implicitly securing the FTP control
connection before authenticating.

Securing the data connection requires user to explicitly ask
for it by calling prot_p() method.

Usage example:
>>> from ftplib import FTP_TLS
>>> ftps = FTP_TLS('ftp.python.org')
>>> ftps.login()  # login anonymously previously securing control channel
'230 Guest login ok, access restrictions apply.'
>>> ftps.prot_p()  # switch to secure data connection
'200 Protection level set to P'
>>> ftps.retrlines('LIST')  # list directory content securely
total 9
drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
-rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
'226 Transfer complete.'
>>> ftps.quit()
'221 Goodbye.'
>>>

## ftplib.FTP_TLS.auth(self)

Set up secure control connection by using TLS/SSL.

## ftplib.FTP_TLS.ccc(self)

Switch back to a clear-text control connection.

## ftplib.FTP_TLS.prot_c(self)

Set up clear text data connection.

## ftplib.FTP_TLS.prot_p(self)

Set up secure data connection.

## ftplib.ftpcp(source, sourcename, target, targetname='', type='I')

Copy file from one FTP-instance to another.

## ftplib.parse150(resp)

Parse the '150' response for a RETR request. Returns the expected transfer size or None; size is not guaranteed to be present in the 150 message.

## ftplib.parse227(resp)

Parse the '227' response for a PASV request. Raises error_proto if it does not contain '(h1,h2,h3,h4,p1,p2)' Return ('host.addr.as.numbers', port#) tuple.

## ftplib.parse229(resp, peer)

Parse the '229' response for an EPSV request. Raises error_proto if it does not contain '(|||port|)' Return ('host.addr.as.numbers', port#) tuple.

## ftplib.parse257(resp)

Parse the '257' response for a MKD or PWD request. This is a response to a MKD or PWD request: a directory name. Returns the directoryname in the 257 reply.

## ftplib.print_line(line)

Default retrlines callback to print a line.

## ftplib.test()

Test program. Usage: ftplib [-d] [-r[file]] host [-l[dir]] [-d[dir]] [-p] [file] ...

Options:
  -d        increase debugging level
  -r[file]  set alternate ~/.netrc file

Commands:
  -l[dir]   list directory
  -d[dir]   change the current directory
  -p        toggle passive and active mode
  file      retrieve the file and write it to stdout
