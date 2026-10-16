# builtins

## builtins.ArithmeticError(...)

Base class for arithmetic errors.

## builtins.AssertionError(...)

Assertion failed.

## builtins.AttributeError(...)

Attribute not found.

## builtins.BaseException(...)

Common base class for all exceptions

## builtins.BaseException.add_note(self, object, /)

Exception.add_note(note) -- add a note to the exception

## builtins.BaseException.with_traceback(self, object, /)

Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.

## builtins.BaseExceptionGroup(...)

A combination of multiple unrelated exceptions.

## builtins.BlockingIOError(...)

I/O operation would block.

## builtins.BrokenPipeError(...)

Broken pipe.

## builtins.BufferError(...)

Buffer error.

## builtins.BytesWarning(...)

Base class for warnings about bytes and buffer related problems, mostly related to conversion from str or comparing to str.

## builtins.ChildProcessError(...)

Child process error.

## builtins.ConnectionAbortedError(...)

Connection aborted.

## builtins.ConnectionError(...)

Connection error.

## builtins.ConnectionRefusedError(...)

Connection refused.

## builtins.ConnectionResetError(...)

Connection reset.

## builtins.DeprecationWarning(...)

Base class for warnings about deprecated features.

## builtins.EOFError(...)

Read beyond end of file.

## builtins.EncodingWarning(...)

Base class for warnings about encodings.

## builtins.EnvironmentError(...)

Base class for I/O related errors.

## builtins.Exception(...)

Common base class for all non-exit exceptions.

## builtins.FileExistsError(...)

File already exists.

## builtins.FileNotFoundError(...)

File not found.

## builtins.FloatingPointError(...)

Floating-point operation failed.

## builtins.FutureWarning(...)

Base class for warnings about constructs that will change semantically in the future.

## builtins.GeneratorExit(...)

Request that a generator exit.

## builtins.IOError(...)

Base class for I/O related errors.

## builtins.ImportError(...)

Import can't find module, or can't find name in module.

## builtins.ImportWarning(...)

Base class for warnings about probable mistakes in module imports

## builtins.IndentationError(...)

Improper indentation.

## builtins.IndexError(...)

Sequence index out of range.

## builtins.InterruptedError(...)

Interrupted by signal.

## builtins.IsADirectoryError(...)

Operation doesn't work on directories.

## builtins.KeyError(...)

Mapping key not found.

## builtins.KeyboardInterrupt(...)

Program interrupted by user.

## builtins.LookupError(...)

Base class for lookup errors.

## builtins.MemoryError(...)

Out of memory.

## builtins.ModuleNotFoundError(...)

Module not found.

## builtins.NameError(...)

Name not found globally.

## builtins.NotADirectoryError(...)

Operation only works on directories.

## builtins.NotImplementedError(...)

Method or function hasn't been implemented yet.

## builtins.OSError(...)

Base class for I/O related errors.

## builtins.OverflowError(...)

Result too large to be represented.

## builtins.PendingDeprecationWarning(...)

Base class for warnings about features which will be deprecated in the future.

## builtins.PermissionError(...)

Not enough permissions.

## builtins.ProcessLookupError(...)

Process not found.

## builtins.PythonFinalizationError(...)

Operation blocked during Python finalization.

## builtins.RecursionError(...)

Recursion limit exceeded.

## builtins.ReferenceError(...)

Weak ref proxy used after referent went away.

## builtins.ResourceWarning(...)

Base class for warnings about resource usage.

## builtins.RuntimeError(...)

Unspecified run-time error.

## builtins.RuntimeWarning(...)

Base class for warnings about dubious runtime behavior.

## builtins.StopAsyncIteration(...)

Signal the end from iterator.__anext__().

## builtins.StopIteration(...)

Signal the end from iterator.__next__().

## builtins.SyntaxError(...)

Invalid syntax.

## builtins.SyntaxWarning(...)

Base class for warnings about dubious syntax.

## builtins.SystemError(...)

Internal error in the Python interpreter. Please report this to the Python maintainer, along with the traceback,
the Python version, and the hardware/OS platform and version.

## builtins.SystemExit(...)

Request to exit from the interpreter.

## builtins.TabError(...)

Improper mixture of spaces and tabs.

## builtins.TimeoutError(...)

Timeout expired.

## builtins.TypeError(...)

Inappropriate argument type.

## builtins.UnboundLocalError(...)

Local name referenced but not bound to a value.

## builtins.UnicodeDecodeError(...)

Unicode decoding error.

## builtins.UnicodeEncodeError(...)

Unicode encoding error.

## builtins.UnicodeError(...)

Unicode related error.

## builtins.UnicodeTranslateError(...)

Unicode translation error.

## builtins.UnicodeWarning(...)

Base class for warnings about Unicode related problems, mostly related to conversion problems.

## builtins.UserWarning(...)

Base class for warnings generated by user code.

## builtins.ValueError(...)

Inappropriate argument value (of correct type).

## builtins.Warning(...)

Base class for warning categories.

## builtins.ZeroDivisionError(...)

Second argument to a division or modulo operation was zero.

## builtins.abs(x, /)

Return the absolute value of the argument.

## builtins.aiter(async_iterable, /)

Return an AsyncIterator for an AsyncIterable object.

## builtins.all(iterable, /)

Return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True.

## builtins.anext(...)

Return the next item from the async iterator. If default is given and the async iterator is exhausted,
it is returned instead of raising StopAsyncIteration.

## builtins.any(iterable, /)

Return True if bool(x) is True for any x in the iterable. If the iterable is empty, return False.

## builtins.ascii(obj, /)

As repr(), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
repr() using \\x, \\u or \\U escapes. This generates a string similar
to that returned by repr() in Python 2.

## builtins.bin(number, /)

