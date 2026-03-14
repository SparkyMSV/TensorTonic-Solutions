def fun(a, b, c, x):
    return a*x**2 + b*x + c
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    """
    here we have to bump x -> X_ideal
    x -= lr*df/dx
    """
    for _ in range(steps):
        f = fun(a,b,c,x0)
        dfdx = 2*a*x0 + b
        x0 -= lr*dfdx
    return x0
        
    