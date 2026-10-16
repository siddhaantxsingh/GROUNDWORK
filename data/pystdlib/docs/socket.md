# socket

## socket.AddressFamily(*values)

An enumeration.

## socket.AddressInfo(*values)

An enumeration.

## socket.MsgFlag(*values)

An enumeration.

## socket.SocketIO(sock, mode)

Raw I/O implementation for stream sockets. This class supports the makefile() method on sockets.  It provides
the raw I/O interface on top of a socket object.

## socket.SocketIO.close(self)

Close the SocketIO object. This doesn't close the underlying socket, except if all references to it have disappeared.

## socket.SocketIO.fileno(self)

Return the file descriptor of the underlying socket.

## socket.SocketIO.readable(self)

True if the SocketIO is open for reading.

## socket.SocketIO.readinto(self, b)

If the socket is non-blocking and no bytes are available, None is returned.

If *b* is non-empty, a 0 return value indicates that the connection
was shutdown at the other end.

## socket.SocketIO.seekable(self)

True if the SocketIO is open for seeking.

## socket.SocketIO.writable(self)

True if the SocketIO is open for writing.

## socket.SocketIO.write(self, b)

This can be less than len(b) if not all data could be written. If the socket is non-blocking and no bytes could be written None is returned.

## socket.SocketKind(*values)

An enumeration.

## socket.create_connection(address, timeout=<object object at 0x7fc8a19208c0>, source_address=None, *, all_errors=False)

Convenience function.  Connect to *address* (a 2-tuple ``(host,
port)``) and return the socket object.  Passing the optional
*timeout* parameter will set the timeout on the socket instance
before attempting to connect.  If no *timeout* is supplied, the
global default timeout setting returned by :func:`getdefaulttimeout`
is used.  If *source_address* is set it must be a tuple of (host, port)
for the socket to bind as a source address before making the connection.
A host of '' or port 0 tells the OS to use the default. When a connection
cannot be created, raises the last error if *all_errors* is False,
and an ExceptionGroup of all errors if *all_errors* is True.

## socket.create_server(address, *, family=<AddressFamily.AF_INET: 2>, backlog=None, reuse_port=False, dualstack_ipv6=False)

*family* should be either AF_INET or AF_INET6.
*backlog* is the queue size passed to socket.listen().
*reuse_port* dictates whether to use the SO_REUSEPORT socket option.
*dualstack_ipv6*: if true and the platform supports it, it will
create an AF_INET6 socket able to accept both IPv4 or IPv6
connections. When false it will explicitly disable this option on
platforms that enable it by default (e.g. Linux).

>>> with create_server(('', 8000)) as server:
...     while True:
...         conn, addr = server.accept()
...         # handle new connection

## socket.fromfd(fd, family, type, proto=0)

Create a socket object from a duplicate of the given file descriptor. The remaining arguments are the same as for socket().

## socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)

Translate the host/port argument into a sequence of 5-tuples that contain
all the necessary arguments for creating a socket connected to that service.
host is a domain name, a string representation of an IPv4/v6 address or
None. port is a string service name such as 'http', a numeric port number or
None. By passing None as the value of host and port, you can pass NULL to
the underlying C API.

The family, type and proto arguments can be optionally specified in order to
narrow the list of addresses returned. Passing zero as a value for each of
these arguments selects the full range of results.

## socket.getfqdn(name='')

An empty argument is interpreted as meaning the local host.

First the hostname returned by gethostbyaddr() is checked, then
possibly existing aliases. In case no FQDN is available and `name`
was given, it is returned unchanged. If `name` was empty, '0.0.0.0' or '::',
hostname from gethostname() is returned.

## socket.has_dualstack_ipv6()

Return True if the platform supports creating a SOCK_STREAM socket which can handle both AF_INET and AF_INET6 (IPv4 / IPv6) connections.

## socket.recv_fds(sock, bufsize, maxfds, flags=0)

Receive up to maxfds file descriptors returning the message data and a list containing the descriptors.

## socket.send_fds(sock, buffers, fds, flags=0, address=None)

Send the list of file descriptors fds over an AF_UNIX socket.

## socket.socket(family=-1, type=-1, proto=-1, fileno=None)

A subclass of _socket.socket adding the makefile() method.

## socket.socket.accept(self)

Wait for an incoming connection. Return a new socket representing the connection, and the address of the client. For IP sockets, the address info is a pair (hostaddr, port).

## socket.socket.detach(self)

Close the socket object without closing the underlying file descriptor. The object cannot be used after this call, but the file descriptor can be reused for other purposes. The file descriptor is returned.

## socket.socket.dup(self)

Duplicate the socket. Return a new socket object connected to the same system resource. The new socket is non-inheritable.

## socket.socket.get_inheritable(self)

Get the inheritable flag of the socket

## socket.socket.makefile(self, mode='r', buffering=None, *, encoding=None, errors=None, newline=None)

The arguments are as for io.open() after the filename, except the only supported mode values are 'r' (default), 'w', 'b', or a combination of those.

## socket.socket.sendfile(self, file, offset=0, count=None)

If os.sendfile() is not available (e.g. Windows) or file is not a regular file socket.send() will be used instead. *offset* tells from where to start reading the file. If specified, *count* is the total number of bytes to transmit as opposed to sending the file until EOF is reached. File position is updated on return or also in case of error in which case file.tell() can be used to figure out the number of bytes which were sent. The socket must be of SOCK_STREAM type. Non-blocking sockets are not supported.

## socket.socket.set_inheritable(self, inheritable)

Set the inheritable flag of the socket

## socket.socketpair(family=None, type=<SocketKind.SOCK_STREAM: 1>, proto=0)

socketpair([family[, type[, proto]]]) -> (socket object, socket object) Create a pair of socket objects from the sockets returned by the platform socketpair() function. The arguments are the same as for socket() except the default family is AF_UNIX if defined on the platform; otherwise, the default is AF_INET.