Return the binary representation of an integer. >>> bin(2796202)
'0b1010101010101010101010'

## builtins.bool(object=False, /)

The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

## builtins.breakpoint(*args, **kws)

Call sys.breakpointhook(*args, **kws). sys.breakpointhook() must accept whatever arguments are passed. By default, this drops you into the pdb debugger.

## builtins.bytearray(...)

Construct a mutable bytearray object from: - an iterable yielding integers in range(256) - a text string encoded using the specified encoding - a bytes or a buffer object - any object implementing the buffer API. - an integer

## builtins.bytearray.append(self, item, /)

Append a single item to the end of the bytearray. item
  The item to be appended.

## builtins.bytearray.capitalize(self, /)

Return a copy of B with only its first character capitalized (ASCII) and the rest lower-cased.

## builtins.bytearray.center(self, width, fillchar=b' ', /)

Return a centered string of length width. Padding is done using the specified fill character.

## builtins.bytearray.clear(self, /)

Remove all items from the bytearray.

## builtins.bytearray.copy(self, /)

Return a copy of B.

## builtins.bytearray.count(...)

Return the number of non-overlapping occurrences of subsection 'sub' in bytes B[start:end]. start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.

## builtins.bytearray.decode(self, /, encoding='utf-8', errors='strict')

encoding
  The encoding with which to decode the bytearray.
errors
  The error handling scheme to use for the handling of decoding
  errors.  The default is 'strict' meaning that decoding errors
  raise a UnicodeDecodeError.  Other possible values are 'ignore'
  and 'replace' as well as any other name registered with
  codecs.register_error that can handle UnicodeDecodeErrors.

## builtins.bytearray.endswith(...)

suffix
  A bytes or a tuple of bytes to try.
start
  Optional start position. Default: start of the bytearray.
end
  Optional stop position. Default: end of the bytearray.

## builtins.bytearray.expandtabs(self, /, tabsize=8)

Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

## builtins.bytearray.extend(self, iterable_of_ints, /)

Append all the items from the iterator or sequence to the end of the bytearray. iterable_of_ints
  The iterable of items to append.

## builtins.bytearray.find(...)

Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start:end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Return -1 on failure.

## builtins.bytearray.fromhex(type, string, /)

Create a bytearray object from a string of hexadecimal numbers. Spaces between two numbers are accepted.
Example:
    bytearray.fromhex('B9 01EF') -> bytearray(b'\\xb9\\x01\\xef')

## builtins.bytearray.hex(...)

sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from
    the right, negative values count from the left.

Example:
>>> value = bytearray([0xb9, 0x01, 0xef])
>>> value.hex()
'b901ef'
>>> value.hex(':')
'b9:01:ef'
>>> value.hex(':', 2)
'b9:01ef'
>>> value.hex(':', -2)
'b901:ef'

## builtins.bytearray.index(...)

Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start:end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.

## builtins.bytearray.insert(self, index, item, /)

Insert a single item into the bytearray before the given index. index
  The index where the value is to be inserted.
item
  The item to be inserted.

## builtins.bytearray.isalnum(self, /)

Return True if all characters in B are alphanumeric and there is at least one character in B, False otherwise.

## builtins.bytearray.isalpha(self, /)

Return True if all characters in B are alphabetic and there is at least one character in B, False otherwise.

## builtins.bytearray.isascii(self, /)

Return True if B is empty or all characters in B are ASCII, False otherwise.

## builtins.bytearray.isdigit(self, /)

Return True if all characters in B are digits and there is at least one character in B, False otherwise.

## builtins.bytearray.islower(self, /)

Return True if all cased characters in B are lowercase and there is at least one cased character in B, False otherwise.

## builtins.bytearray.isspace(self, /)

Return True if all characters in B are whitespace and there is at least one character in B, False otherwise.

## builtins.bytearray.istitle(self, /)

Return True if B is a titlecased string and there is at least one character in B, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

## builtins.bytearray.isupper(self, /)

Return True if all cased characters in B are uppercase and there is at least one cased character in B, False otherwise.

## builtins.bytearray.join(self, iterable_of_bytes, /)

Concatenate any number of bytes/bytearray objects. The bytearray whose method is called is inserted in between each
pair.

The result is returned as a new bytearray object.

## builtins.bytearray.ljust(self, width, fillchar=b' ', /)

Return a left-justified string of length width. Padding is done using the specified fill character.

## builtins.bytearray.lower(self, /)

Return a copy of B with all ASCII characters converted to lowercase.

## builtins.bytearray.lstrip(self, bytes=None, /)

Strip leading bytes contained in the argument. If the argument is omitted or None, strip leading ASCII whitespace.

## builtins.bytearray.maketrans(frm, to, /)

Convert a function to be a static method. A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

class C:
         @staticmethod
         def f(arg1, arg2, argN):
             ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.

## builtins.bytearray.partition(self, sep, /)

Partition the bytearray into three parts using the given separator. This will search for the separator sep in the bytearray.  If the
separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it as new
bytearray objects.

If the separator is not found, returns a 3-tuple containing the copy
of the original bytearray object and two empty bytearray objects.

## builtins.bytearray.pop(self, index=-1, /)

index
    The index from where to remove the item.
    -1 (the default value) means remove the last item.

If no index argument is given, will pop the last item.

## builtins.bytearray.remove(self, value, /)

Remove the first occurrence of a value in the bytearray. value
  The value to remove.

## builtins.bytearray.removeprefix(self, prefix, /)

Return a bytearray with the given prefix string removed if present. If the bytearray starts with the prefix string, return
bytearray[len(prefix):].  Otherwise, return a copy of the original
bytearray.

## builtins.bytearray.removesuffix(self, suffix, /)

