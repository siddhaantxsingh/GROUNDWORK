# inspect

## inspect.ArgInfo(args, varargs, keywords, locals)

ArgInfo(args, varargs, keywords, locals)

## inspect.Arguments(args, varargs, varkw)

Arguments(args, varargs, varkw)

## inspect.Attribute(name, kind, defining_class, object)

Attribute(name, kind, defining_class, object)

## inspect.BlockFinder()

Provide a tokeneater() method to detect the end of a code block.

## inspect.BoundArguments(signature, arguments)

Result of `Signature.bind` call. Holds the mapping of arguments to the function's parameters.

Has the following public attributes:

* arguments : dict
    An ordered mutable mapping of parameters' names to arguments' values.
    Does not contain arguments' default values.
* signature : Signature
    The Signature object that created this instance.
* args : tuple
    Tuple of positional arguments values.
* kwargs : dict
    Dict of keyword arguments values.

## inspect.BoundArguments.apply_defaults(self)

Set default values for missing arguments. For variable-positional arguments (*args) the default is an
empty tuple.

For variable-keyword arguments (**kwargs) the default is an
empty dict.

## inspect.ClosureVars(nonlocals, globals, builtins, unbound)

ClosureVars(nonlocals, globals, builtins, unbound)

## inspect.FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)

FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)

## inspect.Parameter(name, kind, *, default, annotation)

Has the following public attributes:

* name : str
    The name of the parameter as a string.
* default : object
    The default value for the parameter if specified.  If the
    parameter has no default value, this attribute is set to
    `Parameter.empty`.
* annotation
    The annotation for the parameter if specified.  If the
    parameter has no annotation, this attribute is set to
    `Parameter.empty`.
* kind
    Describes how argument values are bound to the parameter.
    Possible values: `Parameter.POSITIONAL_ONLY`,
    `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
    `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.
    Every value has a `description` attribute describing meaning.

## inspect.Parameter.replace(self, *, name=<class 'inspect._void'>, kind=<class 'inspect._void'>, annotation=<class 'inspect._void'>, default=<class 'inspect._void'>)

Creates a customized copy of the Parameter.

## inspect.Signature(parameters=None, *, return_annotation, __validate_parameters__=True)

It stores a Parameter object for each parameter accepted by the function, as well as information specific to the function itself.

A Signature object has the following public attributes and methods:

* parameters : OrderedDict
    An ordered mapping of parameters' names to the corresponding
    Parameter objects (keyword-only arguments are in the same order
    as listed in `code.co_varnames`).
* return_annotation : object
    The annotation for the return type of the function if specified.
    If the function has no annotation for its return type, this
    attribute is set to `Signature.empty`.
* bind(*args, **kwargs) -> BoundArguments
    Creates a mapping from positional and keyword arguments to
    parameters.
* bind_partial(*args, **kwargs) -> BoundArguments
    Creates a partial mapping from positional and keyword arguments
    to parameters (simulating 'functools.partial' behavior.)

## inspect.Signature.bind(self, /, *args, **kwargs)

Get a BoundArguments object, that maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

## inspect.Signature.bind_partial(self, /, *args, **kwargs)

Get a BoundArguments object, that partially maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

## inspect.Signature.format(self, *, max_width=None)

If *max_width* integer is passed,
signature will try to fit into the *max_width*.
If signature is longer than *max_width*,
all parameters will be on separate lines.

## inspect.Signature.from_callable(...)

Constructs Signature for the given callable object.

## inspect.Signature.replace(self, *, parameters=<class 'inspect._void'>, return_annotation=<class 'inspect._void'>)

Creates a customized copy of the Signature. Pass 'parameters' and/or 'return_annotation' arguments to override them in the new copy.

## inspect.classify_class_attrs(cls)

Return list of attribute-descriptor tuples. For each name in dir(cls), the return list contains a 4-tuple
with these elements:

0. The name (a string).

