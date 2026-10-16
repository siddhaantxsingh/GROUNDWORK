# bdb

## bdb.Bdb(skip=None)

Generic Python debugger base class. This class takes care of details of the trace facility;
a derived class should implement user interaction.
The standard debugger class (pdb.Pdb) is an example.

The optional skip argument must be an iterable of glob-style
module name patterns.  The debugger will not step into frames
that originate in a module that matches one of these patterns.
Whether a frame is considered to originate in a certain module
is determined by the __name__ in the frame globals.

## bdb.Bdb.break_anywhere(self, frame)

Return True if there is any breakpoint for frame's filename.

## bdb.Bdb.break_here(self, frame)

Return True if there is an effective breakpoint for this line. Check for line or function breakpoint and if in effect.
Delete temporary breakpoints if effective() says to.

## bdb.Bdb.canonic(self, filename)

Return canonical form of filename. For real filenames, the canonical form is a case-normalized (on
case insensitive filesystems) absolute path.  'Filenames' with
angle brackets, such as "<stdin>", generated in interactive
mode, are returned unchanged.

## bdb.Bdb.clear_all_breaks(self)

Delete all existing breakpoints. If none were set, return an error message.

## bdb.Bdb.clear_all_file_breaks(self, filename)

Delete all breakpoints in filename. If none were set, return an error message.

## bdb.Bdb.clear_bpbynumber(self, arg)

Delete a breakpoint by its index in Breakpoint.bpbynumber. If arg is invalid, return an error message.

## bdb.Bdb.clear_break(self, filename, lineno)

Delete breakpoints for filename:lineno. If no breakpoints were set, return an error message.

## bdb.Bdb.dispatch_call(self, frame, arg)