Return a bytearray with the given suffix string removed if present. If the bytearray ends with the suffix string and that suffix is not
empty, return bytearray[:-len(suffix)].  Otherwise, return a copy of
the original bytearray.

## builtins.bytearray.replace(self, old, new, count=-1, /)

Return a copy with all occurrences of substring old replaced by new. count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

## builtins.bytearray.reverse(self, /)

Reverse the order of the values in B in place.

## builtins.bytearray.rfind(...)

Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start:end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Return -1 on failure.

## builtins.bytearray.rindex(...)

Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start:end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.

## builtins.bytearray.rjust(self, width, fillchar=b' ', /)

Return a right-justified string of length width. Padding is done using the specified fill character.

## builtins.bytearray.rpartition(self, sep, /)

Partition the bytearray into three parts using the given separator. This will search for the separator sep in the bytearray, starting at
the end.  If the separator is found, returns a 3-tuple containing
the part before the separator, the separator itself, and the part
after it as new bytearray objects.

If the separator is not found, returns a 3-tuple containing two
empty bytearray objects and the copy of the original bytearray
object.

## builtins.bytearray.rsplit(self, /, sep=None, maxsplit=-1)

Return a list of the sections in the bytearray, using sep as the delimiter. sep
    The delimiter according which to split the bytearray.
    None (the default value) means split on ASCII whitespace
    characters (space, tab, return, newline, formfeed, vertical tab).
  maxsplit
    Maximum number of splits to do.
    -1 (the default value) means no limit.

Splitting is done starting at the end of the bytearray and working
to the front.

## builtins.bytearray.rstrip(self, bytes=None, /)

Strip trailing bytes contained in the argument. If the argument is omitted or None, strip trailing ASCII whitespace.

## builtins.bytearray.split(self, /, sep=None, maxsplit=-1)

Return a list of the sections in the bytearray, using sep as the delimiter. sep
  The delimiter according which to split the bytearray.
  None (the default value) means split on ASCII whitespace
  characters (space, tab, return, newline, formfeed, vertical tab).
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.

## builtins.bytearray.splitlines(self, /, keepends=False)

Return a list of the lines in the bytearray, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends
is given and true.

## builtins.bytearray.startswith(...)

prefix
  A bytes or a tuple of bytes to try.
start
  Optional start position. Default: start of the bytearray.
end
  Optional stop position. Default: end of the bytearray.

## builtins.bytearray.strip(self, bytes=None, /)

Strip leading and trailing bytes contained in the argument. If the argument is omitted or None, strip leading and trailing ASCII
whitespace.

## builtins.bytearray.swapcase(self, /)

Return a copy of B with uppercase ASCII characters converted to lowercase ASCII and vice versa.

## builtins.bytearray.title(self, /)

Return a titlecased version of B, i.e. ASCII words start with uppercase characters, all remaining cased characters have lowercase.

## builtins.bytearray.translate(self, table, /, delete=b'')

Return a copy with each character mapped by the given translation table. table
    Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are
removed.  The remaining characters are mapped through the given
translation table.

## builtins.bytearray.upper(self, /)

Return a copy of B with all ASCII characters converted to uppercase.

## builtins.bytearray.zfill(self, width, /)

Pad a numeric string with zeros on the left, to fill a field of the given width. The original string is never truncated.

## builtins.bytes(...)

Construct an immutable array of bytes from: - an iterable yielding integers in range(256) - a text string encoded using the specified encoding - any object implementing the buffer API. - an integer

## builtins.bytes.capitalize(self, /)

Return a copy of B with only its first character capitalized (ASCII) and the rest lower-cased.

## builtins.bytes.center(self, width, fillchar=b' ', /)

Return a centered string of length width. Padding is done using the specified fill character.

## builtins.bytes.count(...)

Return the number of non-overlapping occurrences of subsection 'sub' in bytes B[start:end]. start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.

## builtins.bytes.decode(self, /, encoding='utf-8', errors='strict')

encoding
  The encoding with which to decode the bytes.
errors
  The error handling scheme to use for the handling of decoding
  errors.  The default is 'strict' meaning that decoding errors
  raise a UnicodeDecodeError.  Other possible values are 'ignore'
  and 'replace' as well as any other name registered with
  codecs.register_error that can handle UnicodeDecodeErrors.

## builtins.bytes.endswith(...)

suffix
  A bytes or a tuple of bytes to try.
start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.

## builtins.bytes.expandtabs(self, /, tabsize=8)

Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

## builtins.bytes.find(...)

Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Return -1 on failure.

## builtins.bytes.fromhex(type, string, /)

Create a bytes object from a string of hexadecimal numbers. Spaces between two numbers are accepted.
Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.

## builtins.bytes.hex(...)

sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from
    the right, negative values count from the left.

Example:
>>> value = b'\xb9\x01\xef'
>>> value.hex()
'b901ef'
>>> value.hex(':')
'b9:01:ef'
>>> value.hex(':', 2)
'b9:01ef'
>>> value.hex(':', -2)
'b901:ef'

## builtins.bytes.index(...)

Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.

## builtins.bytes.isalnum(self, /)

Return True if all characters in B are alphanumeric and there is at least one character in B, False otherwise.

## builtins.bytes.isalpha(self, /)

Return True if all characters in B are alphabetic and there is at least one character in B, False otherwise.

## builtins.bytes.isascii(self, /)

Return True if B is empty or all characters in B are ASCII, False otherwise.

## builtins.bytes.isdigit(self, /)

Return True if all characters in B are digits and there is at least one character in B, False otherwise.

## builtins.bytes.islower(self, /)

Return True if all cased characters in B are lowercase and there is at least one cased character in B, False otherwise.

## builtins.bytes.isspace(self, /)

Return True if all characters in B are whitespace and there is at least one character in B, False otherwise.

