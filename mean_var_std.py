import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    a = np.array(list).reshape(3, 3)
    stats = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }
    calculations = {}
    for name, f in stats.items():
        calculations[name] = [f(a, axis=0).tolist(), f(a, axis=1).tolist(), f(a).item()]
    return calculations
