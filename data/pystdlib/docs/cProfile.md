# cProfile

## cProfile.Profile(...)

The default timer is a fast built-in one based on real time. For custom timer functions returning integers, timeunit can be a float specifying a scale (i.e. how long each integer unit is, in seconds).

## cProfile.run(statement, filename=None, sort=-1)

Run statement under profiler optionally saving results in filename This function takes a single argument that can be passed to the
"exec" statement, and an optional file name.  In all cases this
routine attempts to "exec" its first argument and gather profiling
statistics from the execution. If no file name is present, then this
function automatically prints a simple profiling report, sorted by the
standard name string (file/line/function-name) that is presented in
each line.

## cProfile.runctx(statement, globals, locals, filename=None, sort=-1)

Run statement under profiler, supplying your own globals and locals, optionally saving results in filename. statement and filename have the same semantics as profile.run
