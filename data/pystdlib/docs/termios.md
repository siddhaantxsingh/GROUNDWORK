# termios

## termios.tcdrain(fd, /)

Wait until all output written to file descriptor fd has been transmitted.

## termios.tcflow(fd, action, /)

Suspend or resume input or output on file descriptor fd. The action argument can be termios.TCOOFF to suspend output,
termios.TCOON to restart output, termios.TCIOFF to suspend input,
or termios.TCION to restart input.

## termios.tcflush(fd, queue, /)

Discard queued data on file descriptor fd. The queue selector specifies which queue: termios.TCIFLUSH for the input
queue, termios.TCOFLUSH for the output queue, or termios.TCIOFLUSH for
both queues.

## termios.tcgetattr(fd, /)

Returns a list [iflag, oflag, cflag, lflag, ispeed, ospeed, cc]
where cc is a list of the tty special characters (each a string of
length 1, except the items with indices VMIN and VTIME, which are
integers when these fields are defined).  The interpretation of the
flags and the speeds as well as the indexing in the cc array must be
done using the symbolic constants defined in this module.

## termios.tcgetwinsize(fd, /)

Get the tty winsize for file descriptor fd. Returns a tuple (ws_row, ws_col).

## termios.tcsendbreak(fd, duration, /)

Send a break on file descriptor fd. A zero duration sends a break for 0.25-0.5 seconds; a nonzero duration
has a system dependent meaning.

## termios.tcsetattr(fd, when, attributes, /)

The attributes to be set are taken from the attributes argument, which
is a list like the one returned by tcgetattr(). The when argument
determines when the attributes are changed: termios.TCSANOW to
change immediately, termios.TCSADRAIN to change after transmitting all
queued output, or termios.TCSAFLUSH to change after transmitting all
queued output and discarding all queued input.

## termios.tcsetwinsize(fd, winsize, /)

Set the tty winsize for file descriptor fd. The winsize to be set is taken from the winsize argument, which
is a two-item tuple (ws_row, ws_col) like the one returned by
tcgetwinsize().
