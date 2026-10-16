# ast

## ast.Add(...)

Add

## ast.And(...)

And

## ast.AnnAssign(...)

AnnAssign(expr target, expr annotation, expr? value, int simple)

## ast.Assert(...)

Assert(expr test, expr? msg)

## ast.Assign(...)

Assign(expr* targets, expr value, string? type_comment)

## ast.AsyncFor(...)

AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)

## ast.AsyncFunctionDef(...)

AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment, type_param* type_params)

## ast.AsyncWith(...)

AsyncWith(withitem* items, stmt* body, string? type_comment)

## ast.Attribute(...)

Attribute(expr value, identifier attr, expr_context ctx)

## ast.AugAssign(...)

AugAssign(expr target, operator op, expr value)

## ast.AugLoad(...)

Deprecated AST node class. Unused in Python 3.

## ast.AugStore(...)

Deprecated AST node class. Unused in Python 3.

## ast.Await(...)

Await(expr value)

## ast.BinOp(...)

BinOp(expr left, operator op, expr right)

## ast.BitAnd(...)

BitAnd

## ast.BitOr(...)

BitOr

## ast.BitXor(...)

BitXor

## ast.BoolOp(...)

BoolOp(boolop op, expr* values)

## ast.Break(...)

Break

## ast.Call(...)

Call(expr func, expr* args, keyword* keywords)

## ast.ClassDef(...)

ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list, type_param* type_params)

## ast.Compare(...)

Compare(expr left, cmpop* ops, expr* comparators)

## ast.Constant(...)

Constant(constant value, string? kind)

## ast.Continue(...)

Continue

## ast.Del(...)

Del

## ast.Delete(...)

Delete(expr* targets)

## ast.Dict(...)

Dict(expr* keys, expr* values)

## ast.DictComp(...)

DictComp(expr key, expr value, comprehension* generators)

## ast.Div(...)

Div

## ast.Eq(...)

Eq

## ast.ExceptHandler(...)

ExceptHandler(expr? type, identifier? name, stmt* body)

## ast.Expr(...)

Expr(expr value)

## ast.Expression(...)

Expression(expr body)

## ast.ExtSlice(dims=(), **kwargs)

Deprecated AST node class. Use ast.Tuple instead.

## ast.FloorDiv(...)

FloorDiv

## ast.For(...)

For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)

## ast.FormattedValue(...)

FormattedValue(expr value, int conversion, expr? format_spec)

## ast.FunctionDef(...)

FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment, type_param* type_params)

## ast.FunctionType(...)

FunctionType(expr* argtypes, expr returns)

## ast.GeneratorExp(...)

GeneratorExp(expr elt, comprehension* generators)

## ast.Global(...)

Global(identifier* names)

## ast.Gt(...)

Gt

## ast.GtE(...)

GtE

## ast.If(...)

If(expr test, stmt* body, stmt* orelse)

## ast.IfExp(...)

IfExp(expr test, expr body, expr orelse)

## ast.Import(...)

Import(alias* names)

## ast.ImportFrom(...)

ImportFrom(identifier? module, alias* names, int? level)

## ast.In(...)

In

## ast.Index(value, **kwargs)

Deprecated AST node class. Use the index value directly instead.

## ast.Interactive(...)

Interactive(stmt* body)

## ast.Invert(...)

Invert

## ast.Is(...)

Is

## ast.IsNot(...)

IsNot

## ast.JoinedStr(...)

JoinedStr(expr* values)

## ast.LShift(...)

LShift

## ast.Lambda(...)

Lambda(arguments args, expr body)

## ast.List(...)

List(expr* elts, expr_context ctx)

## ast.ListComp(...)

ListComp(expr elt, comprehension* generators)

## ast.Load(...)

Load

## ast.Lt(...)

Lt

## ast.LtE(...)

LtE

## ast.MatMult(...)

MatMult

## ast.Match(...)

Match(expr subject, match_case* cases)

## ast.MatchAs(...)

MatchAs(pattern? pattern, identifier? name)

## ast.MatchClass(...)

MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)

## ast.MatchMapping(...)

MatchMapping(expr* keys, pattern* patterns, identifier? rest)

## ast.MatchOr(...)

MatchOr(pattern* patterns)

## ast.MatchSequence(...)

MatchSequence(pattern* patterns)

## ast.MatchSingleton(...)

MatchSingleton(constant value)

## ast.MatchStar(...)

MatchStar(identifier? name)

## ast.MatchValue(...)

MatchValue(expr value)

## ast.Mod(...)

Mod

## ast.Module(...)

Module(stmt* body, type_ignore* type_ignores)

## ast.Mult(...)

Mult

## ast.Name(...)

Name(identifier id, expr_context ctx)

## ast.NamedExpr(...)

NamedExpr(expr target, expr value)

## ast.NodeTransformer()

The `NodeTransformer` will walk the AST and use the return value of the
visitor methods to replace or remove the old node.  If the return value of
the visitor method is ``None``, the node will be removed from its location,
otherwise it is replaced with the return value.  The return value may be the
original node in which case no replacement takes place.

