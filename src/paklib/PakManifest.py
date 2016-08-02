import json
from copy import copy
from Bunch import Bunch

class Permissions(Bunch):
    def __init__(self):
        super(Permissions, self).__init__(
            owner_read = None,
            owner_write = None,
            owner_execute = None,
            group_read = None,
            group_write = None,
            group_execute = None,
            world_read = None,
            world_write = None,
            world_execute = None)



class PakFile(Bunch):
    '''A file in the package'''

    BLANK_PERMS = Permissions()

    def __init__(self, rel_path):
        super(PakFile, self).__init__(
            path = rel_path,
            hash = None,
            owner = None,
            group = None,
            perms = copy(self.BLANK_PERMS))


class PakFolder(Bunch):
    '''A folder/directory in the package'''

    def __init__(self, rel_path):
        super(PakFolder, self).__init__(
            path = rel_path,
            owner = None,
            group = None,
            perms = copy(PakFile.BLANK_PERMS))


class PakManifest(object):
    '''The manifst file lists the files and folders to be deployed in a package

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

     TODO: Update permission flag names

      doc['dirs']: A list of directorie entries.  Each with entry keys:
        path:  Relative path to directory from install target
        owner: The name of the user which should own the file
        group: The name of the group which should own the file
        perms: A dictionary of t/f flags corresponding to basic Unix permission flags
              (or, ow, oe, gr, gw, ge, wr, ww, we)
    '''

    def __init__(self):
        self.version = '1'
        self.files = dict()     # Index by relative path
        self.dirs = dict()      # Index by relative path


    def load_string(self, manifest_src):
        '''Parse manifest file'''
        data = json.loads(manifest_src)
        self.version = data['version']

        self.files = [PakFile(None).from_dict(d) for d in  data['files']]
        self.files = {o.path: o for o in self.files}

        self.dirs = [PakFolder(None).from_dict(d) for d in  data['dirs']]
        self.dirs = {o.path: o for o in self.dirs}


    def save_string(self):
        '''Format string to save manifest data'''
        data = dict(
            version = self.version,
            files = [v.as_dict(suppress_none=True) for v in self.files.values()],
            dirs = [v.as_dict(suppress_none=True) for v in self.dirs.values()],
        )
        return json.dumps(data, indent=4, separators=(',', ': '))
