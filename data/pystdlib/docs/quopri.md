# quopri

## quopri.decode(input, output, header=False)

Read 'input', apply quoted-printable decoding, and write to 'output'. 'input' and 'output' are binary file objects. If 'header' is true, decode underscore as space (per RFC 1522).

## quopri.encode(input, output, quotetabs, header=False)

'input' and 'output' are binary file objects. The 'quotetabs' flag
indicates whether embedded tabs and spaces should be quoted. Note that
line-ending tabs and spaces are always encoded, as per RFC 1521.
The 'header' flag indicates whether we are encoding spaces as _ as per RFC
1522.

## quopri.ishex(c)

Return true if the byte ordinal 'c' is a hexadecimal digit in ASCII.

## quopri.needsquoting(c, quotetabs, header)

The 'quotetabs' flag indicates whether embedded tabs and spaces should be
quoted.  Note that line-ending tabs and spaces are always encoded, as per
RFC 1521.

## quopri.quote(c)

Quote a single character.

## quopri.unhex(s)

Get the integer value of a hexadecimal number.
