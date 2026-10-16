# shelve

## shelve.BsdDbShelf(dict, protocol=None, writeback=False, keyencoding='utf-8')

This adds methods first(), next(), previous(), last() and
set_location() that have no counterpart in [g]dbm databases.

The actual database must be opened using one of the "bsddb"
modules "open" routines (i.e. bsddb.hashopen, bsddb.btopen or
bsddb.rnopen) and passed to the constructor.

See the module's __doc__ string for an overview of the interface.

## shelve.DbfilenameShelf(filename, flag='c', protocol=None, writeback=False)

Shelf implementation using the "dbm" generic dbm interface. This is initialized with the filename for the dbm database.
See the module's __doc__ string for an overview of the interface.

## shelve.DbfilenameShelf.clear(self)

Remove all items from the shelf.

## shelve.Shelf(dict, protocol=None, writeback=False, keyencoding='utf-8')

Base class for shelf implementations. This is initialized with a dictionary-like object.
See the module's __doc__ string for an overview of the interface.

## shelve.open(filename, flag='c', protocol=None, writeback=False)

The filename parameter is the base filename for the underlying
database.  As a side-effect, an extension may be added to the
filename and more than one file may be created.  The optional flag
parameter has the same interpretation as the flag parameter of
dbm.open(). The optional protocol parameter specifies the
version of the pickle protocol.

See the module's __doc__ string for an overview of the interface.
