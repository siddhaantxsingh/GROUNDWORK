# site

## site.abs_paths()

Set all module __file__ and __cached__ attributes to an absolute path

## site.addpackage(sitedir, name, known_paths)

Process a .pth file within the site-packages directory: For each line in the file, either combine it with sitedir to a path and add that to known_paths, or execute it if it starts with 'import '.

## site.addsitedir(sitedir, known_paths=None)

Add 'sitedir' argument to sys.path if missing and handle .pth files in 'sitedir'

## site.addsitepackages(known_paths, prefixes=None)

Add site-packages to sys.path

## site.addusersitepackages(known_paths)

Add a per user site-package to sys.path Each user has its own python directory with site-packages in the
home directory.

## site.check_enableusersite()

The function tests for the command line flag (including environment var),
process uid/gid equal to effective uid/gid.

None: Disabled for security reasons
False: Disabled by user (command line option)
True: Safe and enabled

## site.enablerlcompleter()

Enable default readline configuration on interactive prompts, by registering a sys.__interactivehook__.

## site.execsitecustomize()

Run custom site specific code, if available.

## site.execusercustomize()

Run custom user specific code, if available.

## site.gethistoryfile()

Check if the PYTHON_HISTORY environment variable is set and define it as the .python_history file. If PYTHON_HISTORY is not set, use the default .python_history file.

## site.getsitepackages(prefixes=None)

For each directory present in ``prefixes`` (or the global ``PREFIXES``),
this function will find its `site-packages` subdirectory depending on the
system environment, and will return a list of full paths.

## site.getuserbase()

The `user base` directory can be used to store data. If the global
variable ``USER_BASE`` is not initialized yet, this function will also set
it.

## site.getusersitepackages()

Returns the user-specific site-packages directory path. If the global variable ``USER_SITE`` is not initialized yet, this
function will also set it.

## site.main()

Add standard site-specific directories to the module search path. This function is called automatically when this module is imported,
unless the python interpreter was started with the -S flag.

## site.register_readline()

If the readline module can be imported, the hook will set the Tab key
as completion key and register ~/.python_history as history file.
This can be overridden in the sitecustomize or usercustomize module,
or in a PYTHONSTARTUP file.

## site.removeduppaths()

Remove duplicate entries from sys.path along with making them absolute

## site.setcopyright()

Set 'copyright' and 'credits' in builtins

## site.setquit()

Define new builtins 'quit' and 'exit'. These are objects which make the interpreter exit when called.
The repr of each object contains a hint at how it works.
