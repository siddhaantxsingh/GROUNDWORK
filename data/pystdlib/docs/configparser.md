# configparser

## configparser.BasicInterpolation()

The option values can contain format strings which refer to other values in
the same section, or values in the special default section.

For example:

something: %(dir)s/whatever

would resolve the "%(dir)s" to the value of dir.  All reference
expansions are done late, on demand. If a user needs to use a bare % in
a configuration file, she can escape it by writing %%. Other % usage
is considered a user error and raises `InterpolationSyntaxError`.

## configparser.ConfigParser(defaults=None, dict_type=<class 'dict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x7fc8a1920aa0>, converters=<object object at 0x7fc8a1920aa0>, allow_unnamed_section=False)

ConfigParser implementing interpolation.

## configparser.ConfigParser.add_section(self, section)

Create a new section in the configuration. Extends RawConfigParser.add_section by validating if the section name is a string.

## configparser.ConfigParser.set(self, section, option, value=None)

Set an option. Extends RawConfigParser.set by validating type and interpolation syntax on the value.

## configparser.ConverterMapping(parser)

If a parser class implements a getter directly, the value for the given
key will be ``None``. The presence of the converter name here enables
section proxies to find and use the implementation on the parser class.

## configparser.DuplicateOptionError(section, option, source=None, lineno=None)

Raised by strict parsers when an option is repeated in an input source. Current implementation raises this exception only when an option is found
more than once in a single file, string or dictionary.

## configparser.DuplicateSectionError(section, source=None, lineno=None)

Possible repetitions that raise this exception are: multiple creation
using the API or in strict parsers when a section is found more than once
in a single input file, string or dictionary.

## configparser.Error(msg='')

Base class for ConfigParser exceptions.

## configparser.ExtendedInterpolation()

Advanced variant of interpolation, supports the syntax used by `zc.buildout`. Enables interpolation between sections.

## configparser.Interpolation()

Dummy interpolation that passes the value through with no changes.

## configparser.InterpolationDepthError(option, section, rawval)

Raised when substitutions are nested too deeply.

## configparser.InterpolationError(option, section, msg)

Base class for interpolation-related exceptions.

## configparser.InterpolationMissingOptionError(option, section, rawval, reference)

A string substitution required a setting which was not available.

## configparser.InterpolationSyntaxError(option, section, msg)

Raised when the source text contains invalid syntax. Current implementation raises this exception when the source text into
which substitutions are made does not conform to the required syntax.

## configparser.MissingSectionHeaderError(filename, lineno, line)

Raised when a key-value pair is found before any section header.

## configparser.MultilineContinuationError(filename, lineno, line)

Raised when a key without value is followed by continuation line

## configparser.NoOptionError(option, section)

A requested option was not found.

## configparser.NoSectionError(section)

Raised when no section matches a requested option.

## configparser.ParsingError(source, *args)

Raised when a configuration file does not follow legal syntax.

## configparser.RawConfigParser(defaults=None, dict_type=<class 'dict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x7fc8a1920aa0>, converters=<object object at 0x7fc8a1920aa0>, allow_unnamed_section=False)

ConfigParser that does not do interpolation.

## configparser.RawConfigParser.add_section(self, section)

Create a new section in the configuration. Raise DuplicateSectionError if a section by the specified name
already exists. Raise ValueError if name is DEFAULT.

## configparser.RawConfigParser.get(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x7fc8a1920aa0>)

If `vars` is provided, it must be a dictionary. The option is looked up
in `vars` (if provided), `section`, and in `DEFAULTSECT` in that order.
If the key is not found and `fallback` is provided, it is used as
a fallback value. `None` can be provided as a `fallback` value.

If interpolation is enabled and the optional argument `raw` is False,
all interpolations are expanded in the return values.

Arguments `raw`, `vars`, and `fallback` are keyword only.

The section DEFAULT is special.

## configparser.RawConfigParser.has_option(self, section, option)

Check for the existence of a given option in a given section. If the specified `section` is None or an empty string, DEFAULT is assumed. If the specified `section` does not exist, returns False.

## configparser.RawConfigParser.has_section(self, section)

Indicate whether the named section is present in the configuration. The DEFAULT section is not acknowledged.

## configparser.RawConfigParser.items(self, section=<object object at 0x7fc8a1920aa0>, raw=False, vars=None)

All % interpolations are expanded in the return values, based on the
defaults passed into the constructor, unless the optional argument
`raw` is true.  Additional substitutions may be provided using the
`vars` argument, which must be a dictionary whose contents overrides
any pre-existing defaults.

The section DEFAULT is special.

## configparser.RawConfigParser.options(self, section)

Return a list of option names for the given section name.

## configparser.RawConfigParser.popitem(self)

Remove a section from the parser and return it as a (section_name, section_proxy) tuple. If no section is present, raise KeyError.

The section DEFAULT is never returned because it cannot be removed.

## configparser.RawConfigParser.read(self, filenames, encoding=None)

Files that cannot be opened are silently ignored; this is
designed so that you can specify an iterable of potential
configuration file locations (e.g. current directory, user's
home directory, systemwide directory), and all existing
configuration files in the iterable will be read.  A single
filename may also be given.

Return list of successfully read files.

## configparser.RawConfigParser.read_dict(self, dictionary, source='<dict>')

Read configuration from a dictionary. Keys are section names, values are dictionaries with keys and values
that should be present in the section. If the used dictionary type
preserves order, sections and their keys will be added in order.

All types held in the dictionary are converted to strings during
reading, including section names, option names and keys.

Optional second argument is the `source` specifying the name of the
dictionary being read.

## configparser.RawConfigParser.read_file(self, f, source=None)

The `f` argument must be iterable, returning one line at a time.
Optional second argument is the `source` specifying the name of the
file being read. If not given, it is taken from f.name. If `f` has no
`name` attribute, `<???>` is used.

## configparser.RawConfigParser.read_string(self, string, source='<string>')

Read configuration from a given string.

## configparser.RawConfigParser.remove_option(self, section, option)

Remove an option.

## configparser.RawConfigParser.remove_section(self, section)

Remove a file section.

## configparser.RawConfigParser.sections(self)

Return a list of section names, excluding [DEFAULT]

## configparser.RawConfigParser.set(self, section, option, value=None)

Set an option.

## configparser.RawConfigParser.write(self, fp, space_around_delimiters=True)

If `space_around_delimiters` is True (the default), delimiters
between keys and values are surrounded by spaces.

Please note that comments in the original configuration file are not
preserved when writing the configuration back.

## configparser.SectionProxy(parser, name)

A proxy for a single section from a parser.

## configparser.SectionProxy.get(self, option, fallback=None, *, raw=False, vars=None, _impl=None, **kwargs)

Get an option value. Unless `fallback` is provided, `None` will be returned if the option
is not found.
