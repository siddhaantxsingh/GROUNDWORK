# modulefinder

## modulefinder.ModuleFinder.any_missing(self)

Return a list of modules that appear to be missing. Use any_missing_maybe() if you want to know which modules are certain to be missing, and which *may* be missing.

## modulefinder.ModuleFinder.any_missing_maybe(self)

The latter names could either be submodules *or* just global names in the package.

The reason it can't always be determined is that it's impossible to
tell which names are imported when "from module import *" is done
with an extension module, short of actually importing it.

## modulefinder.ModuleFinder.report(self)

Print a report to stdout, listing the found modules with their paths, as well as modules that are missing, or seem to be missing.