## builtins.bytes.istitle(self, /)

Return True if B is a titlecased string and there is at least one character in B, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

## builtins.bytes.isupper(self, /)

Return True if all cased characters in B are uppercase and there is at least one cased character in B, False otherwise.

## builtins.bytes.join(self, iterable_of_bytes, /)

The bytes whose method is called is inserted in between each pair.

The result is returned as a new bytes object.

Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.

## builtins.bytes.ljust(self, width, fillchar=b' ', /)

Return a left-justified string of length width. Padding is done using the specified fill character.

## builtins.bytes.lower(self, /)

Return a copy of B with all ASCII characters converted to lowercase.

## builtins.bytes.lstrip(self, bytes=None, /)

Strip leading bytes contained in the argument. If the argument is omitted or None, strip leading  ASCII whitespace.

## builtins.bytes.maketrans(frm, to, /)

Convert a function to be a static method. A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

class C:
         @staticmethod
         def f(arg1, arg2, argN):
             ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.

## builtins.bytes.partition(self, sep, /)

Partition the bytes into three parts using the given separator. This will search for the separator sep in the bytes.  If the
separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the
original bytes object and two empty bytes objects.

## builtins.bytes.removeprefix(self, prefix, /)

Return a bytes object with the given prefix string removed if present. If the bytes starts with the prefix string, return
bytes[len(prefix):].  Otherwise, return a copy of the original
bytes.

## builtins.bytes.removesuffix(self, suffix, /)

Return a bytes object with the given suffix string removed if present. If the bytes ends with the suffix string and that suffix is not
empty, return bytes[:-len(prefix)].  Otherwise, return a copy of the
original bytes.

## builtins.bytes.replace(self, old, new, count=-1, /)

Return a copy with all occurrences of substring old replaced by new. count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

## builtins.bytes.rfind(...)

Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Return -1 on failure.

## builtins.bytes.rindex(...)

Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end]. start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.

## builtins.bytes.rjust(self, width, fillchar=b' ', /)

Return a right-justified string of length width. Padding is done using the specified fill character.

## builtins.bytes.rpartition(self, sep, /)

Partition the bytes into three parts using the given separator. This will search for the separator sep in the bytes, starting at the
end.  If the separator is found, returns a 3-tuple containing the
part before the separator, the separator itself, and the part after
it.

If the separator is not found, returns a 3-tuple containing two
empty bytes objects and the original bytes object.

## builtins.bytes.rsplit(self, /, sep=None, maxsplit=-1)

Return a list of the sections in the bytes, using sep as the delimiter. sep
    The delimiter according which to split the bytes.
    None (the default value) means split on ASCII whitespace
    characters (space, tab, return, newline, formfeed, vertical tab).
  maxsplit
    Maximum number of splits to do.
    -1 (the default value) means no limit.

Splitting is done starting at the end of the bytes and working to
the front.

## builtins.bytes.rstrip(self, bytes=None, /)

Strip trailing bytes contained in the argument. If the argument is omitted or None, strip trailing ASCII whitespace.

## builtins.bytes.split(self, /, sep=None, maxsplit=-1)

Return a list of the sections in the bytes, using sep as the delimiter. sep
  The delimiter according which to split the bytes.
  None (the default value) means split on ASCII whitespace
  characters (space, tab, return, newline, formfeed, vertical tab).
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.

## builtins.bytes.splitlines(self, /, keepends=False)

Return a list of the lines in the bytes, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends
is given and true.

## builtins.bytes.startswith(...)

prefix
  A bytes or a tuple of bytes to try.
start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.

## builtins.bytes.strip(self, bytes=None, /)

Strip leading and trailing bytes contained in the argument. If the argument is omitted or None, strip leading and trailing ASCII
whitespace.

## builtins.bytes.swapcase(self, /)

Return a copy of B with uppercase ASCII characters converted to lowercase ASCII and vice versa.

## builtins.bytes.title(self, /)

Return a titlecased version of B, i.e. ASCII words start with uppercase characters, all remaining cased characters have lowercase.

## builtins.bytes.translate(self, table, /, delete=b'')

Return a copy with each character mapped by the given translation table. table
    Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are
removed.  The remaining characters are mapped through the given
translation table.

## builtins.bytes.upper(self, /)

Return a copy of B with all ASCII characters converted to uppercase.

## builtins.bytes.zfill(self, width, /)

Pad a numeric string with zeros on the left, to fill a field of the given width. The original string is never truncated.

## builtins.callable(obj, /)

Return whether the object is callable (i.e., some kind of function). Note that classes are callable, as are instances of classes with a
__call__() method.

## builtins.chr(i, /)

Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

## builtins.classmethod(function, /)

A class method receives the class as implicit first argument,
just like an instance method receives the instance.
To declare a class method, use this idiom:

class C:
      @classmethod
      def f(cls, arg1, arg2, argN):
          ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()).  The instance is ignored except for its class.
If a class method is called for a derived class, the derived class
object is passed as the implied first argument.

Class methods are different than C++ or Java static methods.
If you want those, see the staticmethod builtin.

## builtins.compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, *, _feature_version=-1)

The source code may represent a Python module, statement or
expression.
The filename will be used for run-time error messages.
The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.
The flags argument, if present, controls which future statements
influence the compilation of the code.
The dont_inherit argument, if true, stops the compilation inheriting
the effects of any future statements in effect in the code calling
compile; if absent or false these statements do influence the
compilation, in addition to any features explicitly specified.

## builtins.complex(real=0, imag=0)

If a string is given, parse it as a complex number.
If a single number is given, convert it to a complex number.
If the 'real' or 'imag' arguments are given, create a complex number
with the specified real and imaginary components.

## builtins.complex.conjugate(self, /)

Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.

## builtins.delattr(obj, name, /)

