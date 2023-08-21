import numpy as np
import cvxpy as cp

# Example data: expected returns and covariance matrix of assets
expected_returns = np.array([0.15, 0.10, 0.12, 0.07])
cov_matrix = np.array([[0.05, 0.02, 0.01, 0.03],
                        [0.02, 0.08, 0.03, 0.04],
                        [0.01, 0.03, 0.10, 0.02],
                        [0.03, 0.04, 0.02, 0.06]])

# Number of assets in the portfolio
n_assets = len(expected_returns)

# Decision variables: asset allocation
x = cp.Variable(n_assets)

# Constraints
constraints = [x >= 0, cp.sum(x) == 1]

# Objective function: maximize expected return (can be changed to minimize risk)
objective = cp.Maximize(expected_returns @ x)

# Optimization problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Display results
optimal_allocation = x.value
print("Optimal asset allocation:")
for i in range(n_assets):
    print(f"Asset {i + 1}: {optimal_allocation[i]:.4f}")
