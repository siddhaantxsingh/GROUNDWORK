# sqlite3

## sqlite3.Blob.close(self, /)

Close the blob.

## sqlite3.Blob.read(self, length=-1, /)

length
    Read length in bytes.

If the end of the blob is reached, the data up to end of file will
be returned.  When length is not specified, or is negative,
Blob.read() will read until the end of the blob.

## sqlite3.Blob.seek(self, offset, origin=0, /)

The origin argument defaults to os.SEEK_SET (absolute blob
positioning).  Other values for origin are os.SEEK_CUR (seek
relative to the current position) and os.SEEK_END (seek relative to
the blob's end).

## sqlite3.Blob.tell(self, /)

Return the current access position for the blob.

## sqlite3.Blob.write(self, data, /)

Write data at the current offset. This function cannot change the blob length.  Writing beyond the end
of the blob will result in an exception being raised.

## sqlite3.Connection(...)

SQLite database connection object.

## sqlite3.Connection.backup(self, /, target, *, pages=-1, progress=None, name='main', sleep=0.25)

Makes a backup of the database.

## sqlite3.Connection.blobopen(self, table, column, rowid, /, *, readonly=False, name='main')

Open and return a BLOB object. table
  Table name.
column
  Column name.
rowid
  Row id.
readonly
  Open the BLOB without write permissions.
name
  Database name.

## sqlite3.Connection.close(self, /)

Close the database connection. Any pending transaction is not committed implicitly.

## sqlite3.Connection.commit(self, /)

Commit any pending transaction to the database. If there is no open transaction, this method is a no-op.

## sqlite3.Connection.create_aggregate(self, /, name, n_arg, aggregate_class)

Creates a new aggregate. Note: Passing keyword arguments 'name', 'n_arg' and 'aggregate_class'
to _sqlite3.Connection.create_aggregate() is deprecated. Parameters
'name', 'n_arg' and 'aggregate_class' will become positional-only in
Python 3.15.

## sqlite3.Connection.create_collation(self, name, callback, /)

Creates a collation function.

## sqlite3.Connection.create_function(self, /, name, narg, func, *, deterministic=False)

Creates a new function. Note: Passing keyword arguments 'name', 'narg' and 'func' to
_sqlite3.Connection.create_function() is deprecated. Parameters
'name', 'narg' and 'func' will become positional-only in Python 3.15.

## sqlite3.Connection.create_window_function(self, name, num_params, aggregate_class, /)

Non-standard.

name
  The name of the SQL aggregate window function to be created or
  redefined.
num_params
  The number of arguments the step and inverse methods takes.
aggregate_class
  A class with step(), finalize(), value(), and inverse() methods.
  Set to None to clear the window function.

## sqlite3.Connection.cursor(...)

Return a cursor for the connection.

## sqlite3.Connection.deserialize(self, data, /, *, name='main')

Load a serialized database. data
    The serialized database content.
  name
    Which database to reopen with the deserialization.

The deserialize interface causes the database connection to
disconnect from the target database, and then reopen it as
an in-memory database based on the given serialized data.

The deserialize interface will fail with SQLITE_BUSY if the database
is currently in a read transaction or is involved in a backup
operation.

## sqlite3.Connection.enable_load_extension(self, enable, /)

Enable dynamic loading of SQLite extension modules.

## sqlite3.Connection.execute(self, sql, parameters=(), /)

Executes an SQL statement.

## sqlite3.Connection.executemany(self, sql, parameters, /)

Repeatedly executes an SQL statement.

## sqlite3.Connection.executescript(self, sql_script, /)

Executes multiple SQL statements at once.

## sqlite3.Connection.getconfig(self, op, /)

Query a boolean connection configuration option. op
  The configuration verb; one of the sqlite3.SQLITE_DBCONFIG codes.

## sqlite3.Connection.getlimit(self, category, /)

Get connection run-time limits. category
  The limit category to be queried.

## sqlite3.Connection.interrupt(self, /)

Abort any pending database operation.

## sqlite3.Connection.iterdump(self, /, *, filter=None)

Returns iterator to the dump of the database in an SQL text format. filter
  An optional LIKE pattern for database objects to dump

## sqlite3.Connection.load_extension(self, name, /, *, entrypoint=None)

Load SQLite extension module.

## sqlite3.Connection.rollback(self, /)

Roll back to the start of any pending transaction. If there is no open transaction, this method is a no-op.

## sqlite3.Connection.serialize(self, /, *, name='main')

name
    Which database to serialize.

For an ordinary on-disk database file, the serialization is just
a copy of the disk file.  For an in-memory database or a "temp"
database, the serialization is the same sequence of bytes which
would be written to disk if that database were backed up to disk.

## sqlite3.Connection.set_authorizer(self, /, authorizer_callback)

Set authorizer callback. Note: Passing keyword argument 'authorizer_callback' to
_sqlite3.Connection.set_authorizer() is deprecated. Parameter
'authorizer_callback' will become positional-only in Python 3.15.

## sqlite3.Connection.set_progress_handler(self, /, progress_handler, n)

Set progress handler callback. progress_handler
    A callable that takes no arguments.
    If the callable returns non-zero, the current query is
    terminated, and an exception is raised.
  n
    The number of SQLite virtual machine instructions that are
    executed between invocations of 'progress_handler'.

If 'progress_handler' is None or 'n' is 0, the progress handler is
disabled.

Note: Passing keyword argument 'progress_handler' to
_sqlite3.Connection.set_progress_handler() is deprecated. Parameter
'progress_handler' will become positional-only in Python 3.15.

## sqlite3.Connection.set_trace_callback(self, /, trace_callback)

Set a trace callback called for each SQL statement (passed as unicode). Note: Passing keyword argument 'trace_callback' to
_sqlite3.Connection.set_trace_callback() is deprecated. Parameter
'trace_callback' will become positional-only in Python 3.15.

## sqlite3.Connection.setconfig(self, op, enable=True, /)

Set a boolean connection configuration option. op
  The configuration verb; one of the sqlite3.SQLITE_DBCONFIG codes.

## sqlite3.Connection.setlimit(self, category, limit, /)

Set connection run-time limits. category
    The limit category to be set.
  limit
    The new limit. If the new limit is a negative number, the limit
    is unchanged.

Attempts to increase a limit above its hard upper bound are silently
truncated to the hard upper bound. Regardless of whether or not the
limit was changed, the prior value of the limit is returned.

## sqlite3.Cursor(...)

SQLite database cursor class.

## sqlite3.Cursor.close(self, /)

Closes the cursor.

## sqlite3.Cursor.execute(self, sql, parameters=(), /)

Executes an SQL statement.

## sqlite3.Cursor.executemany(self, sql, seq_of_parameters, /)

Repeatedly executes an SQL statement.

## sqlite3.Cursor.executescript(self, sql_script, /)

Executes multiple SQL statements at once.

## sqlite3.Cursor.fetchall(self, /)

Fetches all rows from the resultset.

## sqlite3.Cursor.fetchmany(self, /, size=1)

Fetches several rows from the resultset. size
  The default value is set by the Cursor.arraysize attribute.

## sqlite3.Cursor.fetchone(self, /)

Fetches one row from the resultset.

## sqlite3.Cursor.setinputsizes(self, sizes, /)

Required by DB-API. Does nothing in sqlite3.

## sqlite3.Cursor.setoutputsize(self, size, column=None, /)

Required by DB-API. Does nothing in sqlite3.

## sqlite3.PrepareProtocol(...)

PEP 246 style object adaption protocol type.

## sqlite3.Row.keys(self, /)

Returns the keys of the row.
