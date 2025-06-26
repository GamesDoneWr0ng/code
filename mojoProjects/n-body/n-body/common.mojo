from tensor import Tensor, TensorShape
from python import Python, PythonObject
from utils.index import Index
from algorithm import parallelize

alias Float = Float64
alias vec3 = SIMD[DType.float64, 4]

alias PI: Float = 3.14159265358979323846
alias SOLAR_MASS: Float = 4 * PI * PI
alias DAYS_PER_YEAR: Float = 365.2422

@value
struct Planet:
    var position: vec3
    var velocity: vec3
    var mass: Float

    fn __init__(out self,
                read position: vec3,
                read velocity: vec3,
                read mass: Float):
        self.position = position
        self.velocity = velocity
        self.mass = mass

fn tensor_to_ndarray(tensor: Tensor[DType.float64]) raises -> PythonObject:
    var np = Python.import_module("numpy")
    var arr = np.zeros(Python.tuple(tensor.shape()[0], tensor.shape()[1], tensor.shape()[2]), dtype=np.float64)

    for i in range(tensor.shape()[0]):
        for j in range(tensor.shape()[1]):
            for k in range(tensor.shape()[2]):
                arr[i, j, k] = tensor[Index(i, j, k)]

    return arr