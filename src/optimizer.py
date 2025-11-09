import numpy as np
from scipy.optimize import differential_evolution, minimize
from .objectives import coarse_obj, full_objective
from .controls import control_to_t
from .model import l1_fit_given_t

def global_initialization(x_obs, y_obs, cfg):
    """Global coarse optimization using Differential Evolution."""
    result = differential_evolution(
        lambda p: coarse_obj(p, x_obs, y_obs, cfg),
        cfg.bounds_params,
        maxiter=200, popsize=20, seed=42
    )
    theta0, M0, X0 = result.x
    print(f"\n[Coarse Init] θ={np.rad2deg(theta0):.3f}° M={M0:.5f} X={X0:.3f} L1={result.fun:.3f}")
    return theta0, M0, X0


def alternating_optimization(x_obs, y_obs, theta0, M0, X0, cfg):
    """Alternating optimization of control vector and model params."""
    theta, M, X = theta0, M0, X0
    vars_controls = np.ones(cfg.m)

    for r in range(cfg.n_rounds):
        print(f"\n--- Round {r+1} ---")

        # Step 1: Control optimization
        def obj_ctrl(ctrl):
            vars_flat = np.concatenate(([theta, M, X], ctrl))
            return full_objective(vars_flat, x_obs, y_obs, cfg)

        res_ctrl = minimize(obj_ctrl, vars_controls, method='L-BFGS-B',
                            bounds=cfg.bounds_ctrl, options={'maxiter': 500, 'ftol': 1e-6})
        vars_controls = np.abs(res_ctrl.x)
        print(f" Control done (obj={res_ctrl.fun:.3f})")

        # Step 2: Parameter optimization
        t_current = control_to_t(vars_controls, cfg.t_min, cfg.t_max, len(x_obs))
        def obj_params(p):
            return l1_fit_given_t(p[0], p[1], p[2], t_current, x_obs, y_obs)

        res_params = minimize(obj_params, [theta, M, X], method='L-BFGS-B',
                              bounds=cfg.bounds_params, options={'maxiter': 500, 'ftol': 1e-6})
        theta, M, X = res_params.x
        print(f" Updated θ={np.rad2deg(theta):.4f}° M={M:.6f} X={X:.6f} L1={res_params.fun:.3f}")

    t_final = control_to_t(vars_controls, cfg.t_min, cfg.t_max, len(x_obs))
    return theta, M, X, t_final
