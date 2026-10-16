# calendar

## calendar.Calendar(firstweekday=0)

Base calendar class. This class doesn't do any formatting. It simply provides data to subclasses.

## calendar.Calendar.itermonthdates(self, year, month)

Return an iterator for one month. The iterator will yield datetime.date values and will always iterate through complete weeks, so it will yield dates outside the specified month.

## calendar.Calendar.itermonthdays(self, year, month)

Like itermonthdates(), but will yield day numbers. For days outside the specified month the day number is 0.

## calendar.Calendar.itermonthdays2(self, year, month)

Like itermonthdates(), but will yield (day number, weekday number) tuples. For days outside the specified month the day number is 0.

## calendar.Calendar.itermonthdays3(self, year, month)

Like itermonthdates(), but will yield (year, month, day) tuples. Can be used for dates outside of datetime.date range.

## calendar.Calendar.itermonthdays4(self, year, month)

Like itermonthdates(), but will yield (year, month, day, day_of_week) tuples. Can be used for dates outside of datetime.date range.

## calendar.Calendar.iterweekdays(self)

Return an iterator for one week of weekday numbers starting with the configured first one.

## calendar.Calendar.monthdatescalendar(self, year, month)

Return a matrix (list of lists) representing a month's calendar. Each row represents a week; week entries are datetime.date values.

## calendar.Calendar.monthdays2calendar(self, year, month)

Return a matrix representing a month's calendar. Each row represents a week; week entries are (day number, weekday number) tuples. Day numbers outside this month are zero.

## calendar.Calendar.monthdayscalendar(self, year, month)

Return a matrix representing a month's calendar. Each row represents a week; days outside this month are zero.

## calendar.Calendar.yeardatescalendar(self, year, width=3)

The return value is a list of month rows. Each month row contains up to width months. Each month contains between 4 and 6 weeks and each week contains 1-7 days. Days are datetime.date objects.

## calendar.Calendar.yeardays2calendar(self, year, width=3)

Return the data for the specified year ready for formatting (similar to yeardatescalendar()). Entries in the week lists are (day number, weekday number) tuples. Day numbers outside this month are zero.

## calendar.Calendar.yeardayscalendar(self, year, width=3)

Return the data for the specified year ready for formatting (similar to yeardatescalendar()). Entries in the week lists are day numbers. Day numbers outside this month are zero.

## calendar.HTMLCalendar(firstweekday=0)

This calendar returns complete HTML pages.

## calendar.HTMLCalendar.formatday(self, day, weekday)

Return a day as a table cell.

## calendar.HTMLCalendar.formatmonth(self, theyear, themonth, withyear=True)

Return a formatted month as a table.

## calendar.HTMLCalendar.formatmonthname(self, theyear, themonth, withyear=True)

Return a month name as a table row.

## calendar.HTMLCalendar.formatweek(self, theweek)

Return a complete week as a table row.

## calendar.HTMLCalendar.formatweekday(self, day)

Return a weekday name as a table header.

## calendar.HTMLCalendar.formatweekheader(self)

Return a header for a week as a table row.

## calendar.HTMLCalendar.formatyear(self, theyear, width=3)

Return a formatted year as a table of tables.

## calendar.HTMLCalendar.formatyearpage(self, theyear, width=3, css='calendar.css', encoding=None)

Return a formatted year as a complete HTML page.

## calendar.LocaleHTMLCalendar(firstweekday=0, locale=None)

This class can be passed a locale name in the constructor and will return month and weekday names in the specified locale.

## calendar.LocaleTextCalendar(firstweekday=0, locale=None)

This class can be passed a locale name in the constructor and will return month and weekday names in the specified locale.

## calendar.TextCalendar(firstweekday=0)

Subclass of Calendar that outputs a calendar as a simple plain text similar to the UNIX program cal.

## calendar.TextCalendar.formatday(self, day, weekday, width)

Returns a formatted day.

## calendar.TextCalendar.formatmonth(self, theyear, themonth, w=0, l=0)

Return a month's calendar string (multi-line).

## calendar.TextCalendar.formatmonthname(self, theyear, themonth, width, withyear=True)

Return a formatted month name.

## calendar.TextCalendar.formatweek(self, theweek, width)

Returns a single week in a string (no newline).

## calendar.TextCalendar.formatweekday(self, day, width)

Returns a formatted week day name.

## calendar.TextCalendar.formatweekheader(self, width)

Return a header for a week.

## calendar.TextCalendar.formatyear(self, theyear, w=2, l=1, c=6, m=3)

Returns a year's calendar as a multi-line string.

## calendar.TextCalendar.prmonth(self, theyear, themonth, w=0, l=0)

Print a month's calendar.

## calendar.TextCalendar.prweek(self, theweek, width)

Print a single week (no newline).

## calendar.TextCalendar.pryear(self, theyear, w=0, l=0, c=6, m=3)

Print a year's calendar.

## calendar.format(cols, colwidth=20, spacing=6)

Prints multi-column formatting for year calendars

## calendar.formatstring(cols, colwidth=20, spacing=6)

Returns a string formatted from n strings, centered within n columns.

## calendar.isleap(year)

Return True for leap years, False for non-leap years.

## calendar.leapdays(y1, y2)

Return number of leap years in range [y1, y2). Assume y1 <= y2.

## calendar.monthrange(year, month)

Return weekday of first day of month (0-6 ~ Mon-Sun) and number of days (28-31) for year, month.

## calendar.timegm(tuple)

Unrelated but handy function to calculate Unix timestamp from GMT.

## calendar.weekday(year, month, day)

Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31).
