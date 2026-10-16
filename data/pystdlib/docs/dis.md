# dis

## dis.Bytecode(x, *, first_line=None, current_offset=None, show_caches=False, adaptive=False, show_offsets=False)

Instantiate this with a function, method, other compiled object, string of
code, or a code object (as returned by compile()).

Iterating over this yields the bytecode operations as Instruction instances.

## dis.Bytecode.dis(self)

Return a formatted view of the bytecode operations.

## dis.Bytecode.from_traceback(...)

Construct a Bytecode from the given traceback

## dis.Bytecode.info(self)

Return formatted information about the code object.

## dis.Formatter.print_instruction_line(self, instr, mark_as_current)

Format instruction details for inclusion in disassembly output.

## dis.Instruction(opname, opcode, arg, argval, argrepr, offset, start_offset, starts_line, line_number, label=None, positions=None, cache_info=None)

Details for a bytecode operation. Defined fields:
  opname - human readable name for operation
  opcode - numeric code for operation
  arg - numeric argument to operation (if any), otherwise None
  argval - resolved arg value (if known), otherwise same as arg
  argrepr - human readable description of operation argument
  offset - start index of operation within bytecode sequence
  start_offset - start index of operation within bytecode sequence including extended args if present;
                 otherwise equal to Instruction.offset
  starts_line - True if this opcode starts a source line, otherwise False
  line_number - source line number associated with this opcode (if any), otherwise None
  label - A label if this instruction is a jump target, otherwise None
  positions - Optional dis.Positions object holding the span of source code
              covered by this instruction
  cache_info - information about the format and content of the instruction's cache
                 entries (if any)

## dis.Positions(lineno=None, end_lineno=None, col_offset=None, end_col_offset=None)

Positions(lineno, end_lineno, col_offset, end_col_offset)

## dis.code_info(x)

Formatted details of methods, functions, or code.

## dis.dis(x=None, *, file=None, depth=None, show_caches=False, adaptive=False, show_offsets=False)

With no argument, disassemble the last traceback.

Compiled objects currently include generator objects, async generator
objects, and coroutine objects, all of which store their code object
in a special attribute.

## dis.disassemble(co, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False)

Disassemble a code object.

## dis.disco(co, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False)

Disassemble a code object.

## dis.distb(tb=None, *, file=None, show_caches=False, adaptive=False, show_offsets=False)

Disassemble a traceback (default: last traceback).

## dis.findlabels(code)

Detect all offsets in a byte code which are jump targets. Return the list of offsets.

## dis.findlinestarts(code)

Find the offsets in a byte code which are start of lines in the source. Generate pairs (offset, lineno)
lineno will be an integer or None the offset does not have a source line.

## dis.get_instructions(x, *, first_line=None, show_caches=None, adaptive=False)

Generates a series of Instruction named tuples giving the details of
each operations in the supplied code.

If *first_line* is not None, it indicates the line number that should
be reported for the first source line in the disassembled code.
Otherwise, the source line information (if any) is taken directly from
the disassembled code object.

## dis.pretty_flags(flags)

Return pretty representation of code flags.

## dis.show_code(co, *, file=None)

Print details of methods, functions, or code to *file*. If *file* is not provided, the output is printed on stdout.
