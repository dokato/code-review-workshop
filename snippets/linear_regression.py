import numpy as np

def compCostFunction(estim_y, true_y):
    E = estim_y - true_y
    C = (1 / 2 * m) * np.sum(E ** 2)
    return C

def test_dimensions(x, y):
    # this checks whether the x and y have the same number of samples
    assert isinstance(x, np.ndarray), "Only works for arrays"
    assert isinstance(y, np.ndarray), "Only works for arrays"
    return x.shape[0] == y.shape[0]

# To be deleted later
# feature_1 = np.linspace(0, 2, num=100)

X = np.random.randn(100,3)  # feature matrix
y = 1 + np.dot(X, [3.5, 4., -4])  # target vector

m = np.shape(X)[0]  # nr of samples
n = np.shape(X)[1]  # nr of features

def iterativeLinearRegression(X, y, alpha=0.01):
    """
    This makes iterative LR via gradient descent and returns estimated parameters and history list.
    """
    steps=500
    X = np.concatenate((np.ones((m, 1)), X), axis=1)

    W = np.random.randn(n + 1, )
 
    # stores the updates on the cost function
    cost_history = []
    # iterate until the maximum number of steps
    for i in np.arange(steps):  # begin the process
 
        y_estimated = X.dot(W)
 
        cost = compCostFunction(y_estimated, y)
        # Update gradient descent
        E = y_estimated - y
        gradient = (1 / m) * X.T.dot(E)
 
        W = W - alpha * gradient
        if i % 10 == 0:
            print(f"step: {i}\tcost: {cost}")
 
        cost_history.append(cost)
 
    return W, cost_history

params, history = iterativeLinearRegression(X, y)

# test 1
print(params)
print(history)

import matplotlib.pyplot as plt
plt.plot(history)
plt.xlabel("steps")
plt.show()

# test 2

X = np.random.randn(500,2)  # feature matrix
y = np.dot(X, [5, -1])  # target vector

m = np.shape(X)[0]  # nr of samples
n = np.shape(X)[1]  # nr of features

params, history = iterativeLinearRegression(X, y)
print(params)

import matplotlib.pyplot as plt
plt.plot(history)
plt.xlabel("steps")
plt.show()
