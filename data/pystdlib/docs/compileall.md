# compileall

## compileall.compile_dir(dir, maxlevels=None, ddir=None, force=False, rx=None, quiet=0, legacy=False, optimize=-1, workers=1, invalidation_mode=None, *, stripdir=None, prependdir=None, limit_sl_dest=None, hardlink_dupes=False)

Arguments (only dir is required):

dir:       the directory to byte-compile
maxlevels: maximum recursion level (default `sys.getrecursionlimit()`)
ddir:      the directory that will be prepended to the path to the
           file as it is compiled into each byte-code file.
force:     if True, force compilation, even if timestamps are up-to-date
quiet:     full output with False or 0, errors only with 1,
           no output with 2
legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
optimize:  int or list of optimization levels or -1 for level of
           the interpreter. Multiple levels leads to multiple compiled
           files each with one optimization level.
workers:   maximum number of parallel workers
invalidation_mode: how the up-to-dateness of the pyc will be checked
stripdir:  part of path to left-strip from source file path
prependdir: path to prepend to beginning of original file path, applied
           after stripdir
limit_sl_dest: ignore symlinks if they are pointing outside of
               the defined path
hardlink_dupes: hardlink duplicated pyc files

## compileall.compile_file(fullname, ddir=None, force=False, rx=None, quiet=0, legacy=False, optimize=-1, invalidation_mode=None, *, stripdir=None, prependdir=None, limit_sl_dest=None, hardlink_dupes=False)

Byte-compile one file. Arguments (only fullname is required):

fullname:  the file to byte-compile
ddir:      if given, the directory name compiled in to the
           byte-code file.
force:     if True, force compilation, even if timestamps are up-to-date
quiet:     full output with False or 0, errors only with 1,
           no output with 2
legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
optimize:  int or list of optimization levels or -1 for level of
           the interpreter. Multiple levels leads to multiple compiled
           files each with one optimization level.
invalidation_mode: how the up-to-dateness of the pyc will be checked
stripdir:  part of path to left-strip from source file path
prependdir: path to prepend to beginning of original file path, applied
           after stripdir
limit_sl_dest: ignore symlinks if they are pointing outside of
               the defined path.
hardlink_dupes: hardlink duplicated pyc files

## compileall.compile_path(skip_curdir=1, maxlevels=0, force=False, quiet=0, legacy=False, optimize=-1, invalidation_mode=None)

Byte-compile all module on sys.path. Arguments (all optional):

skip_curdir: if true, skip current directory (default True)
maxlevels:   max recursion level (default 0)
force: as for compile_dir() (default False)
quiet: as for compile_dir() (default 0)
legacy: as for compile_dir() (default False)
optimize: as for compile_dir() (default -1)
invalidation_mode: as for compiler_dir()

## compileall.main()

Script main program.
