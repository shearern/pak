import os
import gflags

class FileObject(object):
    '''An item found in the source folder'''

    def __init__(self, abs_path, rel_path):
        '''
        :param abs_path: Absoulte path to object on drive
        :param rel_path: Path relative to root folder of scan
        '''
        self.__abs_path = abs_path
        self.__rel_path = rel_path
    @property
    def abs_path(self):
        return self.__abs_path
    @property
    def path(self):
        return self.__rel_path
    def __str__(self):
        return self.__rel_path
    def __repr__(self):
        return "%s('%s', '%s')" % (self.__class__.__name__, self.__abs_path, self.__rel_path)


class FolderInTree(FileObject):

    @property
    def obj_type(self):
        return 'folder'


class FileInTree(FileObject):

    @property
    def obj_type(self):
        return 'file'


class TreeScanner(object):
    '''Utilitiy to scan through a folder to find directories and files'''

    def __init__(self, source_path):
        self.__path = source_path
        self.warn_non_file = None

    def scan(self):
        '''Find files and folders in the source folder'''
        folder_stack = list()
        folder_stack.append(FolderInTree(os.path.abspath(self.__path), ''))

        while len(folder_stack) > 0:
            source_dir = folder_stack.pop()
            if source_dir.path != '':
                yield source_dir
            for obj_name in os.listdir(source_dir.abs_path):
                obj_abs_path = os.path.join(source_dir.abs_path, obj_name)
                obj_rel_path = os.path.join(source_dir.path, obj_name)
                if os.path.isfile(obj_abs_path):
                    yield FileInTree(obj_abs_path, obj_rel_path)
                elif os.path.isdir(obj_abs_path):
                    folder_stack.append(FolderInTree(obj_abs_path, obj_rel_path))
                elif self.warn_non_file is not None:
                    self.warn_non_file(obj_abs_path)

