# optparse

## optparse.AmbiguousOptionError(opt_str, possibilities)

Raised if an ambiguous option is seen on the command line.

## optparse.BadOptionError(opt_str)

Raised if an invalid option is seen on the command line.

## optparse.HelpFormatter(indent_increment, max_help_position, width, short_first)

OptionParser instances should use one of the HelpFormatter subclasses for formatting help; by default IndentedHelpFormatter is used.

Instance attributes:
  parser : OptionParser
    the controlling OptionParser instance
  indent_increment : int
    the number of columns to indent per nesting level
  max_help_position : int
    the maximum starting column for option help text
  help_position : int
    the calculated starting column for option help text;
    initially the same as the maximum
  width : int
    total number of columns for output (pass None to constructor for
    this value to be taken from the $COLUMNS environment variable)
  level : int
    current indentation level
  current_indent : int
    current indentation level (in columns)
  help_width : int
    number of columns available for option help text (calculated)
  default_tag : str
    text to replace with each option's default value, "%default"
    by default.  Set to false value to disable default value expansion.
  option_strings : { Option : str }
    maps Option instances to the snippet of help text explaining
    the syntax of that option, e.g. "-h, --help" or
    "-fFILE, --file=FILE"
  _short_opt_fmt : str
    format string controlling how short options with values are
    printed in help text.  Must be either "%s%s" ("-fFILE") or
    "%s %s" ("-f FILE"), because those are the two syntaxes that
    Optik supports.
  _long_opt_fmt : str
    similar but for long options; must be either "%s %s" ("--file FILE")
    or "%s=%s" ("--file=FILE").

## optparse.HelpFormatter.format_option_strings(self, option)

Return a comma-separated list of option strings & metavariables.

## optparse.IndentedHelpFormatter(indent_increment=2, max_help_position=24, width=None, short_first=1)

Format help with indented section bodies.

## optparse.Option(*opts, **attrs)

Instance attributes: _short_opts : [string] _long_opts : [string] action : string
  type : string
  dest : string
  default : any
  nargs : int
  const : any
  choices : [string]
  callback : function
  callback_args : (any*)
  callback_kwargs : { string : any }
  help : string
  metavar : string

## optparse.OptionConflictError(msg, option)

Raised if conflicting options are added to an OptionParser.

## optparse.OptionContainer(option_class, conflict_handler, description)

Abstract base class. Class attributes:
  standard_option_list : [Option]
    list of standard options that will be accepted by all instances
    of this parser class (intended to be overridden by subclasses).

Instance attributes:
  option_list : [Option]
    the list of Option objects contained by this OptionContainer
  _short_opt : { string : Option }
    dictionary mapping short option strings, eg. "-f" or "-X",
    to the Option instances that implement them.  If an Option
    has multiple short option strings, it will appear in this
    dictionary multiple times. [1]
  _long_opt : { string : Option }
    dictionary mapping long option strings, eg. "--file" or
    "--exclude", to the Option instances that implement them.
    Again, a given Option can occur multiple times in this
    dictionary. [1]
  defaults : { string : any }
    dictionary mapping option destination names to default
    values for each destination [1]

[1] These mappings are common to (shared by) all components of the
    controlling OptionParser, where they are initially created.

## optparse.OptionContainer.add_option(self, *args, **kwargs)

add_option(Option) add_option(opt_str, ..., kwarg=val, ...)

## optparse.OptionContainer.destroy(self)

see OptionParser.destroy().

## optparse.OptionError(msg, option)

Raised if an Option instance is created with invalid or inconsistent arguments.

## optparse.OptionGroup.destroy(self)

see OptionParser.destroy().

## optparse.OptionParser(usage=None, option_list=None, option_class=<class 'optparse.Option'>, version=None, conflict_handler='error', description=None, formatter=None, add_help_option=True, prog=None, epilog=None)

Instance attributes:
  usage : string
    a usage string for your program.  Before it is displayed
    to the user, "%prog" will be expanded to the name of
    your program (self.prog or os.path.basename(sys.argv[0])).
  prog : string
    the name of the current program (to override
    os.path.basename(sys.argv[0])).
  description : string
    A paragraph of text giving a brief overview of your program.
    optparse reformats this paragraph to fit the current terminal
    width and prints it when the user requests help (after usage,
    but before the list of options).
  epilog : string
    paragraph of help text to print after option help

