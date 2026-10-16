# mimetypes

## mimetypes.MimeTypes(filenames=(), strict=True)

MIME-types datastore. This datastore can handle information from mime.types-style files
and supports basic determination of MIME type from a filename or
URL, and can guess a reasonable extension given a MIME type.

## mimetypes.MimeTypes.add_type(self, type, ext, strict=True)

Add a mapping between a type and an extension. When the extension is already known, the new
type will replace the old one. When the type
is already known the extension will be added
to the list of known extensions.

If strict is true, information will be added to
list of standard types, else to the list of non-standard
types.

## mimetypes.MimeTypes.guess_all_extensions(self, type, strict=True)

Guess the extensions for a file based on its MIME type. Return value is a list of strings giving the possible filename
extensions, including the leading dot ('.').  The extension is not
guaranteed to have been associated with any particular data stream,
but would be mapped to the MIME type `type' by guess_type().

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

## mimetypes.MimeTypes.guess_extension(self, type, strict=True)

Guess the extension for a file based on its MIME type. Return value is a string giving a filename extension,
including the leading dot ('.').  The extension is not
guaranteed to have been associated with any particular data
stream, but would be mapped to the MIME type `type' by
guess_type().  If no extension can be guessed for `type', None
is returned.

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

## mimetypes.MimeTypes.guess_file_type(self, path, *, strict=True)

Guess the type of a file based on its path. Similar to guess_type(), but takes file path istead of URL.

## mimetypes.MimeTypes.guess_type(self, url, strict=True)

Return value is a tuple (type, encoding) where type is None if
the type can't be guessed (no or unknown suffix) or a string
of the form type/subtype, usable for a MIME Content-type
header; and encoding is None for no encoding or the name of
the program used to encode (e.g. compress or gzip).  The
mappings are table driven.  Encoding suffixes are case
sensitive; type suffixes are first tried case sensitive, then
case insensitive.

The suffixes .tgz, .taz and .tz (case sensitive!) are all
mapped to '.tar.gz'.  (This is table-driven too, using the
dictionary suffix_map.)

Optional `strict' argument when False adds a bunch of commonly found,
but non-standard types.

## mimetypes.MimeTypes.read(self, filename, strict=True)

Read a single mime.types-format file, specified by pathname. If strict is true, information will be added to
list of standard types, else to the list of non-standard
types.

## mimetypes.MimeTypes.read_windows_registry(self, strict=True)

Load the MIME types database from Windows registry. If strict is true, information will be added to
list of standard types, else to the list of non-standard
types.

## mimetypes.MimeTypes.readfp(self, fp, strict=True)

Read a single mime.types-format file. If strict is true, information will be added to
list of standard types, else to the list of non-standard
types.

## mimetypes.add_type(type, ext, strict=True)

Add a mapping between a type and an extension. When the extension is already known, the new
type will replace the old one. When the type
is already known the extension will be added
to the list of known extensions.

If strict is true, information will be added to
list of standard types, else to the list of non-standard
types.

## mimetypes.guess_all_extensions(type, strict=True)

Guess the extensions for a file based on its MIME type. Return value is a list of strings giving the possible filename
extensions, including the leading dot ('.').  The extension is not
guaranteed to have been associated with any particular data
stream, but would be mapped to the MIME type `type' by
guess_type().  If no extension can be guessed for `type', None
is returned.

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

## mimetypes.guess_extension(type, strict=True)

Guess the extension for a file based on its MIME type. Return value is a string giving a filename extension, including the
leading dot ('.').  The extension is not guaranteed to have been
associated with any particular data stream, but would be mapped to the
MIME type `type' by guess_type().  If no extension can be guessed for
`type', None is returned.

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

## mimetypes.guess_file_type(path, *, strict=True)

Guess the type of a file based on its path. Similar to guess_type(), but takes file path istead of URL.

## mimetypes.guess_type(url, strict=True)

Return value is a tuple (type, encoding) where type is None if the
type can't be guessed (no or unknown suffix) or a string of the
form type/subtype, usable for a MIME Content-type header; and
encoding is None for no encoding or the name of the program used
to encode (e.g. compress or gzip).  The mappings are table
driven.  Encoding suffixes are case sensitive; type suffixes are
first tried case sensitive, then case insensitive.

The suffixes .tgz, .taz and .tz (case sensitive!) are all mapped
to ".tar.gz".  (This is table-driven too, using the dictionary
suffix_map).

Optional `strict' argument when false adds a bunch of commonly found, but
non-standard types.