Deletes the named attribute from the given object. delattr(x, 'y') is equivalent to ``del x.y``

## builtins.dict(...)

dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)

## builtins.dict.clear(self, /)

Remove all items from the dict.

## builtins.dict.copy(self, /)

Return a shallow copy of the dict.

## builtins.dict.fromkeys(type, iterable, value=None, /)

Create a new dictionary with keys from iterable and values set to value.

## builtins.dict.get(self, key, default=None, /)

Return the value for key if key is in the dictionary, else default.

## builtins.dict.items(self, /)

Return a set-like object providing a view on the dict's items.

## builtins.dict.keys(self, /)

Return a set-like object providing a view on the dict's keys.

## builtins.dict.pop(...)

If the key is not found, return the default if given; otherwise, raise a KeyError.

## builtins.dict.popitem(self, /)

Remove and return a (key, value) pair as a 2-tuple. Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.

## builtins.dict.setdefault(self, key, default=None, /)

Insert key with a value of default if key is not in the dictionary. Return the value for key if key is in the dictionary, else default.

## builtins.dict.update(...)

D.update([E, ]**F) -> None. Update D from mapping/iterable E and F. If E is present and has a .keys() method, then does: for k in E.keys(): D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

## builtins.dict.values(self, /)

Return an object providing a view on the dict's values.

## builtins.dir(...)

Else, return an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it. If the object supplies a method named __dir__, it will be used; otherwise the default dir() logic is used and returns: for a module object: the module's attributes. for a class object: its attributes, and recursively the attributes of its bases. for any other object: its attributes, its class's attributes, and recursively the attributes of its class's base classes.

## builtins.divmod(x, y, /)

