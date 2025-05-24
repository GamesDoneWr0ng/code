from python import Python, PythonObject
from tensor import Tensor, TensorShape

def func(tensor: Tensor[DType.int32]) -> PythonObject:
    np = Python.import_module("numpy")
    ctypeslib = Python.import_module("numpy.ctypeslib")
    ctypes = Python.import_module("ctypes")

    var rows = tensor.shape()[0]
    var cols = tensor.shape()[1]

    data_ptr = ctypes.cast(tensor._ptr.cast(DType.int32), ctypes.POINTER(ctypes.c_int32))
    numpy_array = ctypeslib.as_array(data_ptr, shape=Python.tuple(rows, cols))
    return numpy_array

def main():
    var tensor: Tensor[DType.int32] = Tensor[DType.int32](TensorShape(2,2), 1, 2, 3, 4)
    print(tensor)
    print(func(tensor))