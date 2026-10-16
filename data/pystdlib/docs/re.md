# re

## re.Match()

The result of re.match() and re.search(). Match objects always have a boolean value of True.

## re.Match.end(self, group=0, /)

Return index of the end of the substring matched by group.

## re.Match.expand(self, /, template)

Return the string obtained by doing backslash substitution on the string template, as done by the sub() method.

## re.Match.group(...)

group([group1, ...]) -> str or tuple. Return subgroup(s) of the match by indices or names. For 0 returns the entire match.

## re.Match.groupdict(self, /, default=None)

Return a dictionary containing all the named subgroups of the match, keyed by the subgroup name. default
  Is used for groups that did not participate in the match.

## re.Match.groups(self, /, default=None)

Return a tuple containing all the subgroups of the match, from 1. default
  Is used for groups that did not participate in the match.

## re.Match.span(self, group=0, /)

For match object m, return the 2-tuple (m.start(group), m.end(group)).

## re.Match.start(self, group=0, /)

Return index of the start of the substring matched by group.

## re.Pattern()

Compiled regular expression object.

## re.Pattern.findall(self, /, string, pos=0, endpos=9223372036854775807)

Return a list of all non-overlapping matches of pattern in string.

## re.Pattern.finditer(self, /, string, pos=0, endpos=9223372036854775807)

Return an iterator over all non-overlapping matches for the RE pattern in string. For each match, the iterator returns a match object.

## re.Pattern.fullmatch(self, /, string, pos=0, endpos=9223372036854775807)

Matches against all of the string.

## re.Pattern.match(self, /, string, pos=0, endpos=9223372036854775807)

Matches zero or more characters at the beginning of the string.

## re.Pattern.search(self, /, string, pos=0, endpos=9223372036854775807)

Scan through string looking for a match, and return a corresponding match object instance. Return None if no position in the string matches.

## re.Pattern.split(self, /, string, maxsplit=0)

Split string by the occurrences of pattern.

## re.Pattern.sub(self, /, repl, string, count=0)

Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.

## re.Pattern.subn(self, /, repl, string, count=0)

Return the tuple (new_string, number_of_subs_made) found by replacing the leftmost non-overlapping occurrences of pattern with the replacement repl.

## re.PatternError(msg, pattern=None, pos=None)

Exception raised for invalid regular expressions. Attributes:

msg: The unformatted error message
    pattern: The regular expression pattern
    pos: The index in the pattern where compilation failed (may be None)
    lineno: The line corresponding to pos (may be None)
    colno: The column corresponding to pos (may be None)

## re.RegexFlag(*values)

An enumeration.

## re.compile(pattern, flags=0)

Compile a regular expression pattern, returning a Pattern object.

## re.error(msg, pattern=None, pos=None)

Exception raised for invalid regular expressions. Attributes:

msg: The unformatted error message
    pattern: The regular expression pattern
    pos: The index in the pattern where compilation failed (may be None)
    lineno: The line corresponding to pos (may be None)
    colno: The column corresponding to pos (may be None)

## re.escape(pattern)

Escape special characters in a string.

## re.findall(pattern, string, flags=0)

If one or more capturing groups are present in the pattern, return
a list of groups; this will be a list of tuples if the pattern
has more than one group.

Empty matches are included in the result.

## re.finditer(pattern, string, flags=0)

Return an iterator over all non-overlapping matches in the string. For each match, the iterator returns a Match object.

Empty matches are included in the result.

## re.fullmatch(pattern, string, flags=0)

Try to apply the pattern to all of the string, returning a Match object, or None if no match was found.

## re.match(pattern, string, flags=0)

Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.

## re.purge()

Clear the regular expression caches

## re.search(pattern, string, flags=0)

Scan through string looking for a match to the pattern, returning a Match object, or None if no match was found.

## re.split(pattern, string, maxsplit=0, flags=0)

If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.

## re.sub(pattern, repl, string, count=0, flags=0)

Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl. repl can be either a string or a callable; if a string, backslash escapes in it are processed. If it is a callable, it's passed the Match object and must return a replacement string to be used.

## re.subn(pattern, repl, string, count=0, flags=0)

Return a 2-tuple containing (new_string, number). new_string is the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in the source string by the replacement repl. number is the number of substitutions that were made. repl can be either a string or a callable; if a string, backslash escapes in it are processed. If it is a callable, it's passed the Match object and must return a replacement string to be used.
