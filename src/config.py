import numpy as np

class Config:
    # t range
    t_min = 6.0
    t_max = 60.0

    # optimization parameters
    m = 60
    reg_lambda = 1e-2
    n_rounds = 8

    # parameter and control bounds
    bounds_params = [
        (0.0, np.deg2rad(50.0)),   # theta
        (-0.05, 0.05),             # M
        (0.0, 100.0)               # X
    ]
    bounds_ctrl = [(1e-6, 100.0)] * m