1. The kind of attribute this is, one of these strings:
           'class method'    created via classmethod()
           'static method'   created via staticmethod()
           'property'        created via property()
           'method'          any other flavor of method or descriptor
           'data'            not a method

2. The class which defined this attribute (a class).

3. The object as obtained by calling getattr; if this fails, or if the
       resulting object does not live anywhere in the class' mro (including
       metaclasses) then the object is looked up in the defining class's
       dict (found by walking the mro).

If one of the items in dir(cls) is stored in the metaclass it will now
be discovered and not have None be listed as the class in which it was
defined.  Any items whose home class cannot be discovered are skipped.

## inspect.cleandoc(doc)

Clean up indentation from docstrings. Any whitespace that can be uniformly removed from the second line
onwards is removed.

## inspect.currentframe()

Return the frame of the caller or None if this is not possible.

## inspect.findsource(object)

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a list of all the lines
in the file and the line number indexes a line in that list.  An OSError
is raised if the source code cannot be retrieved.

## inspect.formatargvalues(args, varargs, varkw, locals, formatarg=<class 'str'>, formatvarargs=<function <lambda> at 0x7fc8a11d7c40>, formatvarkw=<function <lambda> at 0x7fc8a11d7ce0>, formatvalue=<function <lambda> at 0x7fc8a11d7d80>)

The first four arguments are (args, varargs, varkw, locals).  The
next four arguments are the corresponding optional formatting functions
that are called to turn names and values into strings.  The ninth
argument is an optional function to format the sequence of arguments.

## inspect.get_annotations(obj, *, globals=None, locals=None, eval_str=False)

obj may be a callable, class, or module.
Passing in an object of any other type raises TypeError.

Returns a dict.  get_annotations() returns a new dict every time
it's called; calling it twice on the same object will return two
different but equivalent dicts.

This function handles several details for you:

* If eval_str is true, values of type str will
    be un-stringized using eval().  This is intended
    for use with stringized annotations
    ("from __future__ import annotations").
  * If obj doesn't have an annotations dict, returns an
    empty dict.  (Functions and methods always have an
    annotations dict; classes, modules, and other types of
    callables may not.)
  * Ignores inherited annotations on classes.  If a class
    doesn't have its own annotations dict, returns an empty dict.
  * All accesses to object members and dict values are done
    using getattr() and dict.get() for safety.
  * Always, always, always returns a freshly-created dict.

eval_str controls whether or not values of type str are replaced
with the result of calling eval() on those values:

* If eval_str is true, eval() is called on values of type str.
  * If eval_str is false (the default), values of type str are unchanged.

globals and locals are passed in to eval(); see the documentation
for eval() for more information.  If either globals or locals is
None, this function may replace that value with a context-specific
default, contingent on type(obj):

* If obj is a module, globals defaults to obj.__dict__.
  * If obj is a class, globals defaults to
    sys.modules[obj.__module__].__dict__ and locals
    defaults to the obj class namespace.
  * If obj is a callable, globals defaults to obj.__globals__,
    although if obj is a wrapped function (using
    functools.update_wrapper()) it is first unwrapped.

## inspect.getabsfile(object, _filename=None)

Return an absolute path to the source or compiled file for an object. The idea is for each object to have a unique origin, so this routine
normalizes the result as much as possible.

## inspect.getargs(co)

Three things are returned: (args, varargs, varkw), where
'args' is the list of argument names. Keyword-only arguments are
appended. 'varargs' and 'varkw' are the names of the * and **
arguments or None.

## inspect.getargvalues(frame)

A tuple of four things is returned: (args, varargs, varkw, locals).
'args' is a list of the argument names.
'varargs' and 'varkw' are the names of the * and ** arguments or None.
'locals' is the locals dictionary of the given frame.

## inspect.getasyncgenlocals(agen)

Get the mapping of asynchronous generator local variables to their current values. A dict is returned, with the keys the local variable names and values the
bound values.

