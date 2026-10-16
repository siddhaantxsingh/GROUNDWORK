# zipimport

## zipimport.zipimporter(path)

Create a new zipimporter instance. 'archivepath' must be a path to a zipfile, or to a specific path inside a zipfile. For example, it can be '/tmp/myimport.zip', or '/tmp/myimport.zip/mydirectory', if mydirectory is a valid directory inside the archive.

'ZipImportError is raised if 'archivepath' doesn't point to a valid Zip
archive.

The 'archive' attribute of zipimporter objects contains the name of the
zipfile targeted.

## zipimport.zipimporter.find_spec(self, fullname, target=None)

Create a ModuleSpec for the specified module. Returns None if the module cannot be found.

## zipimport.zipimporter.get_code(self, fullname)

Return the code object for the specified module. Raise ZipImportError if the module couldn't be imported.

## zipimport.zipimporter.get_data(self, pathname)

Return the data associated with 'pathname'. Raise OSError if the file wasn't found.

## zipimport.zipimporter.get_filename(self, fullname)

Return the filename for the specified module or raise ZipImportError if it couldn't be imported.

## zipimport.zipimporter.get_resource_reader(self, fullname)

Return the ResourceReader for a module in a zip file.

## zipimport.zipimporter.get_source(self, fullname)

Return the source code for the specified module. Raise ZipImportError if the module couldn't be found, return None if the archive does contain the module, but has no source for it.

## zipimport.zipimporter.invalidate_caches(self)

Invalidates the cache of file data of the archive path.

## zipimport.zipimporter.is_package(self, fullname)

Return True if the module specified by fullname is a package. Raise ZipImportError if the module couldn't be found.

## zipimport.zipimporter.load_module(self, fullname)

'fullname' must be the fully qualified (dotted) module name. It returns the imported module, or raises ZipImportError if it could not be imported.

Deprecated since Python 3.10. Use exec_module() instead.
