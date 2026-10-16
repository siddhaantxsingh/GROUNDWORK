# pdb

## pdb.Pdb.bp_commands(self, frame)

Call every command that was set for the current active breakpoint (if there is one). Returns True if the normal interaction function must be called,
False otherwise.

## pdb.Pdb.checkline(self, filename, lineno)

Check whether specified line seems to be executable. Return `lineno` if it is, 0 if not (e.g. a docstring, comment, blank
line or EOF). Warning: testing is not comprehensive.

## pdb.Pdb.defaultFile(self)

Produce a reasonable default.

## pdb.Pdb.displayhook(self, obj)

Custom displayhook for the exec in default(), which prevents assignment of the _ variable in the builtins.

## pdb.Pdb.do_EOF(self, arg)

EOF Handles the receipt of EOF as a command.

## pdb.Pdb.do_a(self, arg)

Print the argument list of the current function.

## pdb.Pdb.do_alias(self, arg)

alias [name [command]] Create an alias called 'name' that executes 'command'.  The
command must *not* be enclosed in quotes.  Replaceable
parameters can be indicated by %1, %2, and so on, while %* is
replaced by all the parameters.  If no command is given, the
current alias for name is shown. If no name is given, all
aliases are listed.

Aliases may be nested and can contain anything that can be
legally typed at the pdb prompt.  Note!  You *can* override
internal pdb commands with aliases!  Those internal commands
are then hidden until the alias is removed.  Aliasing is
recursively applied to the first word of the command line; all
other words in the line are left alone.

As an example, here are two useful aliases (especially when
placed in the .pdbrc file):

# Print instance variables (usage "pi classInst")
alias pi for k in %1.__dict__.keys(): print("%1.",k,"=",%1.__dict__[k])
# Print instance variables in self
alias ps pi self

## pdb.Pdb.do_args(self, arg)

Print the argument list of the current function.

## pdb.Pdb.do_b(self, arg, temporary=0)

b(reak) [ ([filename:]lineno | function) [, condition] ] Without argument, list all breaks.

With a line number argument, set a break at this line in the
current file.  With a function name, set a break at the first
executable line of that function.  If a second argument is
present, it is a string specifying an expression which must
evaluate to true before the breakpoint is honored.