## inspect.getasyncgenstate(agen)

Possible states are:
  AGEN_CREATED: Waiting to start execution.
  AGEN_RUNNING: Currently being executed by the interpreter.
  AGEN_SUSPENDED: Currently suspended at a yield expression.
  AGEN_CLOSED: Execution has completed.

## inspect.getattr_static(obj, attr, default=<object object at 0x7fc8a1920750>)

Note: this function may not be able to retrieve all attributes
that getattr can fetch (like dynamically created attributes)
and may find attributes that getattr can't (like descriptors
that raise AttributeError). It can also return descriptor objects
instead of instance members in some cases. See the
documentation for details.

## inspect.getblock(lines)

Extract the block of code at the top of the given list of lines.

## inspect.getcallargs(func, /, *positional, **named)

A dict is returned, with keys the function argument names (including the
names of the * and ** arguments, if any), and values the respective bound
values from 'positional' and 'named'.

## inspect.getclasstree(classes, unique=False)

Where a nested list appears, it contains classes derived from the class
whose entry immediately precedes the list.  Each entry is a 2-tuple
containing a class and a tuple of its base classes.  If the 'unique'
argument is true, exactly one entry appears in the returned structure
for each class in the given list.  Otherwise, classes using multiple
inheritance and their descendants will appear multiple times.

## inspect.getclosurevars(func)

Returns a named tuple of dicts mapping the current nonlocal, global
and builtin references as seen by the body of the function. A final
set of unbound names that could not be resolved is also provided.

## inspect.getcomments(object)

Get lines of comments immediately preceding an object's source code. Returns None when source can't be found.

## inspect.getcoroutinelocals(coroutine)

Get the mapping of coroutine local variables to their current values. A dict is returned, with the keys the local variable names and values the
bound values.

## inspect.getcoroutinestate(coroutine)

Possible states are:
  CORO_CREATED: Waiting to start execution.
  CORO_RUNNING: Currently being executed by the interpreter.
  CORO_SUSPENDED: Currently suspended at an await expression.
  CORO_CLOSED: Execution has completed.

## inspect.getdoc(object)

All tabs are expanded to spaces.  To clean up docstrings that are
indented to line up with blocks of code, any whitespace than can be
uniformly removed from the second line onwards is removed.

## inspect.getfile(object)

Work out which source or compiled file an object was defined in.

## inspect.getframeinfo(frame, context=1)

A tuple of five things is returned: the filename, the line number of
the current line, the function name, a list of lines of context from
the source code, and the index of the current line within that list.
The optional second argument specifies the number of lines of context
to return, which are centered around the current line.

## inspect.getfullargspec(func)

A tuple of seven things is returned:
(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
'args' is a list of the parameter names.
'varargs' and 'varkw' are the names of the * and ** parameters or None.
'defaults' is an n-tuple of the default values of the last n parameters.
'kwonlyargs' is a list of keyword-only parameter names.
'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
'annotations' is a dictionary mapping parameter names to annotations.

Notable differences from inspect.signature():
  - the "self" parameter is always reported, even for bound methods
  - wrapper chains defined by __wrapped__ *not* unwrapped automatically

## inspect.getgeneratorlocals(generator)

Get the mapping of generator local variables to their current values. A dict is returned, with the keys the local variable names and values the
bound values.

## inspect.getgeneratorstate(generator)

Possible states are:
  GEN_CREATED: Waiting to start execution.
  GEN_RUNNING: Currently being executed by the interpreter.
  GEN_SUSPENDED: Currently suspended at a yield expression.
  GEN_CLOSED: Execution has completed.

## inspect.getinnerframes(tb, context=1)

Get a list of records for a traceback's frame and all lower frames. Each record contains a frame object, filename, line number, function
name, a list of lines of context, and index within the context.

## inspect.getlineno(frame)

Get the line number from a frame object, allowing for optimization.

## inspect.getmembers(object, predicate=None)

Return all members of an object as (name, value) pairs sorted by name. Optionally, only return members that satisfy a given predicate.

## inspect.getmembers_static(object, predicate=None)

Optionally, only return members that satisfy a given predicate.

Note: this function may not be able to retrieve all members
   that getmembers can fetch (like dynamically created attributes)
   and may find members that getmembers can't (like descriptors
   that raise AttributeError). It can also return descriptor objects
   instead of instance members in some cases.