Here is an example transformer that rewrites all occurrences of name lookups
(``foo``) to ``data['foo']``::

class RewriteName(NodeTransformer):

def visit_Name(self, node):
           return Subscript(
               value=Name(id='data', ctx=Load()),
               slice=Constant(value=node.id),
               ctx=node.ctx
           )

Keep in mind that if the node you're operating on has child nodes you must
either transform the child nodes yourself or call the :meth:`generic_visit`
method for the node first.

For nodes that were part of a collection of statements (that applies to all
statement nodes), the visitor may also return a list of nodes rather than
just a single node.

Usually you use the transformer like this::

node = YourTransformer().visit(node)

## ast.NodeVisitor()

This function may return a value which is forwarded by the `visit` method.

This class is meant to be subclassed, with the subclass adding visitor
methods.

Per default the visitor functions for the nodes are ``'visit_'`` +
class name of the node.  So a `TryFinally` node visit function would
be `visit_TryFinally`.  This behavior can be changed by overriding
the `visit` method.  If no visitor function exists for a node
(return value `None`) the `generic_visit` visitor is used instead.

Don't use the `NodeVisitor` if you want to apply changes to nodes during
traversing.  For this a special visitor exists (`NodeTransformer`) that
allows modifications.

## ast.NodeVisitor.generic_visit(self, node)

Called if no explicit visitor function exists for a node.

## ast.NodeVisitor.visit(self, node)

Visit a node.

## ast.Nonlocal(...)

Nonlocal(identifier* names)

## ast.Not(...)

Not

## ast.NotEq(...)

NotEq

## ast.NotIn(...)

NotIn

## ast.Or(...)

Or

## ast.Param(...)

Deprecated AST node class. Unused in Python 3.

## ast.ParamSpec(...)

ParamSpec(identifier name, expr? default_value)

## ast.Pass(...)

Pass

## ast.Pow(...)

Pow

## ast.RShift(...)

RShift

## ast.Raise(...)

Raise(expr? exc, expr? cause)

## ast.Return(...)

Return(expr? value)

## ast.Set(...)

Set(expr* elts)

## ast.SetComp(...)

SetComp(expr elt, comprehension* generators)

## ast.Slice(...)

Slice(expr? lower, expr? upper, expr? step)

## ast.Starred(...)

Starred(expr value, expr_context ctx)

## ast.Store(...)

Store

## ast.Sub(...)

Sub

## ast.Subscript(...)

Subscript(expr value, expr slice, expr_context ctx)

## ast.Suite(...)

Deprecated AST node class. Unused in Python 3.

## ast.Try(...)

Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)

## ast.TryStar(...)

TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)

## ast.Tuple(...)

Tuple(expr* elts, expr_context ctx)

## ast.TypeAlias(...)

TypeAlias(expr name, type_param* type_params, expr value)

## ast.TypeIgnore(...)

TypeIgnore(int lineno, string tag)

## ast.TypeVar(...)

TypeVar(identifier name, expr? bound, expr? default_value)

## ast.TypeVarTuple(...)

TypeVarTuple(identifier name, expr? default_value)

## ast.UAdd(...)

UAdd

## ast.USub(...)

USub

## ast.UnaryOp(...)

UnaryOp(unaryop op, expr operand)

## ast.While(...)

While(expr test, stmt* body, stmt* orelse)

## ast.With(...)

With(withitem* items, stmt* body, string? type_comment)

## ast.Yield(...)

Yield(expr? value)

## ast.YieldFrom(...)

YieldFrom(expr value)

## ast.alias(...)

alias(identifier name, identifier? asname)

## ast.arg(...)

arg(identifier arg, expr? annotation, string? type_comment)

## ast.arguments(...)

arguments(arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs, expr* kw_defaults, arg? kwarg, expr* defaults)

## ast.boolop(...)

boolop = And | Or

## ast.cmpop(...)

cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn

## ast.comprehension(...)

comprehension(expr target, expr iter, expr* ifs, int is_async)

## ast.copy_location(new_node, old_node)

