# getpass

## getpass.getpass(prompt='Password: ', stream=None)

Prompt for a password, with echo turned off. Args:
  prompt: Written on stream to ask for the input.  Default: 'Password: '
  stream: A writable file object to display the prompt.  Defaults to
          the tty.  If no tty is available defaults to sys.stderr.
Returns:
  The seKr3t input.
Raises:
  EOFError: If our input tty or stdin was closed.
  GetPassWarning: When we were unable to turn echo off on the input.

Always restores terminal settings before returning.

## getpass.getuser()

First try various environment variables, then the password
database.  This works on Windows as long as USERNAME is set.
Any failure to find a username raises OSError.

.. versionchanged:: 3.13
    Previously, various exceptions beyond just :exc:`OSError`
    were raised.

## getpass.unix_getpass(prompt='Password: ', stream=None)

Prompt for a password, with echo turned off. Args:
  prompt: Written on stream to ask for the input.  Default: 'Password: '
  stream: A writable file object to display the prompt.  Defaults to
          the tty.  If no tty is available defaults to sys.stderr.
Returns:
  The seKr3t input.
Raises:
  EOFError: If our input tty or stdin was closed.
  GetPassWarning: When we were unable to turn echo off on the input.

Always restores terminal settings before returning.

## getpass.win_getpass(prompt='Password: ', stream=None)

Prompt for password with echo off, using Windows getwch().
