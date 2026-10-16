# pstats

## pstats.FunctionProfile(ncalls: str, tottime: float, percall_tottime: float, cumtime: float, percall_cumtime: float, file_name: str, line_number: int) -> None

FunctionProfile(ncalls: str, tottime: float, percall_tottime: float, cumtime: float, percall_cumtime: float, file_name: str, line_number: int)

## pstats.SortKey(*values)

An enumeration.

## pstats.Stats(*args, stream=None)

It is a "friend" of that class, and imports data either by direct access to members of Profile class, or by reading in a dictionary that was emitted (via marshal) from the Profile class.

The big change from the previous Profiler (in terms of raw functionality)
is that an "add()" method has been provided to combine Stats from
several distinct profile runs.  Both the constructor and the add()
method now take arbitrarily many file names as arguments.

All the print methods now take an argument that indicates how many lines
to print.  If the arg is a floating-point number between 0 and 1.0, then
it is taken as a decimal percentage of the available lines to be printed
(e.g., .1 means print 10% of all available lines).  If it is an integer,
it is taken to mean the number of lines of data that you wish to have
printed.

The sort_stats() method now processes some additional options (i.e., in
addition to the old -1, 0, 1, or 2 that are respectively interpreted as
'stdname', 'calls', 'time', and 'cumulative').  It takes either an
arbitrary number of quoted strings or SortKey enum to select the sort
order.

For example sort_stats('time', 'name') or sort_stats(SortKey.TIME,
SortKey.NAME) sorts on the major key of 'internal function time', and on
the minor key of 'the name of the function'.  Look at the two tables in
sort_stats() and get_sort_arg_defs(self) for more examples.

All methods return self, so you can string together commands like:
    Stats('foo', 'goo').strip_dirs().sort_stats('calls').                            print_stats(5).print_callers(5)

## pstats.Stats.dump_stats(self, filename)

Write the profile data to a file we know how to load back.

## pstats.Stats.get_sort_arg_defs(self)

Expand all abbreviations that are unique.

## pstats.Stats.get_stats_profile(self)

Each FunctionProfile instance holds information related to the function's profile such as how long the function took to run, how many times it was called, etc...

## pstats.StatsProfile(total_tt: float, func_profiles: Dict[str, pstats.FunctionProfile]) -> None

Class for keeping track of an item in inventory.

## pstats.TupleComp(comp_select_list)

Each instance records a list of tuple-indices (from most significant to least significant), and sort direction (ascending or descending) for each tuple-index. The compare functions can then be used as the function argument to the system sort() function when a list of tuples need to be sorted in the instances order.

## pstats.add_callers(target, source)

Combine two caller lists in a single list.

## pstats.add_func_stats(target, source)

Add together all the stats for two profile entries.

## pstats.count_calls(callers)

Sum the caller statistics to get total number of calls received.
