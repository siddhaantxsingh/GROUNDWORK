# symtable

## symtable.Class.get_methods(self)

Return a tuple of methods declared in the class.

## symtable.Function.get_frees(self)

Return a tuple of free variables in the function.

## symtable.Function.get_globals(self)

Return a tuple of globals in the function.

## symtable.Function.get_locals(self)

Return a tuple of locals in the function.

## symtable.Function.get_nonlocals(self)

Return a tuple of nonlocals in the function.

## symtable.Function.get_parameters(self)

Return a tuple of parameters to the function.

## symtable.Symbol.get_name(self)

Return a name of a symbol.

## symtable.Symbol.get_namespace(self)

Return the single namespace bound to this name. Raises ValueError if the name is bound to multiple namespaces
or no namespace.

## symtable.Symbol.get_namespaces(self)

Return a list of namespaces bound to this name

## symtable.Symbol.is_annotated(self)

Return *True* if the symbol is annotated.

## symtable.Symbol.is_assigned(self)

Return *True* if a symbol is assigned to.

## symtable.Symbol.is_declared_global(self)

Return *True* if the symbol is declared global with a global statement.

## symtable.Symbol.is_free(self)

Return *True* if a referenced symbol is not assigned to.

## symtable.Symbol.is_global(self)

Return *True* if the symbol is global.

## symtable.Symbol.is_imported(self)

Return *True* if the symbol is created from an import statement.

## symtable.Symbol.is_local(self)

Return *True* if the symbol is local.

## symtable.Symbol.is_namespace(self)

If the name is used as the target of a function or class
statement, this will be true.

Note that a single name can be bound to multiple objects.  If
is_namespace() is true, the name may also be bound to other
objects, like an int or list, that does not introduce a new
namespace.

## symtable.Symbol.is_nonlocal(self)

Return *True* if the symbol is nonlocal.

## symtable.Symbol.is_parameter(self)

Return *True* if the symbol is a parameter.

## symtable.Symbol.is_referenced(self)

Return *True* if the symbol is used in its block.

## symtable.SymbolTable.get_children(self)

Return a list of the nested symbol tables.

## symtable.SymbolTable.get_id(self)

Return an identifier for the table.

## symtable.SymbolTable.get_identifiers(self)

Return a view object containing the names of symbols in the table.

## symtable.SymbolTable.get_lineno(self)

Return the number of the first line in the block for the table.

## symtable.SymbolTable.get_name(self)

Return the table's name. This corresponds to the name of the class, function
or 'top' if the table is for a class, function or
global respectively.

## symtable.SymbolTable.get_symbols(self)

Return a list of *Symbol* instances for names in the table.

## symtable.SymbolTable.get_type(self)

Return the type of the symbol table. The value returned is one of the values in
the ``SymbolTableType`` enumeration.

## symtable.SymbolTable.has_children(self)

Return *True* if the block has nested namespaces.

## symtable.SymbolTable.is_nested(self)

Return *True* if the block is a nested class or function.

## symtable.SymbolTable.is_optimized(self)

Return *True* if the locals in the table are optimizable.

## symtable.SymbolTable.lookup(self, name)

Lookup a *name* in the table. Returns a *Symbol* instance.

## symtable.symtable(code, filename, compile_type)

Return the toplevel *SymbolTable* for the source code. *filename* is the name of the file with the code
and *compile_type* is the *compile()* mode argument.
