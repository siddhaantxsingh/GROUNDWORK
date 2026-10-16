# signal

## signal.Handlers(*values)

An enumeration.

## signal.Sigmasks(*values)

An enumeration.

## signal.Signals(*values)

An enumeration.

## signal.getsignal(signalnum)

The return value can be:
  SIG_IGN -- if the signal is being ignored
  SIG_DFL -- if the default action for the signal is in effect
  None    -- if an unknown handler is in effect
  anything else -- the callable Python object used as a handler

## signal.pthread_sigmask(how, mask)

Fetch and/or change the signal mask of the calling thread.

## signal.signal(signalnum, handler)

The action can be SIG_DFL, SIG_IGN, or a callable Python object.
The previous action is returned.  See getsignal() for possible return
values.

*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments: the first is
the signal number, the second is the interrupted stack frame.

## signal.sigpending()

Examine pending signals. Returns a set of signal numbers that are pending for delivery to
the calling thread.

## signal.sigwait(sigset)

Wait for a signal. Suspend execution of the calling thread until the delivery of one of the
signals specified in the signal set sigset.  The function accepts the
signal and returns the signal number.

## signal.struct_siginfo(iterable=(), /)

This object may be accessed either as a tuple of
(si_signo, si_code, si_errno, si_pid, si_uid, si_status, si_band),
or via the attributes si_signo, si_code, and so on.

## signal.valid_signals()

Return a set of valid signal numbers on this platform. The signal numbers returned by this function can be safely passed to
functions like `pthread_sigmask`.
