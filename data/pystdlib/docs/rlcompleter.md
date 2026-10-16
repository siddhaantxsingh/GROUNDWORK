# rlcompleter

## rlcompleter.Completer.attr_matches(self, text)

Assuming the text is of the form NAME.NAME....[NAME], and is
evaluable in self.namespace, it will be evaluated and its attributes
(as revealed by dir()) are used as possible completions.  (For class
instances, class members are also considered.)

WARNING: this can still invoke arbitrary C code, if an object
with a __getattr__ hook is evaluated.

## rlcompleter.Completer.complete(self, text, state)

Return the next possible completion for 'text'. This is called successively with state == 0, 1, 2, ... until it
returns None.  The completion should begin with 'text'.

## rlcompleter.Completer.global_matches(self, text)

Compute matches when text is a simple name. Return a list of all keywords, built-in functions and names currently
defined in self.namespace that match.
