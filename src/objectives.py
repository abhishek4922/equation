import numpy as np
from .model import l1_fit_given_t
from .controls import control_to_t

def coarse_obj(params, x_obs, y_obs, cfg):
    """Objective for coarse DE optimization (assuming linear t)."""
    theta, M, X = params
    t_lin = np.linspace(cfg.t_min, cfg.t_max, len(x_obs))
    return l1_fit_given_t(theta, M, X, t_lin, x_obs, y_obs)


def full_objective(vars_flat, x_obs, y_obs, cfg):
    """Full objective: optimize θ, M, X, and control deltas together."""
    theta, M, X = vars_flat[0], vars_flat[1], vars_flat[2]
    control = vars_flat[3:]
    t_full = control_to_t(control, cfg.t_min, cfg.t_max, len(x_obs))
    fit_term = l1_fit_given_t(theta, M, X, t_full, x_obs, y_obs)

    # Regularization (smoothness of control)
    if len(control) >= 3:
        smooth_pen = np.sum(np.square(np.diff(control, n=2)))
    else:
        smooth_pen = 0.0

    reg = cfg.reg_lambda * smooth_pen
    return fit_term + reg

