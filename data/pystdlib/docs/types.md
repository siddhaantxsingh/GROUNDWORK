# types

## types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)

This is a descriptor, used to define attributes that act differently
when accessed through an instance and through a class.  Instance access
remains normal, but access to an attribute through a class will be
routed to the class's __getattr__ method; this is done by raising
AttributeError.

This allows one to have properties active on an instance, and have
virtual attributes on the class with the same name.  (Enum used this
between Python versions 3.4 - 3.9 .)

Subclass from this to use a different method of accessing virtual
attributes and still be treated properly by the inspect module.  (Enum
uses this since Python 3.10 .)

## types.GenericAlias(origin, args, /)

Represent a PEP 585 generic type For example, for t = list[int], t.__origin__ is list and t.__args__
is (int,).

## types.SimpleNamespace(mapping_or_iterable=(), /, **kwargs)

A simple attribute-based namespace.

## types.UnionType()

Represent a PEP 604 union type E.g. for int | str

## types.coroutine(func)

Convert regular generator function to a coroutine.

## types.get_original_bases(cls, /)

Examples::

from typing import TypeVar, Generic, NamedTuple, TypedDict

T = TypeVar("T")
    class Foo(Generic[T]): ...
    class Bar(Foo[int], float): ...
    class Baz(list[str]): ...
    Eggs = NamedTuple("Eggs", [("a", int), ("b", str)])
    Spam = TypedDict("Spam", {"a": int, "b": str})

assert get_original_bases(Bar) == (Foo[int], float)
    assert get_original_bases(Baz) == (list[str],)
    assert get_original_bases(Eggs) == (NamedTuple,)
    assert get_original_bases(Spam) == (TypedDict,)
    assert get_original_bases(int) == (object,)

## types.new_class(name, bases=(), kwds=None, exec_body=None)

Create a class object dynamically using the appropriate metaclass.

## types.prepare_class(name, bases=(), kwds=None)

Returns (metaclass, namespace, kwds) as a 3-tuple

*metaclass* is the appropriate metaclass
*namespace* is the prepared class namespace
*kwds* is an updated copy of the passed in kwds argument with any
'metaclass' entry removed. If no kwds argument is passed in, this will
be an empty dict.

## types.resolve_bases(bases)

Resolve MRO entries dynamically as specified by PEP 560.
