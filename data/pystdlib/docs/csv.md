# csv

## csv.Dialect()

Describe a CSV dialect. This must be subclassed (see csv.excel).  Valid attributes are:
delimiter, quotechar, escapechar, doublequote, skipinitialspace,
lineterminator, quoting.

## csv.Sniffer()

"Sniffs" the format of a CSV file (i.e. delimiter, quotechar) Returns a Dialect object.

## csv.Sniffer.sniff(self, sample, delimiters=None)

If several delimiters fit the sample equally well, the
delimiters listed in the preferred attribute are preferred, in
that order, no matter how many times each of them occurs.

## csv.excel()

Describe the usual properties of Excel-generated CSV files.

## csv.excel_tab()

Describe the usual properties of Excel-generated TAB-delimited files.

## csv.unix_dialect()

Describe the usual properties of Unix-generated CSV files.
