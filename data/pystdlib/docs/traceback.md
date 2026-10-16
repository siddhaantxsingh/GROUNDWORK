# traceback

## traceback.FrameSummary(filename, lineno, name, *, lookup_line=True, locals=None, line=None, end_lineno=None, colno=None, end_colno=None, **kwargs)

- :attr:`filename` The filename for the frame.
- :attr:`lineno` The line within filename for the frame that was
  active when the frame was captured.
- :attr:`name` The name of the function or method that was executing
  when the frame was captured.
- :attr:`line` The text from the linecache module for the line
  of code that was running when the frame was captured.
- :attr:`locals` Either None if locals were not supplied, or a dict
  mapping the name to the repr() of the variable.

## traceback.StackSummary(iterable=(), /)

A list of FrameSummary objects, representing a stack of frames.

## traceback.StackSummary.extract(...)

:param frame_gen: A generator that yields (frame, lineno) tuples
    whose summaries are to be included in the stack.
:param limit: None to include all frames or the number of frames to
    include.
:param lookup_lines: If True, lookup lines for each frame immediately,
    otherwise lookup is deferred until the frame is rendered.
:param capture_locals: If True, the local variables from each frame will
    be captured as object representations into the FrameSummary.

## traceback.StackSummary.format(self, **kwargs)

Returns a list of strings ready for printing.  Each string in the
resulting list corresponds to a single frame from the stack.
Each string ends in a newline; the strings may contain internal
newlines as well, for those items with source text lines.

For long sequences of the same frame and line, the first few
repetitions are shown, followed by a summary line stating the exact
number of further repetitions.

## traceback.StackSummary.format_frame_summary(self, frame_summary, **kwargs)

Format the lines for a single FrameSummary. Returns a string representing one frame involved in the stack. This
gets called for every frame to be printed in the stack summary.

## traceback.StackSummary.from_list(...)

Create a StackSummary object from a supplied list of FrameSummary objects or old-style list of tuples.

## traceback.TracebackException(exc_type, exc_value, exc_traceback, *, limit=None, lookup_lines=True, capture_locals=False, compact=False, max_group_width=15, max_group_depth=10, save_exc_type=True, _seen=None)

An exception ready for rendering. The traceback module captures enough attributes from the original exception
to this intermediary form to ensure that no references are held, while
still being able to fully print or format it.

max_group_width and max_group_depth control the formatting of exception
groups. The depth refers to the nesting level of the group, and the width
refers to the size of a single exception group's exceptions array. The
formatted output is truncated when either limit is exceeded.

Use `from_exception` to create TracebackException instances from exception
objects, or the constructor to create TracebackException instances from
individual components.

- :attr:`__cause__` A TracebackException of the original *__cause__*.
- :attr:`__context__` A TracebackException of the original *__context__*.
- :attr:`exceptions` For exception groups - a list of TracebackException
  instances for the nested *exceptions*.  ``None`` for other exceptions.
- :attr:`__suppress_context__` The *__suppress_context__* value from the
  original exception.
- :attr:`stack` A `StackSummary` representing the traceback.
- :attr:`exc_type` (deprecated) The class of the original traceback.
- :attr:`exc_type_str` String display of exc_type
- :attr:`filename` For syntax errors - the filename where the error
  occurred.
- :attr:`lineno` For syntax errors - the linenumber where the error
  occurred.
- :attr:`end_lineno` For syntax errors - the end linenumber where the error
  occurred. Can be `None` if not present.
- :attr:`text` For syntax errors - the text where the error
  occurred.
- :attr:`offset` For syntax errors - the offset into the text where the
  error occurred.
- :attr:`end_offset` For syntax errors - the end offset into the text where
  the error occurred. Can be `None` if not present.
- :attr:`msg` For syntax errors - the compiler error message.

## traceback.TracebackException.format(self, *, chain=True, _ctx=None, **kwargs)

Format the exception. If chain is not *True*, *__cause__* and *__context__* will not be formatted.

The return value is a generator of strings, each ending in a newline and
some containing internal newlines. `print_exception` is a wrapper around
this method which just prints the lines to a file.

The message indicating which exception occurred is always the last
string in the output.

## traceback.TracebackException.format_exception_only(self, *, show_group=False, _depth=0, **kwargs)

The return value is a generator of strings, each ending in a newline.

Generator yields the exception message.
For :exc:`SyntaxError` exceptions, it
also yields (before the exception message)
several lines that (when printed)
display detailed information about where the syntax error occurred.
Following the message, generator also yields
all the exception's ``__notes__``.

