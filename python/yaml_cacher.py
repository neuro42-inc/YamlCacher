if __name__ == '__main__': # need to load the library
    LIB_NAME:str = "lib_yaml_cacher.so"
    def __bootstrap__():
        from os import path
        from ctypes import cdll
        cwd = path.dirname(path.abspath(__file__))
        cdll.LoadLibrary(path.join(cwd, LIB_NAME))
    __bootstrap__()
    from lib_yaml_cacher import get_yaml as get_yaml_impl
else:
    from .lib_yaml_cacher import get_yaml as get_yaml_impl

def get_yaml(absolute_path:str, keys:'list[str]'=None):
    """
    Load yml file. Return dictionary, list, or value.
    Parameters
    ----------
    keys: list[str] or None
        A series of keys used to traverse the yaml file. If None, return the entire file.
        
    Returns
    ----------
    The value of the yaml file at the given keys. If keys is None, return the entire file.
        
    For example, if the yaml file is:
    foo: [1, 2,3]
    bar: {a: 1, b: 2}
    
    Calling get_yaml(absolute_path, ['bar']) will return {a: 1, b: 2}
    Calling get_yaml(absolute_path, ['bar', 'a']) will return 1
    Calling get_yaml(absolute_path) will return {'foo': [1, 2,3], 'bar': {'a': 1, 'b': 2}} 
    """
    return get_yaml_impl(absolute_path, keys)