## inspect.getmodule(object, _filename=None)

Return the module an object was defined in, or None if not found.

## inspect.getmodulename(path)

Return the module name for a given file, or None.

## inspect.getmro(cls)

Return tuple of base classes (including cls) in method resolution order.

## inspect.getouterframes(frame, context=1)

Get a list of records for a frame and all higher (calling) frames. Each record contains a frame object, filename, line number, function
name, a list of lines of context, and index within the context.

## inspect.getsource(object)

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a single string.  An
OSError is raised if the source code cannot be retrieved.

## inspect.getsourcefile(object)

Return the filename that can be used to locate an object's source. Return None if no way can be identified to get the source.

## inspect.getsourcelines(object)

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a list of the lines
corresponding to the object and the line number indicates where in the
original source file the first line of code was found.  An OSError is
raised if the source code cannot be retrieved.

## inspect.indentsize(line)

Return the indent size, in spaces, at the start of a line of text.

## inspect.isabstract(object)

Return true if the object is an abstract base class (ABC).

## inspect.isasyncgen(object)

Return true if the object is an asynchronous generator.

## inspect.isasyncgenfunction(obj)

Return true if the object is an asynchronous generator function. Asynchronous generator functions are defined with "async def"
syntax and have "yield" expressions in their body.

## inspect.isawaitable(object)

Return true if object can be passed to an ``await`` expression.

## inspect.isbuiltin(object)

Built-in functions and methods provide these attributes:
    __doc__         documentation string
    __name__        original name of this function or method
    __self__        instance to which a method is bound, or None

## inspect.isclass(object)

Return true if the object is a class.

## inspect.iscode(object)

Code objects provide these attributes:
    co_argcount         number of arguments (not including *, ** args
                        or keyword only arguments)
    co_code             string of raw compiled bytecode
    co_cellvars         tuple of names of cell variables
    co_consts           tuple of constants used in the bytecode
    co_filename         name of file in which this code object was created
    co_firstlineno      number of first line in Python source code
    co_flags            bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
                        | 16=nested | 32=generator | 64=nofree | 128=coroutine
                        | 256=iterable_coroutine | 512=async_generator
    co_freevars         tuple of names of free variables
    co_posonlyargcount  number of positional only arguments
    co_kwonlyargcount   number of keyword only arguments (not including ** arg)
    co_lnotab           encoded mapping of line numbers to bytecode indices
    co_name             name with which this code object was defined
    co_names            tuple of names other than arguments and function locals
    co_nlocals          number of local variables
    co_stacksize        virtual machine stack space required
    co_varnames         tuple of names of arguments and local variables

## inspect.iscoroutine(object)

Return true if the object is a coroutine.

## inspect.iscoroutinefunction(obj)

Return true if the object is a coroutine function. Coroutine functions are normally defined with "async def" syntax, but may
be marked via markcoroutinefunction.

## inspect.isdatadescriptor(object)

But not if ismethod(), isclass() or isfunction() is true.

Data descriptors have a __set__ or a __delete__ attribute.  Examples are
properties, getsets, and members.  For the latter two (defined only in C
extension modules) more specific tests are available as well:
isgetsetdescriptor() and ismemberdescriptor(), respectively.

Typically, data descriptors will also have __name__ and __doc__ attributes
(properties, getsets, and members have both of these attributes), but this
is not guaranteed.

## inspect.isframe(object)

