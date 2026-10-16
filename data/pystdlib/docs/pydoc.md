# pydoc

## pydoc.Doc.docclass(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.docdata(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.docmodule(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.docother(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.docproperty(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.docroutine(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.document(self, object, name=None, *args)

Generate documentation for an object.

## pydoc.Doc.fail(self, object, name=None, *args)

Raise an exception for unimplemented types.

## pydoc.Doc.getdocloc(self, object, basedir='/usr/lib/python3.13')

Return the location of module docs or None

## pydoc.ErrorDuringImport(filename, exc_info)

Errors that occurred while trying to import something to document it.

## pydoc.HTMLDoc()

Formatter class for HTML documentation.

## pydoc.HTMLDoc.bigsection(self, title, *args)

Format a section with a big heading.

## pydoc.HTMLDoc.classlink(self, object, modname)

Make a link for a class.

## pydoc.HTMLDoc.docclass(self, object, name=None, mod=None, funcs={}, classes={}, *ignored)

Produce HTML documentation for a class object.

## pydoc.HTMLDoc.docdata(self, object, name=None, mod=None, cl=None, *ignored)

Produce html documentation for a data descriptor.

## pydoc.HTMLDoc.docmodule(self, object, name=None, mod=None, *ignored)

Produce HTML documentation for a module object.

## pydoc.HTMLDoc.docother(self, object, name=None, mod=None, *ignored)

Produce HTML documentation for a data object.

## pydoc.HTMLDoc.docproperty(self, object, name=None, mod=None, cl=None, *ignored)

Produce html documentation for a data descriptor.

## pydoc.HTMLDoc.docroutine(self, object, name=None, mod=None, funcs={}, classes={}, methods={}, cl=None, homecls=None)

Produce HTML documentation for a function or method object.

## pydoc.HTMLDoc.filelink(self, url, path)

Make a link to source file.

## pydoc.HTMLDoc.formattree(self, tree, modname, parent=None)

Produce HTML for a class tree as given by inspect.getclasstree().

## pydoc.HTMLDoc.formatvalue(self, object)

Format an argument default value as text.

## pydoc.HTMLDoc.heading(self, title, extras='')

Format a page heading.

## pydoc.HTMLDoc.index(self, dir, shadowed=None)

Generate an HTML index for a directory of modules.

## pydoc.HTMLDoc.markup(self, text, escape=None, funcs={}, classes={}, methods={})

Mark up some plain text, given a context of symbols to look for. Each context dictionary maps object names to anchor names.

## pydoc.HTMLDoc.modpkglink(self, modpkginfo)

Make a link for a module or package to display in an index.

## pydoc.HTMLDoc.modulelink(self, object)

Make a link for a module.

## pydoc.HTMLDoc.multicolumn(self, list, format)

Format a list of items into a multi-column list.

## pydoc.HTMLDoc.namelink(self, name, *dicts)

Make a link for an identifier, given name-to-URL mappings.

## pydoc.HTMLDoc.page(self, title, contents)

Format an HTML page.

## pydoc.HTMLDoc.parentlink(self, object, modname)

Make a link for the enclosing class or module.

## pydoc.HTMLDoc.preformat(self, text)

Format literal preformatted text.

## pydoc.HTMLDoc.section(self, title, cls, contents, width=6, prelude='', marginalia=None, gap='&nbsp;')

Format a section with a heading.

## pydoc.HTMLRepr()

Class for safely making an HTML representation of a Python object.

## pydoc.Helper.getline(self, prompt)

Read one line, using input() when appropriate.

## pydoc.ModuleScanner()

An interruptible scanner that searches module synopses.

## pydoc.TextDoc()

Formatter class for text documentation.

## pydoc.TextDoc.bold(self, text)

Format a string in bold by overstriking.

## pydoc.TextDoc.docclass(self, object, name=None, mod=None, *ignored)

Produce text documentation for a given class object.

## pydoc.TextDoc.docdata(self, object, name=None, mod=None, cl=None, *ignored)

Produce text documentation for a data descriptor.

## pydoc.TextDoc.docmodule(self, object, name=None, mod=None, *ignored)