Invoke user function and return trace function for call event. If the debugger stops on this function call, invoke
self.user_call(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

## bdb.Bdb.dispatch_exception(self, frame, arg)

Invoke user function and return trace function for exception event. If the debugger stops on this exception, invoke
self.user_exception(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

## bdb.Bdb.dispatch_line(self, frame)

Invoke user function and return trace function for line event. If the debugger stops on the current line, invoke
self.user_line(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

## bdb.Bdb.dispatch_opcode(self, frame, arg)

Invoke user function and return trace function for opcode event. If the debugger stops on the current opcode, invoke self.user_opcode(). Raise BdbQuit if self.quitting is set. Return self.trace_dispatch to continue tracing in this scope.

## bdb.Bdb.dispatch_return(self, frame, arg)

Invoke user function and return trace function for return event. If the debugger stops on this function return, invoke
self.user_return(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

## bdb.Bdb.do_clear(self, arg)

Remove temporary breakpoint. Must implement in derived classes or get NotImplementedError.

## bdb.Bdb.format_stack_entry(self, frame_lineno, lprefix=': ')

The stack entry frame_lineno is a (frame, lineno) tuple.  The
return string contains the canonical filename, the function name
or '<lambda>', the input arguments, the return value, and the
line of code (if it exists).

## bdb.Bdb.get_all_breaks(self)

Return all breakpoints that are set.

## bdb.Bdb.get_bpbynumber(self, arg)

Return a breakpoint by its index in Breakpoint.bybpnumber. For invalid arg values or if the breakpoint doesn't exist,
raise a ValueError.

## bdb.Bdb.get_break(self, filename, lineno)

Return True if there is a breakpoint for filename:lineno.

## bdb.Bdb.get_breaks(self, filename, lineno)

Return all breakpoints for filename:lineno. If no breakpoints are set, return an empty list.

## bdb.Bdb.get_file_breaks(self, filename)

Return all lines with breakpoints for filename. If no breakpoints are set, return an empty list.

## bdb.Bdb.get_stack(self, f, t)

Return a list of (frame, lineno) in a stack trace and a size. List starts with original calling frame, if there is one.
Size may be number of frames above or below f.

## bdb.Bdb.is_skipped_module(self, module_name)

Return True if module_name matches any skip pattern.

## bdb.Bdb.reset(self)

Set values of attributes as ready to start debugging.

## bdb.Bdb.run(self, cmd, globals=None, locals=None)

Debug a statement executed via the exec() function. globals defaults to __main__.dict; locals defaults to globals.

## bdb.Bdb.runcall(self, func, /, *args, **kwds)

Debug a single function call. Return the result of the function call.

## bdb.Bdb.runctx(self, cmd, globals, locals)

For backwards-compatibility. Defers to run().

## bdb.Bdb.runeval(self, expr, globals=None, locals=None)

Debug an expression executed via the eval() function. globals defaults to __main__.dict; locals defaults to globals.

## bdb.Bdb.set_break(self, filename, lineno, temporary=False, cond=None, funcname=None)

Set a new breakpoint for filename:lineno. If lineno doesn't exist for the filename, return an error message.
The filename should be in canonical form.

## bdb.Bdb.set_continue(self)

Stop only at breakpoints or when finished. If there are no breakpoints, set the system trace function to None.

## bdb.Bdb.set_next(self, frame)

Stop on the next line in or below the given frame.

## bdb.Bdb.set_quit(self)

Set quitting attribute to True. Raises BdbQuit exception in the next call to a dispatch_*() method.

## bdb.Bdb.set_return(self, frame)

Stop when returning from the given frame.

## bdb.Bdb.set_step(self)

Stop after one line of code.

## bdb.Bdb.set_stepinstr(self)

Stop before the next instruction.

## bdb.Bdb.set_trace(self, frame=None)

Start debugging from frame. If frame is not specified, debugging starts from caller's frame.

## bdb.Bdb.set_until(self, frame, lineno=None)

Stop when the line with the lineno greater than the current one is reached or when returning from current frame.

## bdb.Bdb.stop_here(self, frame)

Return True if frame is below the starting frame in the stack.

## bdb.Bdb.trace_dispatch(self, frame, event, arg)

This function is installed as the trace function for debugged
frames. Its return value is the new trace function, which is
usually itself. The default implementation decides how to
dispatch a frame, depending on the type of event (passed in as a
string) that is about to be executed.

The event can be one of the following:
    line: A new line of code is going to be executed.
    call: A function is about to be called or another code block
          is entered.
    return: A function or other code block is about to return.
    exception: An exception has occurred.
    c_call: A C function is about to be called.
    c_return: A C function has returned.
    c_exception: A C function has raised an exception.

For the Python events, specialized functions (see the dispatch_*()
methods) are called.  For the C events, no action is taken.

The arg parameter depends on the previous event.

## bdb.Bdb.user_call(self, frame, argument_list)

Called if we might stop in a function.

## bdb.Bdb.user_exception(self, frame, exc_info)

Called when we stop on an exception.

## bdb.Bdb.user_line(self, frame)

Called when we stop or break at a line.

## bdb.Bdb.user_opcode(self, frame)

Called when we are about to execute an opcode.

## bdb.Bdb.user_return(self, frame, return_value)

Called when a return trap is set here.

## bdb.BdbQuit(...)

Exception to give up completely.

## bdb.Breakpoint(file, line, temporary=False, cond=None, funcname=None)

Breakpoint class. Implements temporary breakpoints, ignore counts, disabling and
(re)-enabling, and conditionals.

Breakpoints are indexed by number through bpbynumber and by
the (file, line) tuple using bplist.  The former points to a
single instance of class Breakpoint.  The latter points to a
list of such instances since there may be more than one
breakpoint per line.

When creating a breakpoint, its associated filename should be
in canonical form.  If funcname is defined, a breakpoint hit will be
counted when the first line of that function is executed.  A
conditional breakpoint always counts a hit.

## bdb.Breakpoint.bpformat(self)

Return a string with information about the breakpoint. The information includes the breakpoint number, temporary
status, file:line position, break condition, number of times to
ignore, and number of times hit.

## bdb.Breakpoint.bpprint(self, out=None)

Print the output of bpformat(). The optional out argument directs where the output is sent
and defaults to standard output.

## bdb.Breakpoint.deleteMe(self)

Delete the breakpoint from the list associated to a file:line. If it is the last breakpoint in that position, it also deletes
the entry for the file:line.

## bdb.Breakpoint.disable(self)

Mark the breakpoint as disabled.

## bdb.Breakpoint.enable(self)

Mark the breakpoint as enabled.

## bdb.checkfuncname(b, frame)

Whether a break should happen depends on the way that b (the breakpoint)
was set.  If it was set via line number, check if b.line is the same as
the one in the frame.  If it was set via function name, check if this is
the right function and if it is on the first executable line.

## bdb.effective(file, line, frame)

The "active breakpoint" is the first entry in bplist[line, file] (which
must exist) that is enabled, for which checkfuncname is True, and that
has neither a False condition nor a positive ignore count.  The flag,
meaning that a temporary breakpoint should be deleted, is False only
when the condiion cannot be evaluated (in which case, ignore count is
ignored).

If no such entry exists, then (None, None) is returned.

## bdb.set_trace()

Start debugging with a Bdb instance from the caller's frame.
