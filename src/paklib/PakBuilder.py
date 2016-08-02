

class PackBuilder(object):
    '''Converts a folder structure into a package'''

    def __init__(self, source_path, target_path):
        self.source = source_path
        self.target = target_path


    def build(self):
        raise NotImplementedError()
