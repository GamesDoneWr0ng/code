from python import Python, PythonObject
from tensor import Tensor, TensorShape
from memory import UnsafePointer, memcpy
from utils.index import Index
from algorithm import parallelize

fn tensor_to_ndarray(tensor: Tensor[DType.float64]) raises -> PythonObject:
    var np = Python.import_module("numpy")
    var arr = np.zeros(Python.tuple(tensor.shape()[0], tensor.shape()[1], tensor.shape()[2]), dtype=np.float64)

    for i in range(tensor.shape()[0]):
        for j in range(tensor.shape()[1]):
            for k in range(tensor.shape()[2]):
                arr[i, j, k] = tensor[Index(i, j, k)]

    return arr

def main():
    var tensor: Tensor[DType.float64] = Tensor[DType.float64](TensorShape(2,2,2), 1, 2, 3, 4, 5, 6, 7, 8)
    print(tensor)
    try:
        print(tensor_to_ndarray(tensor))
    except:
        return