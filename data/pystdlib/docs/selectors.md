# selectors

## selectors.BaseSelector()

Selector abstract base class. A selector supports registering file objects to be monitored for specific
I/O events.

A file object is a file descriptor or any object with a `fileno()` method.
An arbitrary object can be attached to the file object, which can be used
for example to store context information, a callback, etc.

A selector can use various implementations (select(), poll(), epoll()...)
depending on the platform. The default `Selector` class uses the most
efficient implementation on the current platform.

## selectors.BaseSelector.close(self)

Close the selector. This must be called to make sure that any underlying resource is freed.

## selectors.BaseSelector.get_key(self, fileobj)

Return the key associated to a registered file object. Returns:
SelectorKey for this file object

## selectors.BaseSelector.get_map(self)

Return a mapping of file objects to selector keys.

## selectors.BaseSelector.modify(self, fileobj, events, data=None)

Parameters:
fileobj -- file object or file descriptor
events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
data    -- attached data

Returns:
SelectorKey instance

Raises:
Anything that unregister() or register() raises

## selectors.BaseSelector.register(self, fileobj, events, data=None)

Register a file object. Parameters:
fileobj -- file object or file descriptor
events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
data    -- attached data

Returns:
SelectorKey instance

Raises:
ValueError if events is invalid
KeyError if fileobj is already registered
OSError if fileobj is closed or otherwise is unacceptable to
        the underlying system call (if a system call is made)

Note:
OSError may or may not be raised

## selectors.BaseSelector.select(self, timeout=None)

Parameters:
timeout -- if timeout > 0, this specifies the maximum wait time, in
           seconds
           if timeout <= 0, the select() call won't block, and will
           report the currently ready file objects
           if timeout is None, select() will block until a monitored
           file object becomes ready

Returns:
list of (key, events) for ready file objects
`events` is a bitwise mask of EVENT_READ|EVENT_WRITE

## selectors.BaseSelector.unregister(self, fileobj)

Unregister a file object. Parameters:
fileobj -- file object or file descriptor

Returns:
SelectorKey instance

Raises:
KeyError if fileobj is not registered

Note:
If fileobj is registered but has since been closed this does
*not* raise OSError (even if the wrapped syscall does)

## selectors.DefaultSelector()

Epoll-based selector.

## selectors.EpollSelector()

Epoll-based selector.

## selectors.PollSelector()

Poll-based selector.

## selectors.SelectSelector()

Select-based selector.

## selectors.SelectorKey(fileobj, fd, events, data)

Object used to associate a file object to its backing file descriptor, selected event mask, and attached data.
