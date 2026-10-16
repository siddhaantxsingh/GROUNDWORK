# codeop

## codeop.CommandCompiler()

Instances of this class have __call__ methods identical in signature to compile_command; the difference is that if the instance compiles program text containing a __future__ statement, the instance 'remembers' and compiles all subsequent program texts with the statement in force.

## codeop.Compile()

Instances of this class behave much like the built-in compile function, but if one is used to compile text containing a future statement, it "remembers" and compiles all subsequent program texts with the statement in force.

## codeop.compile_command(source, filename='<input>', symbol='single')

Arguments:

source -- the source string; may contain \n characters
filename -- optional filename from which source was read; default
            "<input>"
symbol -- optional grammar start symbol; "single" (default), "exec"
          or "eval"

Return value / exceptions raised:

- Return a code object if the command is complete and valid
- Return None if the command is incomplete
- Raise SyntaxError, ValueError or OverflowError if the command is a
  syntax error (OverflowError and ValueError can be produced by
  malformed literals).