Produce text documentation for a given module object.

## pydoc.TextDoc.docother(self, object, name=None, mod=None, parent=None, *ignored, maxlen=None, doc=None)

Produce text documentation for a data object.

## pydoc.TextDoc.docproperty(self, object, name=None, mod=None, cl=None, *ignored)

Produce text documentation for a data descriptor.

## pydoc.TextDoc.docroutine(self, object, name=None, mod=None, cl=None, homecls=None)

Produce text documentation for a function or method object.

## pydoc.TextDoc.formattree(self, tree, modname, parent=None, prefix='')

Render in text a class tree as returned by inspect.getclasstree().

## pydoc.TextDoc.formatvalue(self, object)

Format an argument default value as text.

## pydoc.TextDoc.indent(self, text, prefix='    ')

Indent text by prepending a given prefix to each line.

## pydoc.TextDoc.section(self, title, contents)

Format a section with a given heading.

## pydoc.TextRepr()

Class for safely making a text representation of a Python object.

## pydoc.apropos(key)

Print all the one-line module summaries that contain a substring.

## pydoc.browse(port=0, *, open_browser=True, hostname='localhost')

Start the enhanced pydoc web server and open a web browser. Use port '0' to start the server on an arbitrary port.
Set open_browser to False to suppress opening a browser.

## pydoc.classify_class_attrs(object)

Wrap inspect.classify_class_attrs, with fixup for data descriptors and bound methods.

## pydoc.classname(object, modname)

Get a class name and qualify it with a module name if necessary.

## pydoc.cli()

Command-line interface (looks at sys.argv to decide what to do).

## pydoc.cram(text, maxlen)

Omit part of a string if needed to make it fit in a maximum length.

## pydoc.describe(thing)

Produce a short description of the given thing.

## pydoc.doc(thing, title='Python Library Documentation: %s', forceload=0, output=None, is_cli=False)

Display text documentation, given an object or a path to an object.

## pydoc.getdoc(object)

Get the doc string or comments for an object.

## pydoc.importfile(path)

Import a Python source file or compiled file given its path.

## pydoc.isdata(object)

Check if an object is of a type that probably means it's data.

## pydoc.ispackage(path)

Guess whether a path refers to a package directory.

## pydoc.locate(path, forceload=0)

Locate an object by name or dotted path, importing as necessary.

## pydoc.pager(text, title='')

The first time this is called, determine what kind of pager to use.

## pydoc.parentname(object, modname)

Get a name of the enclosing class (qualified it with a module name if necessary) or module.

## pydoc.pathdirs()

Convert sys.path into a list of absolute, existing, unique paths.

## pydoc.render_doc(thing, title='Python Library Documentation: %s', forceload=0, renderer=None)

Render text documentation, given an object or a path to an object.

## pydoc.replace(text, *pairs)

Do a series of global replacements on a string.

## pydoc.resolve(thing, forceload=0)

Given an object or a path to an object, get the object and its name.

## pydoc.safeimport(path, forceload=0, cache={})

If the module *is* found but an exception occurs, it's wrapped in an
ErrorDuringImport exception and reraised.  Unlike __import__, if a
package path is specified, the module at the end of the path is returned,
not the package at the beginning.  If the optional 'forceload' argument
is 1, we reload the module from disk (unless it's a dynamic extension).

## pydoc.sort_attributes(attrs, object)

Sort the attrs list in-place by _fields and then alphabetically by name

## pydoc.source_synopsis(file)

Return the one-line summary of a file object, if present

## pydoc.splitdoc(doc)

Split a doc string into a synopsis line (if any) and the rest.

## pydoc.stripid(text)

Remove the hexadecimal id from a Python object representation.

## pydoc.synopsis(filename, cache={})

Get the one-line summary out of a module file.

## pydoc.visiblename(name, all=None, obj=None)

Decide whether to show documentation on a variable.

## pydoc.writedoc(thing, forceload=0)

Write HTML documentation to a file in the current directory.

## pydoc.writedocs(dir, pkgpath='', done=None)

Write out HTML documentation for all modules in a directory tree.
