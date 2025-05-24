from tensor import Tensor, TensorShape
from python import Python, PythonObject

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

def tensor_to_ndarray(tensor: Tensor[DType.float64]) -> PythonObject:
    var np = Python.import_module("numpy")
    var ctypeslib = Python.import_module("numpy.ctypeslib")
    var ctypes = Python.import_module("ctypes")

    var rows = tensor.shape()[0]
    var cols = tensor.shape()[1]

    var data_ptr = ctypes.cast(Float64(tensor._ptr), ctypes.POINTER(ctypes.c_double))
    return ctypeslib.as_array(data_ptr, shape=Python.tuple(rows, cols))