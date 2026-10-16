# pickle

## pickle.PickleBuffer(...)

Wrapper for potentially out-of-band buffers

## pickle.PickleBuffer.raw(self, /)

Return a memoryview of the raw memory underlying this buffer. Will raise BufferError is the buffer isn't contiguous.

## pickle.PickleBuffer.release(self, /)

Release the underlying buffer exposed by the PickleBuffer object.

## pickle.decode_long(data)

Decode a long from a two's complement little-endian binary string. >>> decode_long(b'')
0
>>> decode_long(b"\xff\x00")
255
>>> decode_long(b"\xff\x7f")
32767
>>> decode_long(b"\x00\xff")
-256
>>> decode_long(b"\x00\x80")
-32768
>>> decode_long(b"\x80")
-128
>>> decode_long(b"\x7f")
127

## pickle.encode_long(x)

Note that 0 is a special case, returning an empty string, to save a byte in the LONG1 pickling context.

>>> encode_long(0)
b''
>>> encode_long(255)
b'\xff\x00'
>>> encode_long(32767)
b'\xff\x7f'
>>> encode_long(-256)
b'\x00\xff'
>>> encode_long(-32768)
b'\x00\x80'
>>> encode_long(-128)
b'\x80'
>>> encode_long(127)
b'\x7f'
>>>

## pickle.whichmodule(obj, name)

Find the module an object belong to.
