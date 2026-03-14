import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def d_sigm(z):
    m = _sigmoid(z)
    return m*(1-m)

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X = np.array(X)
    y = np.array(y)
    N = len(y)
    D = len(X[0])
    w = np.array([0.0]*D)
    b = 0.0
    for _ in range(steps):
        a = X.dot(w) + b
        p = _sigmoid(a)
        dldw = np.dot((np.transpose(X)),(y-p))/N
        dldb = np.sum(y-p)/N
        w += lr*dldw
        b += lr*dldb
    return (w,b)
        