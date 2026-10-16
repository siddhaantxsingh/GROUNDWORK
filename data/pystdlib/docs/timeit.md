# timeit

## timeit.Timer(stmt='pass', setup='pass', timer=<built-in function perf_counter>, globals=None)

The constructor takes a statement to be timed, an additional
statement used for setup, and a timer function.  Both statements
default to 'pass'; the timer function is platform-dependent (see
module doc string).  If 'globals' is specified, the code will be
executed within that namespace (as opposed to inside timeit's
namespace).

To measure the execution time of the first statement, use the
timeit() method.  The repeat() method is a convenience to call
timeit() multiple times and return a list of results.

The statements may contain newlines, as long as they don't contain
multi-line string literals.

## timeit.Timer.autorange(self, callback=None)

Calls the timeit method with increasing numbers from the sequence
1, 2, 5, 10, 20, 50, ... until the time taken is at least 0.2
second.  Returns (number, time_taken).

If *callback* is given and is not None, it will be called after
each trial with two arguments: ``callback(number, time_taken)``.

## timeit.Timer.print_exc(self, file=None)

Typical use:

t = Timer(...)       # outside the try/except
    try:
        t.timeit(...)    # or t.repeat(...)
    except:
        t.print_exc()

The advantage over the standard traceback is that source lines
in the compiled template will be displayed.

The optional file argument directs where the traceback is
sent; it defaults to sys.stderr.

## timeit.Timer.repeat(self, repeat=5, number=1000000)

Call timeit() a few times. This is a convenience function that calls the timeit()
repeatedly, returning a list of results.  The first argument
specifies how many times to call timeit(), defaulting to 5;
the second argument specifies the timer argument, defaulting
to one million.

Note: it's tempting to calculate mean and standard deviation
from the result vector and report these.  However, this is not
very useful.  In a typical case, the lowest value gives a
lower bound for how fast your machine can run the given code
snippet; higher values in the result vector are typically not
caused by variability in Python's speed, but by other
processes interfering with your timing accuracy.  So the min()
of the result is probably the only number you should be
interested in.  After that, you should look at the entire
vector and apply common sense rather than statistics.

## timeit.Timer.timeit(self, number=1000000)

To be precise, this executes the setup statement once, and
then returns the time it takes to execute the main statement
a number of times, as float seconds if using the default timer.   The
argument is the number of times through the loop, defaulting
to one million.  The main statement, the setup statement and
the timer function to be used are passed to the constructor.

## timeit.main(args=None, *, _wrap_timer=None)

The optional 'args' argument specifies the command line to be parsed,
defaulting to sys.argv[1:].

The return value is an exit code to be passed to sys.exit(); it
may be None to indicate success.

When an exception happens during timing, a traceback is printed to
stderr and the return value is 1.  Exceptions at other times
(including the template compilation) are not caught.

'_wrap_timer' is an internal interface used for unit testing.  If it
is not None, it must be a callable that accepts a timer function
and returns another timer function (used for unit testing).

## timeit.reindent(src, indent)

Helper to reindent a multi-line statement.

## timeit.repeat(stmt='pass', setup='pass', timer=<built-in function perf_counter>, repeat=5, number=1000000, globals=None)

Convenience function to create Timer object and call repeat method.

## timeit.timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)

Convenience function to create Timer object and call timeit method.