Return the tuple (x//y, x%y). Invariant: div*y + mod == x.

## builtins.enumerate(iterable, start=0)

Return an enumerate object. iterable
    an object supporting iteration

The enumerate object yields pairs containing a count (from start, which
defaults to zero) and a value yielded by the iterable argument.

enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

## builtins.eval(source, /, globals=None, locals=None)

The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.

## builtins.exec(source, /, globals=None, locals=None, *, closure=None)

The source may be a string representing one or more Python statements
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.
The closure must be a tuple of cellvars, and can only be used
when source is a code object requiring exactly that many cellvars.

## builtins.filter(function, iterable, /)

Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

## builtins.float(x=0, /)

Convert a string or number to a floating-point number, if possible.

## builtins.float.as_integer_ratio(self, /)

The ratio is in lowest terms and has a positive denominator.  Raise
OverflowError on infinities and a ValueError on NaNs.

>>> (10.0).as_integer_ratio()
(10, 1)
>>> (0.0).as_integer_ratio()
(0, 1)
>>> (-.25).as_integer_ratio()
(-1, 4)

## builtins.float.conjugate(self, /)

Return self, the complex conjugate of any float.

## builtins.float.fromhex(type, string, /)

Create a floating-point number from a hexadecimal string. >>> float.fromhex('0x1.ffffp10')
2047.984375
>>> float.fromhex('-0x1p-1074')
-5e-324

## builtins.float.hex(self, /)

Return a hexadecimal representation of a floating-point number. >>> (-0.1).hex()
'-0x1.999999999999ap-4'
>>> 3.14159.hex()
'0x1.921f9f01b866ep+1'

## builtins.float.is_integer(self, /)

Return True if the float is an integer.

## builtins.format(value, format_spec='', /)

Return type(value).__format__(value, format_spec) Many built-in types implement format_spec according to the
Format Specification Mini-language. See help('FORMATTING').

If type(value) does not supply a method named __format__
and format_spec is empty, then str(value) is returned.
See also help('SPECIALMETHODS').

## builtins.frozenset(iterable=(), /)

Build an immutable unordered collection of unique elements.

## builtins.frozenset.copy(self, /)

Return a shallow copy of a set.

## builtins.frozenset.difference(self, /, *others)

Return a new set with elements in the set that are not in the others.

## builtins.frozenset.intersection(self, /, *others)

Return a new set with elements common to the set and all others.

## builtins.frozenset.isdisjoint(self, other, /)

Return True if two sets have a null intersection.

## builtins.frozenset.issubset(self, other, /)

Report whether another set contains this set.

## builtins.frozenset.issuperset(self, other, /)

Report whether this set contains another set.

## builtins.frozenset.symmetric_difference(self, other, /)

Return a new set with elements in either the set or other but not both.

## builtins.frozenset.union(self, /, *others)

Return a new set with elements from the set and all others.

## builtins.getattr(...)

getattr(x, 'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute
doesn't exist; without it, an exception is raised in that case.

## builtins.globals()

Return the dictionary containing the current scope's global variables. NOTE: Updates to this dictionary *will* affect name lookups in the
current global scope and vice-versa.

## builtins.hasattr(obj, name, /)

Return whether the object has an attribute with the given name. This is done by calling getattr(obj, name) and catching AttributeError.

## builtins.hash(obj, /)

Return the hash value for the given object. Two objects that compare equal must also have the same hash value, but the
reverse is not necessarily true.

## builtins.hex(number, /)

Return the hexadecimal representation of an integer. >>> hex(12648430)
'0xc0ffee'

## builtins.id(obj, /)

Return the identity of an object. This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)

## builtins.input(prompt='', /)

The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise
EOFError.
On *nix systems, readline is used if available.

## builtins.int(...)

If x is a number, return x.__int__(). For floating-point numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4

## builtins.int.as_integer_ratio(self, /)

Return a pair of integers, whose ratio is equal to the original int. The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

## builtins.int.bit_count(self, /)

Number of ones in the binary representation of the absolute value of self. Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

## builtins.int.bit_length(self, /)

Number of bits necessary to represent self in binary. >>> bin(37)
'0b100101'
>>> (37).bit_length()
6

## builtins.int.conjugate(self, /)

Returns self, the complex conjugate of any int.

## builtins.int.from_bytes(type, /, bytes, byteorder='big', *, signed=False)

bytes
  Holds the array of bytes to convert.  The argument must either
  support the buffer protocol or be an iterable object producing
  bytes.  Bytes and bytearray are examples of built-in objects that
  support the buffer protocol.
byteorder
  The byte order used to represent the integer.  If byteorder is
  'big', the most significant byte is at the beginning of the byte
  array.  If byteorder is 'little', the most significant byte is at
  the end of the byte array.  To request the native byte order of
  the host system, use sys.byteorder as the byte order value.
  Default is to use 'big'.
signed
  Indicates whether two's complement is used to represent the
  integer.

## builtins.int.is_integer(self, /)

Returns True. Exists for duck type compatibility with float.is_integer.

## builtins.int.to_bytes(self, /, length=1, byteorder='big', *, signed=False)

length
  Length of bytes object to use.  An OverflowError is raised if
  the integer is not representable with the given number of bytes.
  Default is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is
  'big', the most significant byte is at the beginning of the byte
  array.  If byteorder is 'little', the most significant byte is at
  the end of the byte array.  To request the native byte order of
  the host system, use sys.byteorder as the byte order value.
  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the
  integer.  If signed is False and a negative integer is given,
  an OverflowError is raised.

## builtins.isinstance(obj, class_or_tuple, /)

A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the
target to check against.  This is equivalent to ``isinstance(x, A) or
isinstance(x, B) or ...`` etc.

## builtins.issubclass(cls, class_or_tuple, /)

A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the
target to check against.  This is equivalent to ``issubclass(x, A) or
issubclass(x, B) or ...``.

## builtins.iter(...)

In the first form, the argument must supply its own iterator, or be a sequence. In the second form, the callable is called until it returns the sentinel.

## builtins.len(obj, /)

Return the number of items in a container.

## builtins.list(iterable=(), /)

Built-in mutable sequence. If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.

## builtins.list.append(self, object, /)

Append object to the end of the list.

## builtins.list.clear(self, /)

Remove all items from list.

## builtins.list.copy(self, /)

Return a shallow copy of the list.

## builtins.list.count(self, value, /)

Return number of occurrences of value.

## builtins.list.extend(self, iterable, /)

Extend list by appending elements from the iterable.

## builtins.list.index(self, value, start=0, stop=9223372036854775807, /)

Return first index of value. Raises ValueError if the value is not present.

## builtins.list.insert(self, index, object, /)

Insert object before index.

## builtins.list.pop(self, index=-1, /)

Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

## builtins.list.remove(self, value, /)

Remove first occurrence of value. Raises ValueError if the value is not present.

## builtins.list.reverse(self, /)

Reverse *IN PLACE*.

## builtins.list.sort(self, /, *, key=None, reverse=False)

The sort is in-place (i.e. the list itself is modified) and stable
(i.e. the order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort
them, ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

## builtins.locals()

NOTE: Whether or not updates to this dictionary will affect name
lookups in the local scope and vice-versa is *implementation
dependent* and not covered by any backwards compatibility
guarantees.

## builtins.map(function, iterable, /, *iterables)

Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

## builtins.max(...)

The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more positional arguments, return the largest argument.

## builtins.memoryview(object)

Create a new memoryview object which references the given object.

## builtins.memoryview.cast(...)

Cast a memoryview to a new format or shape.

## builtins.memoryview.hex(...)

sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from
    the right, negative values count from the left.

Example:
>>> value = memoryview(b'\xb9\x01\xef')
>>> value.hex()
'b901ef'
>>> value.hex(':')
'b9:01:ef'
>>> value.hex(':', 2)
'b9:01ef'
>>> value.hex(':', -2)
'b901:ef'

## builtins.memoryview.release(self, /)

Release the underlying buffer exposed by the memoryview object.

## builtins.memoryview.tobytes(self, /, order='C')

Order can be {'C', 'F', 'A'}.  When order is 'C' or 'F', the data of
the original array is converted to C or Fortran order.  For
contiguous views, 'A' returns an exact copy of the physical memory.
In particular, in-memory Fortran order is preserved.  For
non-contiguous views, the data is converted to C first.  order=None
is the same as order='C'.

## builtins.memoryview.tolist(self, /)

Return the data in the buffer as a list of elements.

## builtins.memoryview.toreadonly(self, /)

Return a readonly version of the memoryview.

## builtins.min(...)

The default keyword-only argument specifies an object to return if the provided iterable is empty. With two or more positional arguments, return the smallest argument.

## builtins.next(...)

Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

## builtins.object()

The base class of the class hierarchy. When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.

## builtins.oct(number, /)

Return the octal representation of an integer. >>> oct(342391)
'0o1234567'

## builtins.ord(character, /)

If the argument is a one-character string, return the Unicode code
point of that character.

If the argument is a bytes or bytearray object of length 1, return its
single byte value.

## builtins.pow(base, exp, mod=None)

Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments Some types, such as ints, are able to use a more efficient algorithm
when invoked using the three argument form.

## builtins.print(*args, sep=' ', end='\n', file=None, flush=False)

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.

## builtins.property(fget=None, fset=None, fdel=None, doc=None)

Property attribute. fget
    function to be used for getting an attribute value
  fset
    function to be used for setting an attribute value
  fdel
    function to be used for del'ing an attribute
  doc
    docstring

Typical use is to define a managed attribute x:

class C(object):
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

Decorators make defining new properties or modifying existing ones easy:

class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

## builtins.property.deleter(self, object, /)

Descriptor to obtain a copy of the property with a different deleter.

## builtins.property.getter(self, object, /)

Descriptor to obtain a copy of the property with a different getter.

## builtins.property.setter(self, object, /)

Descriptor to obtain a copy of the property with a different setter.

## builtins.range(...)

Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

## builtins.range.count(self, object, /)

rangeobject.count(value) -> integer -- return number of occurrences of value

## builtins.range.index(self, object, /)

rangeobject.index(value) -> integer -- return index of value. Raise ValueError if the value is not present.

## builtins.repr(obj, /)

Return the canonical string representation of the object. For many object types, including most builtins, eval(repr(obj)) == obj.

## builtins.reversed(sequence, /)

Return a reverse iterator over the values of the given sequence.

## builtins.round(number, ndigits=None)

The return value is an integer if ndigits is omitted or None.
Otherwise the return value has the same type as the number.  ndigits
may be negative.

## builtins.set(iterable=(), /)

Build an unordered collection of unique elements.

## builtins.set.add(self, object, /)

Add an element to a set. This has no effect if the element is already present.

## builtins.set.clear(self, /)

Remove all elements from this set.

## builtins.set.copy(self, /)

Return a shallow copy of a set.

## builtins.set.difference(self, /, *others)

Return a new set with elements in the set that are not in the others.

## builtins.set.difference_update(self, /, *others)

Update the set, removing elements found in others.

## builtins.set.discard(self, object, /)

Remove an element from a set if it is a member. Unlike set.remove(), the discard() method does not raise
an exception when an element is missing from the set.

## builtins.set.intersection(self, /, *others)

Return a new set with elements common to the set and all others.

## builtins.set.intersection_update(self, /, *others)

Update the set, keeping only elements found in it and all others.

## builtins.set.isdisjoint(self, other, /)

Return True if two sets have a null intersection.

## builtins.set.issubset(self, other, /)

Report whether another set contains this set.

## builtins.set.issuperset(self, other, /)

Report whether this set contains another set.

## builtins.set.pop(self, /)

Remove and return an arbitrary set element. Raises KeyError if the set is empty.

## builtins.set.remove(self, object, /)

Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.

## builtins.set.symmetric_difference(self, other, /)

Return a new set with elements in either the set or other but not both.

## builtins.set.symmetric_difference_update(self, other, /)

Update the set, keeping only elements found in either set, but not in both.

## builtins.set.union(self, /, *others)

Return a new set with elements from the set and all others.

## builtins.set.update(self, /, *others)

Update the set, adding elements from all others.

## builtins.setattr(obj, name, value, /)

Sets the named attribute on the given object to the specified value. setattr(x, 'y', v) is equivalent to ``x.y = v``

## builtins.slice(...)

Create a slice object. This is used for extended slicing (e.g. a[0:10:2]).

## builtins.slice.indices(self, object, /)

Assuming a sequence of length len, calculate the start and stop indices, and the stride length of the extended slice described by S. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.

## builtins.sorted(iterable, /, *, key=None, reverse=False)

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.

## builtins.staticmethod(function, /)

Convert a function to be a static method. A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

class C:
         @staticmethod
         def f(arg1, arg2, argN):
             ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.

## builtins.str(...)

If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to 'utf-8'. errors defaults to 'strict'.

## builtins.str.capitalize(self, /)

Return a capitalized version of the string. More specifically, make the first character have upper case and the
rest lower case.

## builtins.str.casefold(self, /)

Return a version of the string suitable for caseless comparisons.

## builtins.str.center(self, width, fillchar=' ', /)

Return a centered string of length width. Padding is done using the specified fill character (default is
a space).

## builtins.str.count(...)

Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice
notation.

## builtins.str.encode(self, /, encoding='utf-8', errors='strict')

encoding
  The encoding in which to encode the string.
errors
  The error handling scheme to use for encoding errors.
  The default is 'strict' meaning that encoding errors raise a
  UnicodeEncodeError.  Other possible values are 'ignore', 'replace'
  and 'xmlcharrefreplace' as well as any other name registered with
  codecs.register_error that can handle UnicodeEncodeErrors.

## builtins.str.endswith(...)

suffix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.

## builtins.str.expandtabs(self, /, tabsize=8)

Return a copy where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

## builtins.str.find(...)

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice
notation.  Return -1 on failure.

## builtins.str.format(self, /, *args, **kwargs)

Return a formatted version of the string, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

## builtins.str.format_map(self, mapping, /)

Return a formatted version of the string, using substitutions from mapping. The substitutions are identified by braces ('{' and '}').

## builtins.str.index(...)

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice
notation.  Raises ValueError when the substring is not found.

## builtins.str.isalnum(self, /)

Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are
alpha-numeric and there is at least one character in the string.

## builtins.str.isalpha(self, /)

Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are
alphabetic and there is at least one character in the string.

## builtins.str.isascii(self, /)

Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

## builtins.str.isdecimal(self, /)

Return True if the string is a decimal string, False otherwise. A string is a decimal string if all characters in the string are
decimal and there is at least one character in the string.

## builtins.str.isdigit(self, /)

Return True if the string is a digit string, False otherwise. A string is a digit string if all characters in the string are
digits and there is at least one character in the string.

## builtins.str.isidentifier(self, /)

Return True if the string is a valid Python identifier, False otherwise. Call keyword.iskeyword(s) to test whether string s is a reserved
identifier, such as "def" or "class".

## builtins.str.islower(self, /)

Return True if the string is a lowercase string, False otherwise. A string is lowercase if all cased characters in the string are
lowercase and there is at least one cased character in the string.

## builtins.str.isnumeric(self, /)

Return True if the string is a numeric string, False otherwise. A string is numeric if all characters in the string are numeric and
there is at least one character in the string.

## builtins.str.isprintable(self, /)

Return True if all characters in the string are printable, False otherwise. A character is printable if repr() may use it in its output.

## builtins.str.isspace(self, /)

Return True if the string is a whitespace string, False otherwise. A string is whitespace if all characters in the string are
whitespace and there is at least one character in the string.

## builtins.str.istitle(self, /)

Return True if the string is a title-cased string, False otherwise. In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

## builtins.str.isupper(self, /)

Return True if the string is an uppercase string, False otherwise. A string is uppercase if all cased characters in the string are
uppercase and there is at least one cased character in the string.

## builtins.str.join(self, iterable, /)

Concatenate any number of strings. The string whose method is called is inserted in between each given
string.  The result is returned as a new string.

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

## builtins.str.ljust(self, width, fillchar=' ', /)

Return a left-justified string of length width. Padding is done using the specified fill character (default is
a space).

## builtins.str.lower(self, /)

Return a copy of the string converted to lowercase.

## builtins.str.lstrip(self, chars=None, /)

Return a copy of the string with leading whitespace removed. If chars is given and not None, remove characters in chars instead.

## builtins.str.maketrans(...)

Convert a function to be a static method. A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

class C:
         @staticmethod
         def f(arg1, arg2, argN):
             ...

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.

## builtins.str.partition(self, sep, /)

Partition the string into three parts using the given separator. This will search for the separator in the string.  If the separator
is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing
the original string and two empty strings.

## builtins.str.removeprefix(self, prefix, /)

Return a str with the given prefix string removed if present. If the string starts with the prefix string, return
string[len(prefix):].  Otherwise, return a copy of the original
string.

## builtins.str.removesuffix(self, suffix, /)

Return a str with the given suffix string removed if present. If the string ends with the suffix string and that suffix is not
empty, return string[:-len(suffix)].  Otherwise, return a copy of
the original string.

## builtins.str.replace(self, old, new, /, count=-1)

Return a copy with all occurrences of substring old replaced by new. count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

## builtins.str.rfind(...)

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice
notation.  Return -1 on failure.

## builtins.str.rindex(...)

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice
notation.  Raises ValueError when the substring is not found.

## builtins.str.rjust(self, width, fillchar=' ', /)

Return a right-justified string of length width. Padding is done using the specified fill character (default is
a space).

## builtins.str.rpartition(self, sep, /)

Partition the string into three parts using the given separator. This will search for the separator in the string, starting at the
end.  If the separator is found, returns a 3-tuple containing the
part before the separator, the separator itself, and the part after
it.

If the separator is not found, returns a 3-tuple containing two
empty strings and the original string.

## builtins.str.rsplit(self, /, sep=None, maxsplit=-1)

Return a list of the substrings in the string, using sep as the separator string. sep
    The separator used to split the string.

When set to None (the default value), will split on any
    whitespace character (including \n \r \t \f and spaces) and
    will discard empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

## builtins.str.rstrip(self, chars=None, /)

Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

## builtins.str.split(self, /, sep=None, maxsplit=-1)

Return a list of the substrings in the string, using sep as the separator string. sep
    The separator used to split the string.

When set to None (the default value), will split on any
    whitespace character (including \n \r \t \f and spaces) and
    will discard empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been
intentionally delimited.  With natural text that includes
punctuation, consider using the regular expression module.

## builtins.str.splitlines(self, /, keepends=False)

Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends
is given and true.

## builtins.str.startswith(...)

prefix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.

## builtins.str.strip(self, chars=None, /)

Return a copy of the string with leading and trailing whitespace removed. If chars is given and not None, remove characters in chars instead.

## builtins.str.swapcase(self, /)

Convert uppercase characters to lowercase and lowercase characters to uppercase.

## builtins.str.title(self, /)

Return a version of the string where each word is titlecased. More specifically, words start with uppercased characters and all
remaining cased characters have lower case.

## builtins.str.translate(self, table, /)

table
    Translation table, which must be a mapping of Unicode ordinals
    to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for
instance a dictionary or list.  If this operation raises
LookupError, the character is left untouched.  Characters mapped to
None are deleted.

## builtins.str.upper(self, /)

Return a copy of the string converted to uppercase.

## builtins.str.zfill(self, width, /)

Pad a numeric string with zeros on the left, to fill a field of the given width. The string is never truncated.

## builtins.sum(iterable, /, start=0)

Return the sum of a 'start' value (default: 0) plus an iterable of numbers When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and
may reject non-numeric types.

## builtins.super(...)

super() -> same as super(__class__, <first argument>) super(type) -> unbound super object super(type, obj) -> bound super object; requires isinstance(obj, type) super(type, type2) -> bound super object; requires issubclass(type2, type) Typical use to call a cooperative superclass method: class C(B): def meth(self, arg): super().meth(arg) This works for class methods too: class C(B): @classmethod def cmeth(cls, arg): super().cmeth(arg)

## builtins.tuple(iterable=(), /)

Built-in immutable sequence. If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.

## builtins.tuple.count(self, value, /)

Return number of occurrences of value.

## builtins.tuple.index(self, value, start=0, stop=9223372036854775807, /)

Return first index of value. Raises ValueError if the value is not present.

## builtins.type(...)

type(object) -> the object's type type(name, bases, dict, **kwds) -> a new type

## builtins.type.mro(self, /)

Return a type's method resolution order.

## builtins.vars(...)

Without arguments, equivalent to locals(). With an argument, equivalent to object.__dict__.

## builtins.zip(*iterables, strict=False)

The i-th element in every tuple comes from the i-th iterable argument to zip(). This continues until the shortest argument is exhausted.

If strict is true and one of the arguments is exhausted before the
others, raise a ValueError.

>>> list(zip('abcdefg', range(3), range(4)))
   [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
