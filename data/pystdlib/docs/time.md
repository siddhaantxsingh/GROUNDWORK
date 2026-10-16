# time

## time.asctime(...)

Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'. When the time tuple is not present, current time as returned by localtime() is used.

## time.clock_getres(...)

Return the resolution (precision) of the specified clock clk_id.

## time.clock_gettime(clk_id, /)

Return the time of the specified clock clk_id as a float.

## time.clock_gettime_ns(clk_id, /)

Return the time of the specified clock clk_id as nanoseconds (int).

## time.clock_settime(...)

Set the time of the specified clock clk_id.

## time.clock_settime_ns(...)

Set the time of the specified clock clk_id with nanoseconds.

## time.ctime(...)

Convert a time in seconds since the Epoch to a string in local time. This is equivalent to asctime(localtime(seconds)). When 'seconds' is not passed in, convert the current time instead.

## time.get_clock_info(...)

Get information of the specified clock.

## time.gmtime(...)

GMT). When 'seconds' is not passed in, convert the current time instead.

If the platform supports the tm_gmtoff and tm_zone, they are available as
attributes only.

## time.localtime(...)

Convert seconds since the Epoch to a time tuple expressing local time. When 'seconds' is not passed in, convert the current time instead.

## time.mktime(object, /)

Note that mktime(gmtime(0)) will not generally return zero for most time zones; instead the returned value will either be equal to that of the timezone or altzone attributes on the time module.

## time.monotonic()

Monotonic clock, cannot go backward.

## time.monotonic_ns()

Monotonic clock, cannot go backward, as nanoseconds.

## time.perf_counter()

Performance counter for benchmarking.

## time.perf_counter_ns()

Performance counter for benchmarking as nanoseconds.

## time.process_time()

Process time for profiling: sum of the kernel and user-space CPU time.

## time.process_time_ns()

Process time for profiling as nanoseconds: sum of the kernel and user-space CPU time.

## time.pthread_getcpuclockid(...)

Return the clk_id of a thread's CPU time clock.

## time.sleep(object, /)

Delay execution for a given number of seconds. The argument may be a floating-point number for subsecond precision.

## time.strftime(...)

See the library reference manual for formatting codes. When the time tuple is not present, current time as returned by localtime() is used.

Commonly used format codes:

%Y  Year with century as a decimal number.
%m  Month as a decimal number [01,12].
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%M  Minute as a decimal number [00,59].
%S  Second as a decimal number [00,61].
%z  Time zone offset from UTC.
%a  Locale's abbreviated weekday name.
%A  Locale's full weekday name.
%b  Locale's abbreviated month name.
%B  Locale's full month name.
%c  Locale's appropriate date and time representation.
%I  Hour (12-hour clock) as a decimal number [01,12].
%p  Locale's equivalent of either AM or PM.

Other codes may be available on your platform.  See documentation for
the C library strftime function.

## time.strptime(...)

See the library reference manual for formatting codes (same as strftime()).

Commonly used format codes:

%Y  Year with century as a decimal number.
%m  Month as a decimal number [01,12].
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%M  Minute as a decimal number [00,59].
%S  Second as a decimal number [00,61].
%z  Time zone offset from UTC.
%a  Locale's abbreviated weekday name.
%A  Locale's full weekday name.
%b  Locale's abbreviated month name.
%B  Locale's full month name.
%c  Locale's appropriate date and time representation.
%I  Hour (12-hour clock) as a decimal number [01,12].
%p  Locale's equivalent of either AM or PM.

Other codes may be available on your platform.  See documentation for
the C library strftime function.

## time.struct_time(iterable=(), /)

May be considered as a sequence of 9 integers.

Note that several fields' values are not the same as those defined by
the C language standard for struct tm.  For example, the value of the
field tm_year is the actual year, not year - 1900.  See individual
fields' descriptions for details.

## time.thread_time()

Thread time for profiling: sum of the kernel and user-space CPU time.

## time.thread_time_ns()

Thread time for profiling as nanoseconds: sum of the kernel and user-space CPU time.

## time.time()

Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them.

## time.time_ns()

Return the current time in nanoseconds since the Epoch.

## time.tzset()

The TZ environment variable should be specified in standard Unix timezone format as documented in the tzset man page (eg. 'US/Eastern', 'Europe/Amsterdam'). Unknown timezones will silently fall back to UTC. If the TZ environment variable is not set, the local timezone is set to the systems best guess of wallclock time. Changing the TZ environment variable without calling tzset *may* change the local timezone used by methods such as localtime, but this behaviour should not be relied on.
