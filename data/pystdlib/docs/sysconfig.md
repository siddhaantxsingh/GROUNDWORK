# sysconfig

## sysconfig.expand_makefile_vars(s, vars)

Variables not present in 'vars' are silently expanded to the empty string. The variable values in 'vars' should not contain further variable expansions; if 'vars' is the output of 'parse_makefile()', you're fine. Returns a variable-expanded version of 's'.

## sysconfig.get_config_h_filename()

Return the path of pyconfig.h.

## sysconfig.get_config_var(name)

Return the value of a single variable using the dictionary returned by 'get_config_vars()'. Equivalent to get_config_vars().get(name)

## sysconfig.get_config_vars(*args)

On Unix, this means every variable defined in Python's installed Makefile;
On Windows it's a much smaller set.

With arguments, return a list of values that result from looking up
each argument in the configuration variable dictionary.

## sysconfig.get_makefile_filename()

Return the path of the Makefile.

## sysconfig.get_path(name, scheme='posix_local', vars=None, expand=True)

Return a path corresponding to the scheme. ``scheme`` is the install scheme name.

## sysconfig.get_path_names()

Return a tuple containing the paths names.

## sysconfig.get_paths(scheme='posix_local', vars=None, expand=True)

Return a mapping containing an install scheme. ``scheme`` is the install scheme name. If not provided, it will
return the default scheme for the current platform.

## sysconfig.get_platform()

This is used mainly to distinguish platform-specific build directories and
platform-specific built distributions.  Typically includes the OS name and
version and the architecture (as supplied by 'os.uname()'), although the
exact information included depends on the OS; on Linux, the kernel version
isn't particularly important.

Examples of returned values:

Windows:

- win-amd64 (64-bit Windows on AMD64, aka x86_64, Intel64, and EM64T)
- win-arm64 (64-bit Windows on ARM64, aka AArch64)
- win32 (all others - specifically, sys.platform is returned)

POSIX based OS:

- linux-x86_64
- macosx-15.5-arm64
- macosx-26.0-universal2 (macOS on Apple Silicon or Intel)
- android-24-arm64_v8a

For other non-POSIX platforms, currently just returns :data:`sys.platform`.

## sysconfig.get_scheme_names()

Return a tuple containing the schemes names.

## sysconfig.parse_config_h(fp, vars=None)

Parse a config.h-style file. A dictionary containing name/value pairs is returned.  If an
optional dictionary is passed in as the second argument, it is
used instead of a new dictionary.
