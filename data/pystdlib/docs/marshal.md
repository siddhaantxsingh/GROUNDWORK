# marshal

## marshal.dump(value, file, version=4, /, *, allow_code=True)

value
    Must be a supported type.
  file
    Must be a writeable binary file.
  version
    Indicates the data format that dump should use.
  allow_code
    Allow to write code objects.

If the value has (or contains an object that has) an unsupported type, a
ValueError exception is raised - but garbage data will also be written
to the file. The object will not be properly read back by load().

## marshal.dumps(value, version=4, /, *, allow_code=True)

value
    Must be a supported type.
  version
    Indicates the data format that dumps should use.
  allow_code
    Allow to write code objects.

Raise a ValueError exception if value has (or contains an object that
has) an unsupported type.

## marshal.load(file, /, *, allow_code=True)

file
    Must be readable binary file.
  allow_code
    Allow to load code objects.

If no valid value is read (e.g. because the data has a different Python
version's incompatible marshal format), raise EOFError, ValueError or
TypeError.

Note: If an object containing an unsupported type was marshalled with
dump(), load() will substitute None for the unmarshallable type.

## marshal.loads(bytes, /, *, allow_code=True)

Convert the bytes-like object to a value. allow_code
    Allow to load code objects.

If no valid value is found, raise EOFError, ValueError or TypeError.
Extra bytes in the input are ignored.
