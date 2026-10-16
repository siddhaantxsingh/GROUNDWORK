# socketserver

## socketserver.BaseRequestHandler(request, client_address, server)

This class is instantiated for each request to be handled.  The
constructor sets the instance variables request, client_address
and server, and then calls the handle() method.  To implement a
specific service, all you need to do is to derive a class which
defines a handle() method.

The handle() method can find the request as self.request, the
client address as self.client_address, and the server (in case it
needs access to per-server information) as self.server.  Since a
separate instance is created for each request, the handle() method
can define other arbitrary instance variables.

## socketserver.BaseServer(server_address, RequestHandlerClass)

Base class for server classes. Methods for the caller:

- __init__(server_address, RequestHandlerClass)
- serve_forever(poll_interval=0.5)
- shutdown()
- handle_request()  # if you do not use serve_forever()
- fileno() -> int   # for selector

Methods that may be overridden:

- server_bind()
- server_activate()
- get_request() -> request, client_address
- handle_timeout()
- verify_request(request, client_address)
- server_close()
- process_request(request, client_address)
- shutdown_request(request)
- close_request(request)
- service_actions()
- handle_error()

Methods for derived classes:

- finish_request(request, client_address)

Class variables that may be overridden by derived classes or
instances:

- timeout
- address_family
- socket_type
- allow_reuse_address
- allow_reuse_port

Instance variables:

- RequestHandlerClass
- socket

## socketserver.BaseServer.close_request(self, request)

Called to clean up an individual request.

## socketserver.BaseServer.finish_request(self, request, client_address)

Finish one request by instantiating RequestHandlerClass.

## socketserver.BaseServer.handle_error(self, request, client_address)

Handle an error gracefully. May be overridden.

The default is to print a traceback and continue.

## socketserver.BaseServer.handle_request(self)

Handle one request, possibly blocking. Respects self.timeout.

## socketserver.BaseServer.handle_timeout(self)

Called if no new request arrives within self.timeout. Overridden by ForkingMixIn.

## socketserver.BaseServer.process_request(self, request, client_address)

Call finish_request. Overridden by ForkingMixIn and ThreadingMixIn.

## socketserver.BaseServer.serve_forever(self, poll_interval=0.5)

Handle one request at a time until shutdown. Polls for shutdown every poll_interval seconds. Ignores
self.timeout. If you need to do periodic tasks, do them in
another thread.

## socketserver.BaseServer.server_activate(self)

Called by constructor to activate the server. May be overridden.

## socketserver.BaseServer.server_close(self)

Called to clean-up the server. May be overridden.

## socketserver.BaseServer.service_actions(self)

Called by the serve_forever() loop. May be overridden by a subclass / Mixin to implement any code that
needs to be run during the loop.

## socketserver.BaseServer.shutdown(self)

Stops the serve_forever loop. Blocks until the loop has finished. This must be called while
serve_forever() is running in another thread, or it will
deadlock.

## socketserver.BaseServer.shutdown_request(self, request)

Called to shutdown and close an individual request.

## socketserver.BaseServer.verify_request(self, request, client_address)

Verify the request. May be overridden.

Return True if we should proceed with this request.

## socketserver.DatagramRequestHandler(request, client_address, server)

Define self.rfile and self.wfile for datagram sockets.

## socketserver.ForkingMixIn()

Mix-in class to handle each request in a new process.

## socketserver.ForkingMixIn.collect_children(self, *, blocking=False)

Internal routine to wait for children that have exited.

## socketserver.ForkingMixIn.handle_timeout(self)

Wait for zombies after self.timeout seconds of inactivity. May be extended, do not override.

## socketserver.ForkingMixIn.process_request(self, request, client_address)

Fork a new subprocess to process the request.

## socketserver.ForkingMixIn.service_actions(self)

Collect the zombie child processes regularly in the ForkingMixIn. service_actions is called in the BaseServer's serve_forever loop.

## socketserver.StreamRequestHandler(request, client_address, server)

Define self.rfile and self.wfile for stream sockets.

## socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)

Defaults to synchronous IP stream (i.e., TCP).

Methods for the caller:

- __init__(server_address, RequestHandlerClass, bind_and_activate=True)
- serve_forever(poll_interval=0.5)
- shutdown()
- handle_request()  # if you don't use serve_forever()
- fileno() -> int   # for selector

Methods that may be overridden:

- server_bind()
- server_activate()
- get_request() -> request, client_address
- handle_timeout()
- verify_request(request, client_address)
- process_request(request, client_address)
- shutdown_request(request)
- close_request(request)
- handle_error()

Methods for derived classes:

- finish_request(request, client_address)

Class variables that may be overridden by derived classes or
instances:

- timeout
- address_family
- socket_type
- request_queue_size (only for stream sockets)
- allow_reuse_address
- allow_reuse_port

Instance variables:

- server_address
- RequestHandlerClass
- socket

## socketserver.TCPServer.close_request(self, request)

Called to clean up an individual request.

## socketserver.TCPServer.fileno(self)

Return socket file number. Interface required by selector.

## socketserver.TCPServer.get_request(self)

Get the request and client address from the socket. May be overridden.

## socketserver.TCPServer.server_activate(self)

Called by constructor to activate the server. May be overridden.

## socketserver.TCPServer.server_bind(self)

Called by constructor to bind the socket. May be overridden.

## socketserver.TCPServer.server_close(self)

Called to clean-up the server. May be overridden.

## socketserver.TCPServer.shutdown_request(self, request)

Called to shutdown and close an individual request.

## socketserver.ThreadingMixIn()

Mix-in class to handle each request in a new thread.

## socketserver.ThreadingMixIn.process_request(self, request, client_address)

Start a new thread to process the request.

## socketserver.ThreadingMixIn.process_request_thread(self, request, client_address)

Same as in BaseServer but as a thread. In addition, exception handling is done here.

## socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)

UDP server class.
