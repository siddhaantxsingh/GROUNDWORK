# runpy

## runpy.run_module(mod_name, init_globals=None, run_name=None, alter_sys=False)

mod_name -- an absolute module name or package name.

Optional arguments:
init_globals -- dictionary used to pre-populate the module’s
globals dictionary before the code is executed.

run_name -- if not None, this will be used for setting __name__;
otherwise, __name__ will be set to mod_name + '__main__' if the
named module is a package and to just mod_name otherwise.

alter_sys -- if True, sys.argv[0] is updated with the value of
__file__ and sys.modules[__name__] is updated with a temporary
module object for the module being executed. Both are
restored to their original values before the function returns.

Returns the resulting module globals dictionary.

## runpy.run_path(path_name, init_globals=None, run_name=None)

path_name -- filesystem location of a Python script, zipfile,
or directory containing a top level __main__.py script.

Optional arguments:
init_globals -- dictionary used to pre-populate the module’s
globals dictionary before the code is executed.

run_name -- if not None, this will be used to set __name__;
otherwise, '<run_path>' will be used for __name__.

Returns the resulting module globals dictionary.
