# code

## code.InteractiveConsole(locals=None, filename='<console>', *, local_exit=False)

Closely emulate the behavior of the interactive Python interpreter. This class builds on InteractiveInterpreter and adds prompting
using the familiar sys.ps1 and sys.ps2, and input buffering.

## code.InteractiveConsole.interact(self, banner=None, exitmsg=None)

The optional banner argument specifies the banner to print
before the first interaction; by default it prints a banner
similar to the one printed by the real Python interpreter,
followed by the current class name in parentheses (so as not
to confuse this with the real interpreter -- since it's so
close!).

The optional exitmsg argument specifies the exit message
printed when exiting. Pass the empty string to suppress
printing an exit message. If exitmsg is not given or None,
a default message is printed.

## code.InteractiveConsole.push(self, line, filename=None, _symbol='single')

The line should not have a trailing newline; it may have
internal newlines.  The line is appended to a buffer and the
interpreter's runsource() method is called with the
concatenated contents of the buffer as source.  If this
indicates that the command was executed or invalid, the buffer
is reset; otherwise, the command is incomplete, and the buffer
is left as it was after the line was appended.  The return
value is 1 if more input is required, 0 if the line was dealt
with in some way (this is the same as runsource()).

## code.InteractiveConsole.raw_input(self, prompt='')

The returned line does not include the trailing newline.
When the user enters the EOF key sequence, EOFError is raised.

The base implementation uses the built-in function
input(); a subclass may replace this with a different
implementation.

## code.InteractiveConsole.resetbuffer(self)

Reset the input buffer.

## code.InteractiveInterpreter(locals=None)

Base class for InteractiveConsole. This class deals with parsing and interpreter state (the user's
namespace); it doesn't deal with input buffering or prompting or
input file naming (the filename is always passed in explicitly).

## code.InteractiveInterpreter.runcode(self, code)

Execute a code object. When an exception occurs, self.showtraceback() is called to
display a traceback.  All exceptions are caught except
SystemExit, which is reraised.

A note about KeyboardInterrupt: this exception may occur
elsewhere in this code, and may not always be caught.  The
caller should be prepared to deal with it.

## code.InteractiveInterpreter.runsource(self, source, filename='<input>', symbol='single')

Arguments are as for compile_command().

One of several things can happen:

1) The input is incorrect; compile_command() raised an
exception (usually SyntaxError).  A syntax traceback will be
printed by calling the showsyntaxerror() method.

2) The input is incomplete, and more input is required;
compile_command() returned None.  Nothing happens.

3) The input is complete; compile_command() returned a code
object.  The code is executed by calling self.runcode() (which
also handles run-time exceptions, except for SystemExit).

The return value is True in case 2, False in the other cases (unless
an exception is raised).  The return value can be used to
decide whether to use sys.ps1 or sys.ps2 to prompt the next
line.

## code.InteractiveInterpreter.showsyntaxerror(self, filename=None, **kwargs)

This doesn't display a stack trace because there isn't one.

If a filename is given, it is stuffed in the exception instead
of what was there before (because Python's parser always uses
"<string>" when reading from a string).

The output is written by self.write(), below.

## code.InteractiveInterpreter.showtraceback(self)

Display the exception that just occurred. We remove the first stack item because it is our own code.

The output is written by self.write(), below.

## code.InteractiveInterpreter.write(self, data)

Write a string. The base implementation writes to sys.stderr; a subclass may
replace this with a different implementation.

## code.interact(banner=None, readfunc=None, local=None, exitmsg=None, local_exit=False)

This is a backwards compatible interface to the InteractiveConsole
class.  When readfunc is not specified, it attempts to import the
readline module to enable GNU readline if it is available.

Arguments (all optional, all default to None):

banner -- passed to InteractiveConsole.interact()
readfunc -- if not None, replaces InteractiveConsole.raw_input()
local -- passed to InteractiveInterpreter.__init__()
exitmsg -- passed to InteractiveConsole.interact()
local_exit -- passed to InteractiveConsole.__init__()
