import numpy as np

def model_xy(theta, M, X, t):
    """Compute (x, y) from parameters and time array."""
    term = np.exp(M * np.abs(t)) * np.sin(0.3 * t)
    x = t * np.cos(theta) - term * np.sin(theta) + X
    y = 42.0 + t * np.sin(theta) + term * np.cos(theta)
    return x, y


def l1_fit_given_t(theta, M, X, t, x_obs, y_obs):
    """Compute L1 distance between predicted and observed (x, y)."""
    x_pred, y_pred = model_xy(theta, M, X, t)
    return np.sum(np.abs(x_pred - x_obs) + np.abs(y_pred - y_obs))
