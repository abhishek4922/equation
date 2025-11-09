import pandas as pd
import numpy as np

def save_results(x_obs, y_obs, t_final, theta, M, X):
    df_out = pd.DataFrame({'x': x_obs, 'y': y_obs, 't_est': t_final})
    df_out.to_csv('outputs/fitted_with_t_estimates.csv', index=False)
    np.savetxt('outputs/fitted_params.txt', np.array([theta, M, X]), header='theta,M,X')