When *show_group* is ``True``, and the exception is an instance of
:exc:`BaseExceptionGroup`, the nested exceptions are included as
well, recursively, with indentation relative to their nesting depth.

## traceback.TracebackException.from_exception(...)

Create a TracebackException from an exception.

## traceback.TracebackException.print(self, *, file=None, chain=True, **kwargs)

Print the result of self.format(chain=chain) to 'file'.

## traceback.clear_frames(tb)

Clear all references to local variables in the frames of a traceback.

## traceback.extract_stack(f=None, limit=None)

The return value has the same format as for extract_tb().  The
optional 'f' and 'limit' arguments have the same meaning as for
print_stack().  Each item in the list is a FrameSummary object,
and the entries are in order from oldest to newest stack frame.

## traceback.extract_tb(tb, limit=None)

This is useful for alternate formatting of stack traces.  If
'limit' is omitted or None, all entries are extracted.  A
pre-processed stack trace entry is a FrameSummary object
representing the information that is usually printed for a
stack trace. The line attribute is a string with
leading and trailing whitespace stripped; if the source is not
available the corresponding attribute is None.

## traceback.format_exc(limit=None, chain=True)

Like print_exc() but return a string.

## traceback.format_exception(exc, /, value=<implicit>, tb=<implicit>, limit=None, chain=True, **kwargs)

The arguments have the same meaning as the corresponding arguments
to print_exception().  The return value is a list of strings, each
ending in a newline and some containing internal newlines.  When
these lines are concatenated and printed, exactly the same text is
printed as does print_exception().

## traceback.format_exception_only(exc, /, value=<implicit>, *, show_group=False, **kwargs)

The return value is a list of strings, each ending in a newline.

The list contains the exception's message, which is
normally a single string; however, for :exc:`SyntaxError` exceptions, it
contains several lines that (when printed) display detailed information
about where the syntax error occurred. Following the message, the list
contains the exception's ``__notes__``.

When *show_group* is ``True``, and the exception is an instance of
:exc:`BaseExceptionGroup`, the nested exceptions are included as
well, recursively, with indentation relative to their nesting depth.

## traceback.format_list(extracted_list)

Given a list of tuples or FrameSummary objects as returned by
extract_tb() or extract_stack(), return a list of strings ready
for printing.

Each string in the resulting list corresponds to the item with the
same index in the argument list.  Each string ends in a newline;
the strings may contain internal newlines as well, for those items
whose source text line is not None.

## traceback.format_stack(f=None, limit=None)

Shorthand for 'format_list(extract_stack(f, limit))'.

## traceback.format_tb(tb, limit=None)

A shorthand for 'format_list(extract_tb(tb, limit))'.

## traceback.print_exc(limit=None, file=None, chain=True)

Shorthand for 'print_exception(sys.exception(), limit=limit, file=file, chain=chain)'.

## traceback.print_exception(exc, /, value=<implicit>, tb=<implicit>, limit=None, file=None, chain=True, **kwargs)

This differs from print_tb() in the following ways: (1) if
traceback is not None, it prints a header "Traceback (most recent
call last):"; (2) it prints the exception type and value after the
stack trace; (3) if type is SyntaxError and value has the
appropriate format, it prints the line where the syntax error
occurred with a caret on the next line indicating the approximate
position of the error.

## traceback.print_last(limit=None, file=None, chain=True)

This is a shorthand for 'print_exception(sys.last_exc, limit=limit, file=file, chain=chain)'.

## traceback.print_list(extracted_list, file=None)

Print the list of tuples as returned by extract_tb() or extract_stack() as a formatted stack trace to the given file.

## traceback.print_stack(f=None, limit=None, file=None)

The optional 'f' argument can be used to specify an alternate
stack frame at which to start. The optional 'limit' and 'file'
arguments have the same meaning as for print_exception().

## traceback.print_tb(tb, limit=None, file=None)

If 'limit' is omitted or None, all entries are printed.  If 'file'
is omitted or None, the output goes to sys.stderr; otherwise
'file' should be an open file or file-like object with a write()
method.

## traceback.walk_stack(f)

Walk a stack yielding the frame and line number for each frame. This will follow f.f_back from the given frame. If no frame is given, the
current stack is used. Usually used with StackSummary.extract.

## traceback.walk_tb(tb)

Walk a traceback yielding the frame and line number for each frame. This will follow tb.tb_next (and thus is in the opposite order to
walk_stack). Usually used with StackSummary.extract.
