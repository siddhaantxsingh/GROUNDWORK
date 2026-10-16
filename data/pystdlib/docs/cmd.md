# cmd

## cmd.Cmd(completekey='tab', stdin=None, stdout=None)

These are often useful for test harnesses, administrative tools, and
prototypes that will later be wrapped in a more sophisticated interface.

A Cmd instance or subclass instance is a line-oriented interpreter
framework.  There is no good reason to instantiate Cmd itself; rather,
it's useful as a superclass of an interpreter class you define yourself
in order to inherit Cmd's methods and encapsulate action methods.

## cmd.Cmd.cmdloop(self, intro=None)

Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument.

## cmd.Cmd.columnize(self, list, displaywidth=80)

Display a list of strings as a compact set of columns. Each column is only as wide as necessary.
Columns are separated by two spaces (one was not legible enough).

## cmd.Cmd.complete(self, text, state)

Return the next possible completion for 'text'. If a command has not been entered, then complete against command list.
Otherwise try to call complete_<command> to get list of completions.

## cmd.Cmd.completedefault(self, *ignored)

Method called to complete an input line when no command-specific complete_*() method is available. By default, it returns an empty list.

## cmd.Cmd.default(self, line)

Called on an input line when the command prefix is not recognized. If this method is not overridden, it prints an error message and
returns.

## cmd.Cmd.do_help(self, arg)

List available commands with "help" or detailed help with "help cmd".

## cmd.Cmd.emptyline(self)

Called when an empty line is entered in response to the prompt. If this method is not overridden, it repeats the last nonempty
command entered.

## cmd.Cmd.onecmd(self, line)

Interpret the argument as though it had been typed in response to the prompt. This may be overridden, but should not normally need to be;
see the precmd() and postcmd() methods for useful execution hooks.
The return value is a flag indicating whether interpretation of
commands by the interpreter should stop.

## cmd.Cmd.parseline(self, line)

Parse the line into a command name and a string containing the arguments. Returns a tuple containing (command, args, line). 'command' and 'args' may be None if the line couldn't be parsed.

## cmd.Cmd.postcmd(self, stop, line)

Hook method executed just after a command dispatch is finished.

## cmd.Cmd.postloop(self)

Hook method executed once when the cmdloop() method is about to return.

## cmd.Cmd.precmd(self, line)

Hook method executed just before the command line is interpreted, but after the input prompt is generated and issued.

## cmd.Cmd.preloop(self)

Hook method executed once when the cmdloop() method is called.
