# tokenize

## tokenize.Untokenizer.add_backslash_continuation(self, start)

Add backslash continuation characters if the row has increased without encountering a newline token. This also inserts the correct amount of whitespace before the backslash.

## tokenize.detect_encoding(readline)

It requires one argument, readline, in the same way as the tokenize() generator.

It will call readline a maximum of twice, and return the encoding used
(as a string) and a list of any lines (left as bytes) it has read in.

It detects the encoding from the presence of a utf-8 bom or an encoding
cookie as specified in pep-0263.  If both a bom and a cookie are present,
but disagree, a SyntaxError will be raised.  If the encoding cookie is an
invalid charset, raise a SyntaxError.  Note that if a utf-8 bom is found,
'utf-8-sig' is returned.

If no encoding is specified, then the default of 'utf-8' will be returned.

## tokenize.generate_tokens(readline)

Tokenize a source reading Python code as unicode strings. This has the same API as tokenize(), except that it expects the *readline*
callable to return str objects instead of bytes.

## tokenize.open(filename)

Open a file in read only mode using the encoding detected by detect_encoding().

## tokenize.tokenize(readline)

Each call to the function should return one line of input as bytes. Alternatively, readline can be a callable function terminating with StopIteration: readline = open(myfile, 'rb').__next__ # Example of alternate readline

The generator produces 5-tuples with these members: the token type; the
token string; a 2-tuple (srow, scol) of ints specifying the row and
column where the token begins in the source; a 2-tuple (erow, ecol) of
ints specifying the row and column where the token ends in the source;
and the line on which the token was found.  The line passed is the
physical line.

The first token sequence will always be an ENCODING token
which tells you which encoding was used to decode the bytes stream.

## tokenize.untokenize(iterable)

It returns a bytes object, encoded using the ENCODING token, which is the first token sequence output by tokenize.

Each element returned by the iterable must be a token sequence
with at least two elements, a token number and token value.  If
only two tokens are passed, the resulting output is poor.

The result is guaranteed to tokenize back to match the input so
that the conversion is lossless and round-trips are assured.
The guarantee applies only to the token type and token string as
the spacing between tokens (column positions) may change.
