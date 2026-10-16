# binascii

## binascii.a2b_base64(data, /, *, strict_mode=False)

strict_mode
  When set to True, bytes that are not part of the base64 standard are not allowed.
  The same applies to excess data after padding (= / ==).

## binascii.a2b_hex(hexstr, /)

Binary data of hexadecimal representation. hexstr must contain an even number of hex digits (upper or lower case).
This function is also available as "unhexlify()".

## binascii.a2b_qp(data, header=False)

Decode a string of qp-encoded data.

## binascii.a2b_uu(data, /)

Decode a line of uuencoded data.

## binascii.b2a_base64(data, /, *, newline=True)

Base64-code line of data.

## binascii.b2a_hex(...)

Hexadecimal representation of binary data. sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from the
    right, negative values count from the left.

The return value is a bytes object.  This function is also
available as "hexlify()".

Example:
>>> binascii.b2a_hex(b'\xb9\x01\xef')
b'b901ef'
>>> binascii.hexlify(b'\xb9\x01\xef', ':')
b'b9:01:ef'
>>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
b'b9_01ef'

## binascii.b2a_qp(data, quotetabs=False, istext=True, header=False)

On encoding, when istext is set, newlines are not encoded, and white
space at end of lines is.  When istext is not set, \r and \n (CR/LF)
are both encoded.  When quotetabs is set, space and tabs are encoded.

## binascii.b2a_uu(data, /, *, backtick=False)

Uuencode line of data.

## binascii.crc32(data, crc=0, /)

Compute CRC-32 incrementally.

## binascii.crc_hqx(data, crc, /)

Compute CRC-CCITT incrementally.

## binascii.hexlify(...)

Hexadecimal representation of binary data. sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from the
    right, negative values count from the left.

The return value is a bytes object.  This function is also
available as "b2a_hex()".

## binascii.unhexlify(hexstr, /)

Binary data of hexadecimal representation. hexstr must contain an even number of hex digits (upper or lower case).
