import numpy as np

def approach(val: float, target: float, maxMove: float) -> float:
    if maxMove == 0 or val == target:
        return val
    
    if val > target:
        return max(val - maxMove, target)
    else:
        return min(val + maxMove, target)

def approachVector(val: np.ndarray, target: np.ndarray, maxMove: float) -> np.ndarray:
    if maxMove == 0 or val == target:
        return val
    
    diff = target - val
    length = np.linalg.norm(diff)
    if length < maxMove:
        return target
    else:
        return val + diff / length * maxMove
    
def lerp(a, b, decay, dt):
    """Actualy expDecay, usefull range for decay is arround 1 to 25 from slow to fast."""
    return b + (a - b) * np.exp(-decay * dt)