The line number may be prefixed with a filename and a colon,
to specify a breakpoint in another file (probably one that
hasn't been loaded yet).  The file is searched for on
sys.path; the .py suffix may be omitted.

## pdb.Pdb.do_break(self, arg, temporary=0)

b(reak) [ ([filename:]lineno | function) [, condition] ] Without argument, list all breaks.

With a line number argument, set a break at this line in the
current file.  With a function name, set a break at the first
executable line of that function.  If a second argument is
present, it is a string specifying an expression which must
evaluate to true before the breakpoint is honored.

The line number may be prefixed with a filename and a colon,
to specify a breakpoint in another file (probably one that
hasn't been loaded yet).  The file is searched for on
sys.path; the .py suffix may be omitted.

## pdb.Pdb.do_bt(self, arg)

Print a stack trace, with the most recent frame at the bottom. An arrow indicates the "current frame", which determines the context of most commands. 'bt' is an alias for this command.

## pdb.Pdb.do_c(self, arg)

Continue execution, only stop when a breakpoint is encountered.

## pdb.Pdb.do_cl(self, arg)

cl(ear) [filename:lineno | bpnumber ...] With a space separated list of breakpoint numbers, clear
those breakpoints.  Without argument, clear all breaks (but
first ask confirmation).  With a filename:lineno argument,
clear all breaks at that line in that file.

## pdb.Pdb.do_clear(self, arg)

cl(ear) [filename:lineno | bpnumber ...] With a space separated list of breakpoint numbers, clear
those breakpoints.  Without argument, clear all breaks (but
first ask confirmation).  With a filename:lineno argument,
clear all breaks at that line in that file.

## pdb.Pdb.do_commands(self, arg)

(Pdb) commands [bpnumber] (com) ... (com) end (Pdb)

Specify a list of commands for breakpoint number bpnumber.
The commands themselves are entered on the following lines.
Type a line containing just 'end' to terminate the commands.
The commands are executed when the breakpoint is hit.

To remove all commands from a breakpoint, type commands and
follow it immediately with end; that is, give no commands.

With no bpnumber argument, commands refers to the last
breakpoint set.

You can use breakpoint commands to start your program up
again.  Simply use the continue command, or step, or any other
command that resumes execution.

Specifying any command resuming execution (currently continue,
step, next, return, jump, quit and their abbreviations)
terminates the command list (as if that command was
immediately followed by end).  This is because any time you
resume execution (even with a simple next or step), you may
encounter another breakpoint -- which could have its own
command list, leading to ambiguities about which list to
execute.

If you use the 'silent' command in the command list, the usual
message about stopping at a breakpoint is not printed.  This
may be desirable for breakpoints that are to print a specific
message and then continue.  If none of the other commands
print anything, you will see no sign that the breakpoint was
reached.

## pdb.Pdb.do_condition(self, arg)

condition bpnumber [condition] Set a new condition for the breakpoint, an expression which
must evaluate to true before the breakpoint is honored.  If
condition is absent, any existing condition is removed; i.e.,
the breakpoint is made unconditional.

## pdb.Pdb.do_cont(self, arg)

Continue execution, only stop when a breakpoint is encountered.

## pdb.Pdb.do_continue(self, arg)

Continue execution, only stop when a breakpoint is encountered.

## pdb.Pdb.do_d(self, arg)

d(own) [count] Move the current frame count (default one) levels down in the
stack trace (to a newer frame).

## pdb.Pdb.do_debug(self, arg)

debug code Enter a recursive debugger that steps through the code
argument (which is an arbitrary expression or statement to be
executed in the current environment).

## pdb.Pdb.do_disable(self, arg)

disable bpnumber [bpnumber ...] Disables the breakpoints given as a space separated list of
breakpoint numbers.  Disabling a breakpoint means it cannot
cause the program to stop execution, but unlike clearing a
breakpoint, it remains in the list of breakpoints and can be
(re-)enabled.

## pdb.Pdb.do_display(self, arg)

display [expression] Display the value of the expression if it changed, each time execution
stops in the current frame.

Without expression, list all display expressions for the current frame.

## pdb.Pdb.do_down(self, arg)

d(own) [count] Move the current frame count (default one) levels down in the
stack trace (to a newer frame).

## pdb.Pdb.do_enable(self, arg)

enable bpnumber [bpnumber ...] Enables the breakpoints given as a space separated list of
breakpoint numbers.

## pdb.Pdb.do_exceptions(self, arg)

exceptions [number] List or change current exception in an exception chain.

Without arguments, list all the current exception in the exception
chain. Exceptions will be numbered, with the current exception indicated
with an arrow.

If given an integer as argument, switch to the exception at that index.

## pdb.Pdb.do_exit(self, arg)

q(uit) | exit Quit from the debugger. The program being executed is aborted.

## pdb.Pdb.do_h(self, arg)

Without argument, print the list of available commands. With a command name as argument, print help about that command. "help pdb" shows the full pdb documentation. "help exec" gives help on the ! command.

## pdb.Pdb.do_help(self, arg)

Without argument, print the list of available commands. With a command name as argument, print help about that command. "help pdb" shows the full pdb documentation. "help exec" gives help on the ! command.

## pdb.Pdb.do_ignore(self, arg)

ignore bpnumber [count] Set the ignore count for the given breakpoint number.  If
count is omitted, the ignore count is set to 0.  A breakpoint
becomes active when the ignore count is zero.  When non-zero,
the count is decremented each time the breakpoint is reached
and the breakpoint is not disabled and any associated
condition evaluates to true.

## pdb.Pdb.do_interact(self, arg)

interact Start an interactive interpreter whose global namespace
contains all the (global and local) names found in the current scope.

## pdb.Pdb.do_j(self, arg)

j(ump) lineno Set the next line that will be executed.  Only available in
the bottom-most frame.  This lets you jump back and execute
code again, or jump forward to skip code that you don't want
to run.

It should be noted that not all jumps are allowed -- for
instance it is not possible to jump into the middle of a
for loop or out of a finally clause.

## pdb.Pdb.do_jump(self, arg)

j(ump) lineno Set the next line that will be executed.  Only available in
the bottom-most frame.  This lets you jump back and execute
code again, or jump forward to skip code that you don't want
to run.

It should be noted that not all jumps are allowed -- for
instance it is not possible to jump into the middle of a
for loop or out of a finally clause.

## pdb.Pdb.do_l(self, arg)

l(ist) [first[, last] | .] List source code for the current file.  Without arguments,
list 11 lines around the current line or continue the previous
listing.  With . as argument, list 11 lines around the current
line.  With one argument, list 11 lines starting at that line.
With two arguments, list the given range; if the second
argument is less than the first, it is a count.

The current line in the current frame is indicated by "->".
If an exception is being debugged, the line where the
exception was originally raised or propagated is indicated by
">>", if it differs from the current line.

## pdb.Pdb.do_list(self, arg)

l(ist) [first[, last] | .] List source code for the current file.  Without arguments,
list 11 lines around the current line or continue the previous
listing.  With . as argument, list 11 lines around the current
line.  With one argument, list 11 lines starting at that line.
With two arguments, list the given range; if the second
argument is less than the first, it is a count.

The current line in the current frame is indicated by "->".
If an exception is being debugged, the line where the
exception was originally raised or propagated is indicated by
">>", if it differs from the current line.

## pdb.Pdb.do_ll(self, arg)

ll | longlist List the whole source code for the current function or frame.

## pdb.Pdb.do_longlist(self, arg)

ll | longlist List the whole source code for the current function or frame.

## pdb.Pdb.do_n(self, arg)

Continue execution until the next line in the current function is reached or it returns.

## pdb.Pdb.do_next(self, arg)

Continue execution until the next line in the current function is reached or it returns.

## pdb.Pdb.do_p(self, arg)

p expression Print the value of the expression.

## pdb.Pdb.do_pp(self, arg)

pp expression Pretty-print the value of the expression.

## pdb.Pdb.do_q(self, arg)

q(uit) | exit Quit from the debugger. The program being executed is aborted.

## pdb.Pdb.do_quit(self, arg)

q(uit) | exit Quit from the debugger. The program being executed is aborted.

## pdb.Pdb.do_r(self, arg)

Continue execution until the current function returns.

## pdb.Pdb.do_restart(self, arg)

run [args...] Restart the debugged python program. If a string is supplied
it is split with "shlex", and the result is used as the new
sys.argv.  History, breakpoints, actions and debugger options
are preserved.  "restart" is an alias for "run".

## pdb.Pdb.do_return(self, arg)

Continue execution until the current function returns.

## pdb.Pdb.do_retval(self, arg)

retval Print the return value for the last return of a function.

## pdb.Pdb.do_run(self, arg)

run [args...] Restart the debugged python program. If a string is supplied
it is split with "shlex", and the result is used as the new
sys.argv.  History, breakpoints, actions and debugger options
are preserved.  "restart" is an alias for "run".

## pdb.Pdb.do_rv(self, arg)

retval Print the return value for the last return of a function.

## pdb.Pdb.do_s(self, arg)

Execute the current line, stop at the first possible occasion (either in a function that is called or in the current function).

## pdb.Pdb.do_source(self, arg)

source expression Try to get source code for the given object and display it.

## pdb.Pdb.do_step(self, arg)

Execute the current line, stop at the first possible occasion (either in a function that is called or in the current function).

## pdb.Pdb.do_tbreak(self, arg)

tbreak [ ([filename:]lineno | function) [, condition] ] Same arguments as break, but sets a temporary breakpoint: it
is automatically deleted when first hit.

## pdb.Pdb.do_u(self, arg)

u(p) [count] Move the current frame count (default one) levels up in the
stack trace (to an older frame).

## pdb.Pdb.do_unalias(self, arg)

unalias name Delete the specified alias.

## pdb.Pdb.do_undisplay(self, arg)

undisplay [expression] Do not display the expression any more in the current frame.

Without expression, clear all display expressions for the current frame.

## pdb.Pdb.do_unt(self, arg)

unt(il) [lineno] Without argument, continue execution until the line with a
number greater than the current one is reached.  With a line
number, continue execution until a line with a number greater
or equal to that is reached.  In both cases, also stop when
the current frame returns.

## pdb.Pdb.do_until(self, arg)

unt(il) [lineno] Without argument, continue execution until the line with a
number greater than the current one is reached.  With a line
number, continue execution until a line with a number greater
or equal to that is reached.  In both cases, also stop when
the current frame returns.

## pdb.Pdb.do_up(self, arg)

u(p) [count] Move the current frame count (default one) levels up in the
stack trace (to an older frame).

## pdb.Pdb.do_w(self, arg)

Print a stack trace, with the most recent frame at the bottom. An arrow indicates the "current frame", which determines the context of most commands. 'bt' is an alias for this command.

## pdb.Pdb.do_whatis(self, arg)

whatis expression Print the type of the argument.

## pdb.Pdb.do_where(self, arg)

Print a stack trace, with the most recent frame at the bottom. An arrow indicates the "current frame", which determines the context of most commands. 'bt' is an alias for this command.

## pdb.Pdb.handle_command_def(self, line)

Handles one command line during command list definition.

## pdb.Pdb.help_exec(self)

(!) statement Execute the (one-line) statement in the context of the current
stack frame.  The exclamation point can be omitted unless the
first word of the statement resembles a debugger command, e.g.:
(Pdb) ! n=42
(Pdb)

To assign to a global variable you must always prefix the command with
a 'global' command, e.g.:
(Pdb) global list_options; list_options = ['-l']
(Pdb)

## pdb.Pdb.lookupmodule(self, filename)

lookupmodule() translates (possibly incomplete) file or module name
into an absolute file name.

filename could be in format of:
    * an absolute path like '/path/to/file.py'
    * a relative path like 'file.py' or 'dir/file.py'
    * a module name like 'module' or 'package.module'

files and modules will be searched in sys.path.

## pdb.Pdb.onecmd(self, line)

Interpret the argument as though it had been typed in response to the prompt. Checks whether this line is typed at the normal prompt or in
a breakpoint command list definition.

## pdb.Pdb.precmd(self, line)

Handle alias expansion and ';;' separator.

## pdb.Pdb.user_call(self, frame, argument_list)

This method is called when there is the remote possibility that we ever need to stop in this function.

## pdb.Pdb.user_exception(self, frame, exc_info)

This function is called if an exception occurs, but only if we are to stop at or just below this level.

## pdb.Pdb.user_line(self, frame)

This function is called when we stop or break at this line.

## pdb.Pdb.user_opcode(self, frame)

This function is called when we stop or break at this line.

## pdb.Pdb.user_return(self, frame, return_value)

This function is called when a return trap is set here.

## pdb.Restart(...)

Causes a debugger to be restarted for the debugged python program.

## pdb.find_first_executable_line(code)

Try to find the first executable line of the code object. Equivalently, find the line number of the instruction that's
after RESUME

Return code.co_firstlineno if no executable line is found.

## pdb.pm()

Enter post-mortem debugging of the traceback found in sys.last_exc.

## pdb.post_mortem(t=None)

If no traceback is given, it uses the one of the exception that is
currently being handled (an exception must be being handled if the
default is to be used).

If `t` is an exception object, the `exceptions` command makes it possible to
list and inspect its chained exceptions (if any).

## pdb.run(statement, globals=None, locals=None)

The debugger prompt appears before any code is executed; you can set
breakpoints and type continue, or you can step through the statement
using step or next.

The optional *globals* and *locals* arguments specify the
environment in which the code is executed; by default the
dictionary of the module __main__ is used (see the explanation of
the built-in exec() or eval() functions.).

## pdb.runcall(*args, **kwds)

Call the function (a function or method object, not a string) with the given arguments. When runcall() returns, it returns whatever the function call
returned. The debugger prompt appears as soon as the function is
entered.

## pdb.runeval(expression, globals=None, locals=None)

Evaluate the *expression* (given as a string or a code object) under debugger control. When runeval() returns, it returns the value of the expression.
Otherwise this function is similar to run().

## pdb.set_trace(*, header=None)

This is useful to hard-code a breakpoint at a given point in a
program, even if the code is not otherwise being debugged (e.g. when
an assertion fails). If given, *header* is printed to the console
just before debugging begins.