Frame objects provide these attributes:
    f_back          next outer frame object (this frame's caller)
    f_builtins      built-in namespace seen by this frame
    f_code          code object being executed in this frame
    f_globals       global namespace seen by this frame
    f_lasti         index of last attempted instruction in bytecode
    f_lineno        current line number in Python source code
    f_locals        local namespace seen by this frame
    f_trace         tracing function for this frame, or None

## inspect.isfunction(object)

Function objects provide these attributes:
    __doc__         documentation string
    __name__        name with which this function was defined
    __code__        code object containing compiled function bytecode
    __defaults__    tuple of any default values for arguments
    __globals__     global namespace in which this function was defined
    __annotations__ dict of parameter annotations
    __kwdefaults__  dict of keyword only parameters with defaults

## inspect.isgenerator(object)

Generator objects provide these attributes:
    __iter__        defined to support iteration over container
    close           raises a new GeneratorExit exception inside the
                    generator to terminate the iteration
    gi_code         code object
    gi_frame        frame object or possibly None once the generator has
                    been exhausted
    gi_running      set to 1 when generator is executing, 0 otherwise
    gi_suspended    set to 1 when the generator is suspended at a yield point, 0 otherwise
    gi_yieldfrom    object being iterated by yield from or None
    next            return the next item from the container
    send            resumes the generator and "sends" a value that becomes
                    the result of the current yield-expression
    throw           used to raise an exception inside the generator

## inspect.isgeneratorfunction(obj)

Return true if the object is a user-defined generator function. Generator function objects provide the same attributes as functions.
See help(isfunction) for a list of attributes.

## inspect.isgetsetdescriptor(object)

Return true if the object is a getset descriptor. getset descriptors are specialized descriptors defined in extension
modules.

## inspect.ismemberdescriptor(object)

Return true if the object is a member descriptor. Member descriptors are specialized descriptors defined in extension
modules.

## inspect.ismethod(object)

Return true if the object is an instance method.

## inspect.ismethoddescriptor(object)

But not if ismethod(), isclass() or isfunction() is true.

An object passing this test (for example, int.__add__) has a __get__
attribute, but not a __set__ attribute or a __delete__ attribute.
Beyond that, the set of attributes varies; __name__ is usually
sensible, and __doc__ often is.

Methods implemented via descriptors that also pass one of the other
tests (ismethod(), isclass(), isfunction()) make this function return
false, simply because those other tests promise more -- you can, for
example, count on having the __func__ attribute when an object passes
ismethod().

## inspect.ismethodwrapper(object)

Return true if the object is a method wrapper.

## inspect.ismodule(object)

Return true if the object is a module.

## inspect.isroutine(object)

Return true if the object is any kind of function or method.

## inspect.istraceback(object)

Traceback objects provide these attributes:
    tb_frame        frame object at this level
    tb_lasti        index of last attempted instruction in bytecode
    tb_lineno       current line number in Python source code
    tb_next         next inner traceback object (called by this level)

## inspect.markcoroutinefunction(func)

Decorator to ensure callable is recognised as a coroutine function.

## inspect.signature(obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)

Get a signature object for the passed callable.

## inspect.stack(context=1)

Return a list of records for the stack above the caller's frame.

## inspect.trace(context=1)

Return a list of records for the stack below the current exception.

## inspect.unwrap(func, *, stop=None)

Follows the chain of :attr:`__wrapped__` attributes returning the last
object in the chain.

*stop* is an optional callback accepting an object in the wrapper chain
as its sole argument that allows the unwrapping to be terminated early if
the callback returns a true value. If the callback never returns a true
value, the last object in the chain is returned as usual. For example,
:func:`signature` uses this to stop unwrapping if any object in the
chain has a ``__signature__`` attribute defined.

:exc:`ValueError` is raised if a cycle is encountered.

## inspect.walktree(classes, children, parent)

Recursive helper function for getclasstree().
