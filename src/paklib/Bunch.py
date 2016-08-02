
class Bunch(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def as_dict(self, suppress_none=False):
        d = self.__dict__.copy()
        for k, v in d.items():
            if k.startswith('_'):
                del d[k]
            elif suppress_none and v is None:
                del d[k]
            else:
                try:
                    dict_value = v.as_dict(suppress_none)
                    d[k] = dict_value
                except AttributeError:
                    pass
        return d

    def from_dict(self, values):
        self.__dict__.update(values)
        return self

    def __str__(self):
       return str(self.as_dict())

    def __repr__(self):
        return "%s(%s)" % (
            self.__class__.__name__,
            ', '.join(['%s = %v' % (k, repr(v)) for k, v in self.as_dict().items()]))
