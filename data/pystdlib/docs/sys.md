# sys

## sys.activate_stack_trampoline(backend, /)

Activate stack profiler trampoline *backend*.

## sys.addaudithook(hook)

Adds a new audit hook callback.

## sys.audit(event, /, *args)

Passes the event to any audit hooks that are attached.

## sys.breakpointhook(*args, **kwargs)

This hook function is called by built-in breakpoint().

## sys.call_tracing(func, args, /)

The tracing state is saved, and restored afterwards.  This is intended
to be called from a debugger from a checkpoint, to recursively debug
some other code.

## sys.deactivate_stack_trampoline()

Deactivate the current stack profiler trampoline backend. If no stack profiler is activated, this function has no effect.

## sys.displayhook(object, /)

Print an object to sys.stdout and also save it in builtins._

## sys.exc_info()

Return current exception information: (type, value, traceback). Return information about the most recent exception caught by an except
clause in the current stack frame or in an older stack frame.

## sys.excepthook(exctype, value, traceback, /)

Handle an exception by displaying it with a traceback on sys.stderr.

## sys.exception()

Return the current exception. Return the most recent exception caught by an except clause
in the current stack frame or in an older stack frame, or None
if no such exception exists.

## sys.exit(status=None, /)

If the status is omitted or None, it defaults to zero (i.e., success).
If the status is an integer, it will be used as the system exit status.
If it is another kind of object, it will be printed and the system
exit status will be one (i.e., failure).

## sys.get_asyncgen_hooks()

Return the installed asynchronous generators hooks. This returns a namedtuple of the form (firstiter, finalizer).

## sys.get_coroutine_origin_tracking_depth()

Check status of origin tracking for coroutine objects in this thread.

## sys.get_int_max_str_digits()

Return the maximum string digits limit for non-binary int<->str conversions.

## sys.getallocatedblocks()

Return the number of memory blocks currently allocated.

## sys.getdefaultencoding()

Return the current default encoding used by the Unicode implementation.

## sys.getdlopenflags()

Return the current value of the flags that are used for dlopen calls. The flag constants are defined in the os module.

## sys.getfilesystemencodeerrors()

Return the error mode used Unicode to OS filename conversion.

## sys.getfilesystemencoding()

Return the encoding used to convert Unicode filenames to OS filenames.

## sys.getprofile()

Return the profiling function set with sys.setprofile. See the profiler chapter in the library manual.

## sys.getrecursionlimit()

The recursion limit is the maximum depth of the Python interpreter
stack.  This limit prevents infinite recursion from causing an overflow
of the C stack and crashing Python.

## sys.getrefcount(object, /)

Return the reference count of object. The count returned is generally one higher than you might expect,
because it includes the (temporary) reference as an argument to
getrefcount().

## sys.getsizeof(...)

Return the size of object in bytes.

## sys.getswitchinterval()

Return the current thread switch interval; see sys.setswitchinterval().

## sys.gettrace()

Return the global debug tracing function set with sys.settrace. See the debugger chapter in the library manual.

## sys.getunicodeinternedsize(*, _only_immortal=False)

Return the number of elements of the unicode interned dictionary

## sys.intern(string, /)

``Intern'' the given string. This enters the string in the (global) table of interned strings whose
purpose is to speed up dictionary lookups. Return the string itself or
the previously interned string object with the same value.

## sys.is_finalizing()

Return True if Python is exiting.

## sys.is_stack_trampoline_active()

Return *True* if a stack profiler trampoline is active.

## sys.set_asyncgen_hooks(...)

Set a finalizer for async generators objects.

## sys.set_coroutine_origin_tracking_depth(depth)

Coroutine objects will track 'depth' frames of traceback information
about where they came from, available in their cr_origin attribute.

Set a depth of 0 to disable.

## sys.set_int_max_str_digits(maxdigits)

Set the maximum string digits limit for non-binary int<->str conversions.

## sys.setdlopenflags(flags, /)

This is used, for example, when the interpreter loads extension
modules. Among other things, this will enable a lazy resolving of
symbols when importing a module, if called as sys.setdlopenflags(0).
To share symbols across extension modules, call as
sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
modules can be found in the os module (RTLD_xxx constants, e.g.
os.RTLD_LAZY).

## sys.setprofile(function, /)

Set the profiling function. It will be called on each function call and return.  See the profiler
chapter in the library manual.

## sys.setrecursionlimit(limit, /)

Set the maximum depth of the Python interpreter stack to n. This limit prevents infinite recursion from causing an overflow of the C
stack and crashing Python.  The highest possible limit is platform-
dependent.

## sys.setswitchinterval(interval, /)

The actual frequency of switching threads can be lower if the
interpreter executes long sequences of uninterruptible code
(this is implementation-specific and workload-dependent).

The parameter must represent the desired switching delay in seconds
A typical value is 0.005 (5 milliseconds).

## sys.settrace(function, /)

Set the global debug tracing function. It will be called on each function call.  See the debugger chapter
in the library manual.

## sys.unraisablehook(unraisable, /)

Handle an unraisable exception. The unraisable argument has the following attributes:

* exc_type: Exception type.
* exc_value: Exception value, can be None.
* exc_traceback: Exception traceback, can be None.
* err_msg: Error message, can be None.
* object: Object causing the exception, can be None.