Copy source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset` attributes) from *old_node* to *new_node* if possible, and return *new_node*.

## ast.dump(node, annotate_fields=True, include_attributes=False, *, indent=None, show_empty=False)

This is mainly useful for debugging purposes. If annotate_fields is true (by default), the returned string will show the names and the values for fields. If annotate_fields is false, the result string will be more compact by omitting unambiguous field names. Attributes such as line numbers and column offsets are not dumped by default. If this is wanted, include_attributes can be set to true. If indent is a non-negative integer or string, then the tree will be pretty-printed with that indent level. None (the default) selects the single line representation. If show_empty is False, then empty lists and fields that are None will be omitted from the output for better readability.

## ast.excepthandler(...)

excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)

## ast.expr(...)

expr = BoolOp(boolop op, expr* values) | NamedExpr(expr target, expr value) | BinOp(expr left, operator op, expr right) | UnaryOp(unaryop op, expr operand) | Lambda(arguments args, expr body) | IfExp(expr test, expr body, expr orelse) | Dict(expr* keys, expr* values) | Set(expr* elts) | ListComp(expr elt, comprehension* generators) | SetComp(expr elt, comprehension* generators) | DictComp(expr key, expr value, comprehension* generators) | GeneratorExp(expr elt, comprehension* generators) | Await(expr value) | Yield(expr? value) | YieldFrom(expr value) | Compare(expr left, cmpop* ops, expr* comparators) | Call(expr func, expr* args, keyword* keywords) | FormattedValue(expr value, int conversion, expr? format_spec) | JoinedStr(expr* values) | Constant(constant value, string? kind) | Attribute(expr value, identifier attr, expr_context ctx) | Subscript(expr value, expr slice, expr_context ctx) | Starred(expr value, expr_context ctx) | Name(identifier id, expr_context ctx) | List(expr* elts, expr_context ctx) | Tuple(expr* elts, expr_context ctx) | Slice(expr? lower, expr? upper, expr? step)

## ast.expr_context(...)

expr_context = Load | Store | Del

## ast.fix_missing_locations(node)

This is rather tedious to fill in for generated nodes, so this helper adds these attributes recursively where not already set, by setting them to the values of the parent node. It works recursively starting at *node*.

## ast.get_docstring(node, clean=True)

If the node provided does not have docstrings a TypeError will be raised.

If *clean* is `True`, all tabs are expanded to spaces and any whitespace
that can be uniformly removed from the second line onwards is removed.

## ast.get_source_segment(source, node, *, padded=False)

If some location information (`lineno`, `end_lineno`, `col_offset`,
or `end_col_offset`) is missing, return None.

If *padded* is `True`, the first line of a multi-line statement will
be padded with spaces to match its original position.

## ast.increment_lineno(node, n=1)

Increment the line number and end line number of each node in the tree starting at *node* by *n*. This is useful to "move code" to a different location in a file.

## ast.iter_child_nodes(node)

Yield all direct child nodes of *node*, that is, all fields that are nodes and all items of fields that are lists of nodes.

## ast.iter_fields(node)

Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields`` that is present on *node*.

## ast.keyword(...)

keyword(identifier? arg, expr value)

## ast.literal_eval(node_or_string)

The string or node provided may only consist of the following Python literal structures: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.

Caution: A complex expression can overflow the C stack and cause a crash.

## ast.match_case(...)

match_case(pattern pattern, expr? guard, stmt* body)

## ast.mod(...)

mod = Module(stmt* body, type_ignore* type_ignores) | Interactive(stmt* body) | Expression(expr body) | FunctionType(expr* argtypes, expr returns)

## ast.operator(...)

operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv

## ast.parse(source, filename='<unknown>', mode='exec', *, type_comments=False, feature_version=None, optimize=-1)

Parse the source into an AST node. Equivalent to compile(source, filename, mode, PyCF_ONLY_AST). Pass type_comments=True to get back type comments where the syntax allows.

## ast.pattern(...)

pattern = MatchValue(expr value) | MatchSingleton(constant value) | MatchSequence(pattern* patterns) | MatchMapping(expr* keys, pattern* patterns, identifier? rest) | MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns) | MatchStar(identifier? name) | MatchAs(pattern? pattern, identifier? name) | MatchOr(pattern* patterns)

## ast.slice(...)

Deprecated AST node class.

## ast.stmt(...)

stmt = FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment, type_param* type_params) | AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment, type_param* type_params) | ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list, type_param* type_params) | Return(expr? value) | Delete(expr* targets) | Assign(expr* targets, expr value, string? type_comment) | TypeAlias(expr name, type_param* type_params, expr value) | AugAssign(expr target, operator op, expr value) | AnnAssign(expr target, expr annotation, expr? value, int simple) | For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment) | AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment) | While(expr test, stmt* body, stmt* orelse) | If(expr test, stmt* body, stmt* orelse) | With(withitem* items, stmt* body, string? type_comment) | AsyncWith(withitem* items, stmt* body, string? type_comment) | Match(expr subject, match_case* cases) | Raise(expr? exc, expr? cause) | Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody) | TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody) | Assert(expr test, expr? msg) | Import(alias* names) | ImportFrom(identifier? module, alias* names, int? level) | Global(identifier* names) | Nonlocal(identifier* names) | Expr(expr value) | Pass | Break | Continue

## ast.type_ignore(...)

type_ignore = TypeIgnore(int lineno, string tag)

## ast.type_param(...)

type_param = TypeVar(identifier name, expr? bound, expr? default_value) | ParamSpec(identifier name, expr? default_value) | TypeVarTuple(identifier name, expr? default_value)

## ast.unaryop(...)

unaryop = Invert | Not | UAdd | USub

## ast.walk(node)

Recursively yield all descendant nodes in the tree starting at *node* (including *node* itself), in no specified order. This is useful if you only want to modify nodes in place and don't care about the context.

## ast.withitem(...)

withitem(expr context_expr, expr? optional_vars)
