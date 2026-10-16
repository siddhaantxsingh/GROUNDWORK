# argparse

## argparse.Action(option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None, deprecated=False)

Action objects are used by an ArgumentParser to represent the information
needed to parse a single argument from one or more strings from the
command line. The keyword arguments to the Action constructor are also
all attributes of Action instances.

Keyword Arguments:

- option_strings -- A list of command-line option strings which
        should be associated with this action.

- dest -- The name of the attribute to hold the created object(s)

- nargs -- The number of command-line arguments that should be
        consumed. By default, one argument will be consumed and a single
        value will be produced.  Other values include:
            - N (an integer) consumes N arguments (and produces a list)
            - '?' consumes zero or one arguments
            - '*' consumes zero or more arguments (and produces a list)
            - '+' consumes one or more arguments (and produces a list)
        Note that the difference between the default and nargs=1 is that
        with the default, a single value will be produced, while with
        nargs=1, a list containing a single value will be produced.

- const -- The value to be produced if the option is specified and the
        option uses an action that takes no values.

- default -- The value to be produced if the option is not specified.

- type -- A callable that accepts a single string argument, and
        returns the converted value.  The standard Python types str, int,
        float, and complex are useful examples of such callables.  If None,
        str is used.

- choices -- A container of values that should be allowed. If not None,
        after a command-line argument has been converted to the appropriate
        type, an exception will be raised if it is not a member of this
        collection.

- required -- True if the action must always be specified at the
        command line. This is only meaningful for optional command-line
        arguments.

- help -- The help string describing the argument.

- metavar -- The name to be used for the option's argument with the
        help string. If None, the 'dest' value will be used as the name.

## argparse.ArgumentDefaultsHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)

Help message formatter which adds default values to argument help. Only the name of this class is considered a public API. All the methods
provided by the class are considered an implementation detail.

## argparse.ArgumentError(argument, message)

An error from creating or using an argument (optional or positional). The string value of this exception is the message, augmented with
information about the argument that caused it.

## argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=<class 'argparse.HelpFormatter'>, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)

Keyword Arguments:
    - prog -- The name of the program (default:
        ``os.path.basename(sys.argv[0])``)
    - usage -- A usage message (default: auto-generated from arguments)
    - description -- A description of what the program does
    - epilog -- Text following the argument descriptions
    - parents -- Parsers whose arguments should be copied into this one
    - formatter_class -- HelpFormatter class for printing help messages
    - prefix_chars -- Characters that prefix optional arguments
    - fromfile_prefix_chars -- Characters that prefix files containing
        additional arguments
    - argument_default -- The default value for all arguments
    - conflict_handler -- String indicating how to handle conflicts
    - add_help -- Add a -h/-help option
    - allow_abbrev -- Allow long options to be abbreviated unambiguously
    - exit_on_error -- Determines whether or not ArgumentParser exits with
        error info when an error occurs

## argparse.ArgumentParser.error(self, message)

Prints a usage message incorporating the message to stderr and exits. If you override this in a subclass, it should not return -- it
should either exit or raise an exception.

## argparse.ArgumentTypeError(...)

An error from trying to convert a command line string to a type.

## argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None)

Instances of FileType are typically passed as type= arguments to the
ArgumentParser add_argument() method.

Keyword Arguments:
    - mode -- A string indicating how the file is to be opened. Accepts the
        same values as the builtin open() function.
    - bufsize -- The file's desired buffer size. Accepts the same values as
        the builtin open() function.
    - encoding -- The file's encoding. Accepts the same values as the
        builtin open() function.
    - errors -- A string indicating how encoding and decoding errors are to
        be handled. Accepts the same value as the builtin open() function.

## argparse.HelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)

Formatter for generating usage messages and argument help strings. Only the name of this class is considered a public API. All the methods
provided by the class are considered an implementation detail.

## argparse.MetavarTypeHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)

Help message formatter which uses the argument 'type' as the default metavar value (instead of the argument 'dest') Only the name of this class is considered a public API. All the methods
provided by the class are considered an implementation detail.

## argparse.Namespace(**kwargs)

Simple object for storing attributes. Implements equality by attribute names and values, and provides a simple
string representation.

## argparse.RawDescriptionHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)

Help message formatter which retains any formatting in descriptions. Only the name of this class is considered a public API. All the methods
provided by the class are considered an implementation detail.

## argparse.RawTextHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)

Help message formatter which retains formatting of all help text. Only the name of this class is considered a public API. All the methods
provided by the class are considered an implementation detail.
