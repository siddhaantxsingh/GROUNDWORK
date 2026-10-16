# warnings

## warnings.catch_warnings(*, record=False, module=None, action=None, category=<class 'Warning'>, lineno=0, append=False)

The 'record' argument specifies whether warnings should be captured by a
custom implementation of warnings.showwarning() and be appended to a list
returned by the context manager. Otherwise None is returned by the context
manager. The objects appended to the list are arguments whose attributes
mirror the arguments to showwarning().

The 'module' argument is to specify an alternative module to the module
named 'warnings' and imported under that name. This argument is only useful
when testing the warnings module itself.

If the 'action' argument is not None, the remaining arguments are passed
to warnings.simplefilter() as if it were called immediately on entering the
context.

## warnings.deprecated(message: str, /, *, category: type[Warning] | None = <class 'DeprecationWarning'>, stacklevel: int = 1) -> None

When this decorator is applied to an object, the type checker
will generate a diagnostic on usage of the deprecated object.

Usage:

@deprecated("Use B instead")
    class A:
        pass

@deprecated("Use g instead")
    def f():
        pass

@overload
    @deprecated("int support is deprecated")
    def g(x: int) -> int: ...
    @overload
    def g(x: str) -> int: ...

The warning specified by *category* will be emitted at runtime
on use of deprecated objects. For functions, that happens on calls;
for classes, on instantiation and on creation of subclasses.
If the *category* is ``None``, no warning is emitted at runtime.
The *stacklevel* determines where the
warning is emitted. If it is ``1`` (the default), the warning
is emitted at the direct caller of the deprecated object; if it
is higher, it is emitted further up the stack.
Static type checker behavior is not affected by the *category*
and *stacklevel* arguments.

The deprecation message passed to the decorator is saved in the
``__deprecated__`` attribute on the decorated object.
If applied to an overload, the decorator
must be after the ``@overload`` decorator for the attribute to
exist on the overload as returned by ``get_overloads()``.

See PEP 702 for details.

## warnings.filterwarnings(action, message='', category=<class 'Warning'>, module='', lineno=0, append=False)

'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'message' -- a regex that the warning message must match
'category' -- a class that the warning must be a subclass of
'module' -- a regex that the module name must match
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters

## warnings.formatwarning(message, category, filename, lineno, line=None)

Function to format a warning the standard way.

## warnings.resetwarnings()

Clear the list of warning filters, so that no filters are active.

## warnings.showwarning(message, category, filename, lineno, file=None, line=None)

Hook to write a warning to a file; replace if you like.

## warnings.simplefilter(action, category=<class 'Warning'>, lineno=0, append=False)

A simple filter matches all modules and messages.
'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'category' -- a class that the warning must be a subclass of
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters
