# readline

## readline.add_history(string, /)

Add an item to the history buffer.

## readline.append_history_file(nelements, filename=None, /)

Append the last nelements items of the history list to file. The default filename is ~/.history.

## readline.clear_history()

Clear the current readline history.

## readline.get_begidx()

Get the beginning index of the completion scope.

## readline.get_completer()

Get the current completer function.

## readline.get_completer_delims()

Get the word delimiters for completion.

## readline.get_completion_type()

Get the type of completion being attempted.

## readline.get_current_history_length()

Return the current (not the maximum) length of history.

## readline.get_endidx()

Get the ending index of the completion scope.

## readline.get_history_item(index, /)

Return the current contents of history item at one-based index.

## readline.get_history_length()

Return the maximum number of lines that will be written to the history file.

## readline.get_line_buffer()

Return the current contents of the line buffer.

## readline.insert_text(string, /)

Insert text into the line buffer at the cursor position.

## readline.parse_and_bind(string, /)

Execute the init line provided in the string argument.

## readline.read_history_file(filename=None, /)

Load a readline history file. The default filename is ~/.history.

## readline.read_init_file(filename=None, /)

Execute a readline initialization file. The default filename is the last filename used.

## readline.redisplay()

Change what's displayed on the screen to reflect contents of the line buffer.

## readline.remove_history_item(pos, /)

Remove history item given by its zero-based position.

## readline.replace_history_item(pos, line, /)

Replaces history item given by its position with contents of line. pos is zero-based.

## readline.set_auto_history(enabled, /)

Enables or disables automatic history.

## readline.set_completer(function=None, /)

The function is called as function(text, state),
for state in 0, 1, 2, ..., until it returns a non-string.
It should return the next possible completion starting with 'text'.

## readline.set_completer_delims(string, /)

Set the word delimiters for completion.

## readline.set_completion_display_matches_hook(function=None, /)

Set or remove the completion display function. The function is called as
  function(substitution, [matches], longest_match_length)
once each time matches need to be displayed.

## readline.set_history_length(length, /)

Set the maximal number of lines which will be written to the history file. A negative length is used to inhibit history truncation.

## readline.set_pre_input_hook(function=None, /)

Set or remove the function invoked by the rl_pre_input_hook callback. The function is called with no arguments after the first prompt
has been printed and just before readline starts reading input
characters.

## readline.set_startup_hook(function=None, /)

Set or remove the function invoked by the rl_startup_hook callback. The function is called with no arguments just
before readline prints the first prompt.

## readline.write_history_file(filename=None, /)

Save a readline history file. The default filename is ~/.history.
