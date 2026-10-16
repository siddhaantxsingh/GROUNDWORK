# datetime

## datetime.date(...)

date(year, month, day) --> date object

## datetime.date.ctime(self, /)

Return ctime() style string.

## datetime.date.fromisocalendar(...)

int, int, int -> Construct a date from the ISO year, week number and weekday. This is the inverse of the date.isocalendar() function

## datetime.date.fromisoformat(type, object, /)

str -> Construct a date from a string in ISO 8601 format.

## datetime.date.fromordinal(...)

int -> date corresponding to a proleptic Gregorian ordinal.

## datetime.date.fromtimestamp(type, timestamp, /)

Create a date from a POSIX timestamp. The timestamp is a number, e.g. created via time.time(), that is
interpreted as local time.

## datetime.date.isocalendar(self, /)

Return a named tuple containing ISO year, week number, and weekday.

## datetime.date.isoformat(self, /)

Return string in ISO 8601 format, YYYY-MM-DD.

## datetime.date.isoweekday(self, /)

Return the day of the week represented by the date. Monday == 1 ... Sunday == 7

## datetime.date.replace(...)

Return date with new specified fields.

## datetime.date.strftime(...)

format -> strftime() style string.

## datetime.date.timetuple(self, /)

Return time tuple, compatible with time.localtime().

## datetime.date.today(type, /)

Current date or datetime: same as self.__class__.fromtimestamp(time.time()).

## datetime.date.toordinal(self, /)

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

## datetime.date.weekday(self, /)

Return the day of the week represented by the date. Monday == 0 ... Sunday == 6

## datetime.datetime(...)

The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

## datetime.datetime.astimezone(...)

tz -> convert to local time in new timezone tz

## datetime.datetime.combine(...)

date, time -> datetime with same date and time fields

## datetime.datetime.ctime(self, /)

Return ctime() style string.

## datetime.datetime.date(self, /)

Return date object with same year, month and day.

## datetime.datetime.dst(self, /)

Return self.tzinfo.dst(self).

## datetime.datetime.fromisoformat(type, object, /)

string -> datetime from a string in most ISO 8601 formats

## datetime.datetime.fromtimestamp(...)

timestamp[, tz] -> tz's local time from POSIX timestamp.

## datetime.datetime.isoformat(...)

The optional argument timespec specifies the number of additional terms of the time to include. Valid options are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds' and 'microseconds'.

## datetime.datetime.now(type, /, tz=None)

Returns new datetime object representing current time local to tz. tz
    Timezone object.

If no tz is specified, uses local timezone.

## datetime.datetime.replace(...)

Return datetime with new specified fields.

## datetime.datetime.strptime(...)

string, format -> new datetime parsed from a string (like time.strptime()).

## datetime.datetime.time(self, /)

Return time object with same time but with tzinfo=None.

## datetime.datetime.timestamp(self, /)

Return POSIX timestamp as float.

## datetime.datetime.timetuple(self, /)

Return time tuple, compatible with time.localtime().

## datetime.datetime.timetz(self, /)

Return time object with same time and tzinfo.

## datetime.datetime.tzname(self, /)

Return self.tzinfo.tzname(self).

## datetime.datetime.utcfromtimestamp(...)

Construct a naive UTC datetime from a POSIX timestamp.

## datetime.datetime.utcnow(type, /)

Return a new datetime representing UTC day and time.

## datetime.datetime.utcoffset(self, /)

Return self.tzinfo.utcoffset(self).

## datetime.datetime.utctimetuple(self, /)

Return UTC time tuple, compatible with time.localtime().

## datetime.time(...)

time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object All arguments are optional. tzinfo may be None, or an instance of
a tzinfo subclass. The remaining arguments may be ints.

## datetime.time.dst(self, /)

Return self.tzinfo.dst(self).

## datetime.time.fromisoformat(type, object, /)

string -> time from a string in ISO 8601 format

## datetime.time.isoformat(...)

The optional argument timespec specifies the number of additional terms
of the time to include. Valid options are 'auto', 'hours', 'minutes',
'seconds', 'milliseconds' and 'microseconds'.

## datetime.time.replace(...)

Return time with new specified fields.

## datetime.time.strftime(...)

format -> strftime() style string.

## datetime.time.tzname(self, /)

Return self.tzinfo.tzname(self).

## datetime.time.utcoffset(self, /)

Return self.tzinfo.utcoffset(self).

## datetime.timedelta(...)

Difference between two datetime values. timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.

## datetime.timedelta.total_seconds(self, /)

Total seconds in the duration.

## datetime.timezone(...)

Fixed offset from UTC implementation of tzinfo.

## datetime.timezone.dst(self, object, /)

Return None.

## datetime.timezone.fromutc(self, object, /)

datetime in UTC -> datetime in local time.

## datetime.timezone.tzname(self, object, /)

If name is specified when timezone is created, returns the name. Otherwise returns offset as 'UTC(+|-)HH:MM'.

## datetime.timezone.utcoffset(self, object, /)

Return fixed offset.

## datetime.tzinfo(...)

Abstract base class for time zone info objects.

## datetime.tzinfo.dst(self, object, /)

datetime -> DST offset as timedelta positive east of UTC.

## datetime.tzinfo.fromutc(self, object, /)

datetime in UTC -> datetime in local time.

## datetime.tzinfo.tzname(self, object, /)

datetime -> string name of time zone.

## datetime.tzinfo.utcoffset(self, object, /)

datetime -> timedelta showing offset from UTC, negative values indicating West of UTC
