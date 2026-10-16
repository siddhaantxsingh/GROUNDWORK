# locale

## locale.atof(string, func=<class 'float'>)

Parses a string as a float according to the locale settings.

## locale.atoi(string)

Converts a string to an integer according to the locale settings.

## locale.currency(val, symbol=True, grouping=False, international=False)

Formats val according to the currency settings in the current locale.

## locale.delocalize(string)

Parses a string as a normalized number according to the locale settings.

## locale.format_string(f, val, grouping=False, monetary=False)

Formats a string in the same way that the % formatting would use, but takes the current locale into account. Grouping is applied if the third parameter is true.
Conversion uses monetary thousands separator and grouping strings if
forth parameter monetary is true.

## locale.getdefaultlocale(envvars=('LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE'))

According to POSIX, a program which has not called
setlocale(LC_ALL, "") runs using the portable 'C' locale.
Calling setlocale(LC_ALL, "") lets it use the default locale as
defined by the LANG variable. Since we don't want to interfere
with the current locale setting we thus emulate the behavior
in the way described above.

To maintain compatibility with other platforms, not only the
LANG variable is tested, but a list of variables given as
envvars parameter. The first found to be defined will be
used. envvars defaults to the search path used in GNU gettext;
it must always contain the variable name 'LANG'.

Except for the code 'C', the language code corresponds to RFC
1766.  code and encoding can be None in case the values cannot
be determined.

## locale.getlocale(category=0)

category may be one of the LC_* value except LC_ALL. It
defaults to LC_CTYPE.

Except for the code 'C', the language code corresponds to RFC
1766.  code and encoding can be None in case the values cannot
be determined.

## locale.getpreferredencoding(do_setlocale=True)

Return the charset that the user is likely using, according to the system configuration.

## locale.localize(string, grouping=False, monetary=False)

Parses a string as locale number according to the locale settings.

## locale.normalize(localename)

The returned locale code is formatted for use with
setlocale().

If normalization fails, the original name is returned
unchanged.

If the given encoding is not known, the function defaults to
the default encoding for the locale code just like setlocale()
does.

## locale.setlocale(category, locale=None)

The locale can be a string, an iterable of two strings (language code and encoding), or None.

Iterables are converted to strings using the locale aliasing
engine.  Locale strings are passed directly to the C lib.

category may be given as one of the LC_* values.

## locale.str(val)

Convert float to string, taking the locale into account.
