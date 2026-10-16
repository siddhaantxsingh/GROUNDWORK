# platform

## platform.AndroidVer(release, api_level, manufacturer, model, device, is_emulator)

AndroidVer(release, api_level, manufacturer, model, device, is_emulator)

## platform.IOSVersionInfo(system, release, model, is_simulator)

IOSVersionInfo(system, release, model, is_simulator)

## platform.architecture(executable='/usr/bin/python3', bits='', linkage='')

Returns a tuple (bits, linkage) which contains information about
the bit architecture and the linkage format used for the
executable. Both values are returned as strings.

Values that cannot be determined are returned as given by the
parameter presets. If bits is given as '', the sizeof(pointer)
(or sizeof(long) on Python version < 1.5.2) is used as
indicator for the supported pointer size.

The function relies on the system's "file" command to do the
actual work. This is available on most if not all Unix
platforms. On some non-Unix platforms where the "file" command
does not exist and the executable is set to the Python interpreter
binary defaults from _default_architecture are used.

## platform.freedesktop_os_release()

Return operation system identification from freedesktop.org os-release

## platform.ios_ver(system='', release='', model='', is_simulator=False)

Get iOS version information, and return it as a namedtuple: (system, release, model, is_simulator). If values can't be determined, they are set to values provided as
parameters.

## platform.java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))

Version interface for Jython. Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
tuple (os_name, os_version, os_arch).

Values which cannot be determined are set to the defaults
given as parameters (which all default to '').

## platform.libc_ver(executable=None, lib='', version='', chunksize=16384)

Returns a tuple of strings (lib,version) which default to the
given parameters in case the lookup fails.

Note that the function has intimate knowledge of how different
libc versions add symbols to the executable and thus is probably
only usable for executables compiled using gcc.

The file is read and scanned in chunks of chunksize bytes.

## platform.mac_ver(release='', versioninfo=('', '', ''), machine='')

Get macOS version information and return it as tuple (release, versioninfo, machine) with versioninfo being a tuple (version, dev_stage, non_release_version). Entries which cannot be determined are set to the parameter values
which default to ''. All tuple entries are strings.

## platform.machine()

Returns the machine type, e.g. 'i386'

An empty string is returned if the value cannot be determined.

## platform.node()

Returns the computer's network name (which may not be fully qualified) An empty string is returned if the value cannot be determined.

## platform.platform(aliased=False, terse=False)

The output is intended to be human readable rather than
machine parseable. It may look different on different
platforms and this is intended.

If "aliased" is true, the function will use aliases for
various platforms that report system names which differ from
their common names, e.g. SunOS will be reported as
Solaris. The system_alias() function is used to implement
this.

Setting terse to true causes the function to return only the
absolute minimum information needed to identify the platform.

## platform.processor()

'amdk6'

An empty string is returned if the value cannot be
determined. Note that many platforms do not provide this
information or simply return the same value as for machine(),
e.g.  NetBSD does this.

## platform.python_branch()

Returns a string identifying the Python implementation branch. For CPython this is the SCM branch from which the
Python binary was built.

If not available, an empty string is returned.

## platform.python_build()

Returns a tuple (buildno, builddate) stating the Python build number and date as strings.

## platform.python_compiler()

Returns a string identifying the compiler used for compiling Python.

## platform.python_implementation()

Returns a string identifying the Python implementation. Currently, the following implementations are identified:
  'CPython' (C implementation of Python),
  'Jython' (Java implementation of Python),
  'PyPy' (Python implementation of Python).

## platform.python_revision()

Returns a string identifying the Python implementation revision. For CPython this is the SCM revision from which the
Python binary was built.

If not available, an empty string is returned.

## platform.python_version()

Returns the Python version as string 'major.minor.patchlevel' Note that unlike the Python sys.version, the returned value
will always include the patchlevel (it defaults to 0).

## platform.python_version_tuple()

Returns the Python version as tuple (major, minor, patchlevel) of strings. Note that unlike the Python sys.version, the returned value
will always include the patchlevel (it defaults to 0).

## platform.release()

Returns the system's release, e.g. '2.2.0' or 'NT'

An empty string is returned if the value cannot be determined.

## platform.system()

Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

An empty string is returned if the value cannot be determined.

## platform.system_alias(system, release, version)

Returns (system, release, version) aliased to common marketing names used for some systems. It also does some reordering of the information in some cases
where it would otherwise cause confusion.

## platform.uname()

Fairly portable uname interface. Returns a tuple of strings (system, node, release, version, machine, processor) identifying the underlying platform.

Note that unlike the os.uname function this also returns
possible processor information as an additional tuple entry.

Entries which cannot be determined are set to ''.

## platform.uname_result(system, node, release, version, machine)

A uname_result that's largely compatible with a simple namedtuple except that 'processor' is resolved late and cached to avoid calling "uname" except when needed.

## platform.version()

Returns the system's release version, e.g. '#3 on degas'

An empty string is returned if the value cannot be determined.