option_groups : [OptionGroup]
    list of option groups in this parser (option groups are
    irrelevant for parsing the command-line, but very useful
    for generating help)

allow_interspersed_args : bool = true
    if true, positional arguments may be interspersed with options.
    Assuming -a and -b each take a single argument, the command-line
      -ablah foo bar -bboo baz
    will be interpreted the same as
      -ablah -bboo -- foo bar baz
    If this flag were false, that command line would be interpreted as
      -ablah -- foo bar -bboo baz
    -- ie. we stop processing options as soon as we see the first
    non-option argument.  (This is the tradition followed by
    Python's getopt module, Perl's Getopt::Std, and other argument-
    parsing libraries, but it is generally annoying to users.)

process_default_values : bool = true
    if true, option default values are processed similarly to option
    values from the command line: that is, they are passed to the
    type-checking function for the option's type (as long as the
    default value is a string).  (This really only matters if you
    have defined custom types; see SF bug #955889.)  Set it to false
    to restore the behaviour of Optik 1.4.1 and earlier.

rargs : [string]
    the argument list currently being parsed.  Only set when
    parse_args() is active, and continually trimmed down as
    we consume arguments.  Mainly there for the benefit of
    callback options.
  largs : [string]
    the list of leftover arguments that we have skipped while
    parsing options.  If allow_interspersed_args is false, this
    list is always empty.
  values : Values
    the set of option values currently being accumulated.  Only
    set when parse_args() is active.  Also mainly for callbacks.

Because of the 'rargs', 'largs', and 'values' attributes,
OptionParser is not thread-safe.  If, for some perverse reason, you
need to parse command-line arguments simultaneously in different
threads, use different OptionParser instances.

## optparse.OptionParser.check_values(self, values, args)

Returns the option values and leftover arguments (possibly adjusted, possibly completely new -- whatever you like). Default implementation just returns the passed-in values; subclasses may override as desired.

## optparse.OptionParser.destroy(self)

This cleans up reference cycles so the OptionParser (and all objects referenced by it) can be garbage-collected promptly. After calling destroy(), the OptionParser is unusable.

## optparse.OptionParser.disable_interspersed_args(self)

Use this if you have a command processor which runs another command that has options of its own and you want to make sure these options don't get confused.

## optparse.OptionParser.enable_interspersed_args(self)

Set parsing to not stop on the first non-option, allowing interspersing switches with command arguments. This is the default behavior. See also disable_interspersed_args() and the class documentation description of the attribute allow_interspersed_args.

## optparse.OptionParser.error(self, msg)

Print a usage message incorporating 'msg' to stderr and exit. If you override this in a subclass, it should not return -- it should either exit or raise an exception.

## optparse.OptionParser.parse_args(self, args=None, values=None)

Parse the command-line options found in 'args' (default:
sys.argv[1:]).  Any errors result in a call to 'error()', which
by default prints the usage message to stderr and calls
sys.exit() with an error message.  On success returns a pair
(values, args) where 'values' is a Values instance (with all
your option values) and 'args' is the list of arguments left
over after parsing options.

## optparse.OptionParser.print_help(self, file=None)

Print an extended help message, listing all options and any help text provided with them, to 'file' (default stdout).

## optparse.OptionParser.print_usage(self, file=None)

Any occurrence of the string "%prog" in self.usage is replaced with the name of the current program (basename of sys.argv[0]). Does nothing if self.usage is empty or not defined.

## optparse.OptionParser.print_version(self, file=None)

Print the version message for this program (self.version) to 'file' (default stdout). As with print_usage(), any occurrence of "%prog" in self.version is replaced by the current program's name. Does nothing if self.version is empty or undefined.

## optparse.OptionValueError(msg)

Raised if an invalid option value is encountered on the command line.

## optparse.TitledHelpFormatter(indent_increment=0, max_help_position=24, width=None, short_first=0)

Format help with underlined section headers.

## optparse.make_option(*opts, **attrs)

Instance attributes: _short_opts : [string] _long_opts : [string] action : string
  type : string
  dest : string
  default : any
  nargs : int
  const : any
  choices : [string]
  callback : function
  callback_args : (any*)
  callback_kwargs : { string : any }
  help : string
  metavar : string
