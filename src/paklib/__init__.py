'''Library to support the pak command

Package format v1
-----------------

File format is a zip (with optional compression).  The structure of the archive is:

 manifest.json - Listing of files and directories
 files/* - Files contents to be placed when installed

The manifest structure is:

  doc: Root objectis a dictionary

  version: Holds value "1"

  doc['files']: A list of file entries.  Each with entry keys:
    path:  Relative path to file from install target
    hash:  An MD5 hash of the contents
    owner: The name of the user which should own the file
    group: The name of the group which should own the file
    perms: A dictionary of t/f flags corresponding to basic Unix permission flags
           (or, ow, oe, gr, gw, ge, wr, ww, we)

  doc['dirs']: A list of directorie entries.  Each with entry keys:
    path:  Relative path to directory from install target
    owner: The name of the user which should own the file
    group: The name of the group which should own the file
    perms: A dictionary of t/f flags corresponding to basic Unix permission flags
          (or, ow, oe, gr, gw, ge, wr, ww, we)


'''