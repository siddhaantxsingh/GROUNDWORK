# ctypes

## ctypes.CDLL(name, mode=0, handle=None, use_errno=False, use_last_error=False, winmode=None)

The exported functions can be accessed as attributes, or by
indexing with the function name.  Examples:

<obj>.qsort -> callable object
<obj>['qsort'] -> callable object

Calling the functions releases the Python GIL during the call and
reacquires it afterwards.

## ctypes.CFUNCTYPE(restype, *argtypes, **kw)

restype: the result type
argtypes: a sequence specifying the argument types

The function prototype can be called in different ways to create a
callable object:

prototype(integer address) -> foreign function
prototype(callable) -> create and return a C callable function from callable
prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
prototype((function name, dll object)[, paramflags]) -> foreign function exported by name

## ctypes.PyDLL(name, mode=0, handle=None, use_errno=False, use_last_error=False, winmode=None)

This class represents the Python library itself. It allows accessing Python API functions. The GIL is not released, and Python exceptions are handled correctly.

## ctypes.c_buffer(init, size=None)

create_string_buffer(aBytes) -> character array create_string_buffer(anInteger) -> character array create_string_buffer(aBytes, anInteger) -> character array

## ctypes.create_string_buffer(init, size=None)

create_string_buffer(aBytes) -> character array create_string_buffer(anInteger) -> character array create_string_buffer(aBytes, anInteger) -> character array

## ctypes.create_unicode_buffer(init, size=None)

create_unicode_buffer(aString) -> character array create_unicode_buffer(anInteger) -> character array create_unicode_buffer(aString, anInteger) -> character array

## ctypes.string_at(ptr, size=-1)

Return the byte string at void *ptr.

## ctypes.wstring_at(ptr, size=-1)

Return the wide-character string at void *ptr.
