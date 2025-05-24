from tensor import Tensor, TensorShape
from utils.index import Index
from common import *
from row_col_matrix import MojoMatrix

fn lagrange(read bodies: List[Planet],
            read bounds: List[vec3],
            read divisions: List[Int]) raises -> Tensor[DType.float64]:

    var step: vec3 = (bounds[1] - bounds[0]) / vec3(divisions[0], divisions[1], divisions[2], 1)
    var result: Tensor[DType.float64] = Tensor[DType.float64](TensorShape(divisions[0], divisions[1], divisions[2]))

    for i in range(divisions[0]):
        for j in range(divisions[1]):
            for k in range(divisions[2]):
                var pos: vec3 = bounds[0] + vec3(i,j,k,0)*step
                var vec: vec3 = vec3(0,0,0,0)

                for body in bodies:
                    var dx: vec3 = pos - body[].position
                    vec -= body[].mass * (dx * ((dx*dx).reduce_add() ** -1.5)) # M/r^2
                # centripetal force
                vec += 4 * PI * PI * pos / ((pos*pos).reduce_add() ** 0.5) #4pi^2/T^2
                
                result[Index(i,j,k)] = (vec*vec).reduce_add() ** 0.5
    return result