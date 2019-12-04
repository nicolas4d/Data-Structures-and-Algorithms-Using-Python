import ctypes

PyArrayType = ctypes.py_object * 5
_element = PyArrayType()

_element[0] = None
print(_element[0])
