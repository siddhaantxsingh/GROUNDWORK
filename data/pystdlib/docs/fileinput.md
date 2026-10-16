# fileinput

## fileinput.FileInput(files=None, inplace=False, backup='', *, mode='r', openhook=None, encoding=None, errors=None)

In addition it has a readline() method which returns the next input line, and a __getitem__() method which implements the sequence behavior. The sequence must be accessed in strictly sequential order; random access and readline() cannot be mixed.

## fileinput.close()

Close the sequence.

## fileinput.filelineno()

Before the first line has been read, returns 0. After the last line of the last file has been read, returns the line number of that line within the file.

## fileinput.filename()

Return the name of the file currently being read. Before the first line has been read, returns None.

## fileinput.fileno()

Return the file number of the current file. When no file is currently opened, returns -1.

## fileinput.input(files=None, inplace=False, backup='', *, mode='r', openhook=None, encoding=None, errors=None)

The parameters are passed to the constructor of the FileInput class.
The returned instance, in addition to being an iterator,
keeps global state for the functions of this module,.

## fileinput.isfirstline()

Returns true the line just read is the first line of its file, otherwise returns false.

## fileinput.isstdin()

Returns true if the last line was read from sys.stdin, otherwise returns false.

## fileinput.lineno()

Before the first line has been read, returns 0. After the last line of the last file has been read, returns the line number of that line.

## fileinput.nextfile()

The filename is not changed until after the first line of the next file has been read. Before the first line has been read, this function has no effect; it cannot be used to skip the first file. After the last line of the last file has been read, this function has no effect.
