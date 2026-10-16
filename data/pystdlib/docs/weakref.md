# weakref

## weakref.KeyedRef(ob, callback, key)

This is used in the WeakValueDictionary to avoid having to create
a function object for each key stored in the mapping.  A shared
callback object can use the 'key' attribute of a KeyedRef instead
of getting a reference to the key from an enclosing scope.

## weakref.WeakKeyDictionary(dict=None)

Entries in the dictionary will be discarded when there is no
longer a strong reference to the key. This can be used to
associate additional data with an object owned by other parts of
an application without adding attributes to those objects. This
can be especially useful with objects that override attribute
accesses.

## weakref.WeakKeyDictionary.keyrefs(self)

The references are not guaranteed to be 'live' at the time
they are used, so the result of calling the references needs
to be checked before being used.  This can be used to avoid
creating references that will cause the garbage collector to
keep the keys around longer than needed.

## weakref.WeakMethod(meth, callback=None)

A custom `weakref.ref` subclass which simulates a weak reference to a bound method, working around the lifetime problem of bound methods.

## weakref.WeakValueDictionary(other=(), /, **kw)

Mapping class that references values weakly. Entries in the dictionary will be discarded when no strong
reference to the value exists anymore

## weakref.WeakValueDictionary.itervaluerefs(self)

The references are not guaranteed to be 'live' at the time
they are used, so the result of calling the references needs
to be checked before being used.  This can be used to avoid
creating references that will cause the garbage collector to
keep the values around longer than needed.

## weakref.WeakValueDictionary.valuerefs(self)

The references are not guaranteed to be 'live' at the time
they are used, so the result of calling the references needs
to be checked before being used.  This can be used to avoid
creating references that will cause the garbage collector to
keep the values around longer than needed.

## weakref.finalize(obj, func, /, *args, **kwargs)

finalize(obj, func, *args, **kwargs) returns a callable finalizer
object which will be called when obj is garbage collected. The
first time the finalizer is called it evaluates func(*arg, **kwargs)
and returns the result. After this the finalizer is dead, and
calling it just returns None.

When the program exits any remaining finalizers for which the
atexit attribute is true will be run in reverse order of creation.
By default atexit is true.

## weakref.finalize.detach(self)

If alive then mark as dead and return (obj, func, args, kwargs); otherwise return None

## weakref.finalize.peek(self)

If alive then return (obj, func, args, kwargs); otherwise return None
