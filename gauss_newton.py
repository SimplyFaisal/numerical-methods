import math
import numpy as np
from util import FileReader
from factorizations import qr_fact_househ, qr_fact_givens

def gauss_newton(filename, initial_guess, iterations, qr, fit, partial):
    """
    Input:
        filename: the name of the file containing the points
        initial_guess: the initial guesses for for the parameters a, b, and c
        iterations: number of iterations to run the gauss-newton algorithm
        qr: the qr factorization algorithm to use (function)
        fit: the curve to approximate (function)
        partial: the partial derivative of the curve (function)

    Returns:
        the parameters giving the best approximation for the appropriate curve
        matching the given points
    """

    # Read in the file and initialize the vector B, the residual vector, and the Jacobian
    points = FileReader().vectorize(filename)
    B = np.array(initial_guess)
    r = residuals(B, points, fit)
    J = jacobian(B , points, partial)

    # Perform the necessary iterations
    for i in range(iterations):
        Q, R = qr(J)
        b = np.dot(Q.transpose(), r)
        x = solve(R, b)
        B = B - x
        r = residuals(B, points, fit)
        J = jacobian(B, points, partial)
    return B

def residuals(B, points, curve):
    """
    Input:
        B: vector (a, b , c)
        points: the points used to construct the residual
        curve: the curve used to construct the residual
    
    Returns:
        the residual vector

    """
    return np.array([y - curve(B, x) for x, y in points])

def jacobian(B, points, partial):
    """
    Input:
        B: vector (a, b, c)
        R: the residual vector
        partial: the partial used to construct the jacobian

    Returns:
        The jacobian formed by the inputs
    """
    j = [[partial(B, index, p[0]) for index in range(len(B))] for p in points]
    return np.array(j)

def solve(A, b):
    """
        Input:
            A: a matrix
            b: the vector to solve for

        Returns:
            x: the solution to Ax = b
    """
    z = b[2] / A[2][2]
    y = (b[1] - (z * A[1][2])) / A[1][1]
    x = (b[0] - (z * A[0][2]) - (y * A[0][1])) / A[0][0]
    return x , y, z

def quadratic_fit(B, x):
    """
    Input:
        B: vector with 3 coordinates
        x: a value

    Returns:
        B(x)        
    """
    a, b , c = B
    return (a * math.pow(x, 2)) + (b * x) + c

def quadratic_partial(B, index, value):
    """
    Input:
        B: vector (a, b ,c)
        index: the index of B that is passed in, used to artificially
            construct the partial derivative
        value:

    Returns:
        the partial of r with respect to B index

    """
    if index == 0:
        return  -math.pow(value, 2)
    if index == 1:
        return -value
    if index == 2:
        return -1

def exponential_fit(B, x):
    """
    Input:
        B: vector with 3 coordinates
        x: a value

    Returns:
       the exponential fit  B(x)        
    """
    a, b , c = B
    return a * math.pow(math.e, b * x) + c

def exponential_partial(B, index, x):
    """
     Input:
        B: vector (a, b ,c)
        index: the index of B that is passed in, used to artificially
            construct the partial derivative

        value:

    Returns:
        the partial of r with respect to B index
    """

    a , b , c = B
    if index == 0:
        return -math.pow(math.e, b * x)
    if index == 1:
        return - x * a * math.pow(math.e, b * x)
    if index == 2:
        return -1 

def logarithmic_fit(B, x):
    """
    Input:
        B: vector with 3 coordinates
        x: a value

    Returns:
       the logarithmic fit  B(x)        
    """
    a, b , c = B
    return a * math.log(x + b) + c

def logarithmic_partial(B, index, x):
    a, b , c = B
    if index == 0:
        return -math.log(x + b)
    if index == 1:
        return -a / math.log(x + b)
    if index == 2:
        return -1

def rational_fit(B, x):
    """
    Input:
        B: vector with 3 coordinates
        x: a value

    Returns:
       the rational fit  B(x)        
    """
    a, b , c = B
    return ((a * x) / (x + b)) + c

def rational_partial(B, index, x):
    """
     Input:
        B: vector (a, b ,c)
        index: the index of B that is passed in, used to artificially
            construct the partial derivative
        value:

    Returns:
        the partial of r with respect to B index
    """
    a, b , c = B
    if index == 0:
        return - x / (x + b)
    if index == 1:
        return (a * x) / math.pow(x + b, 2)
    if index == 2:
        return -1

if __name__ == '__main__':
    a = gauss_newton('quadratic.txt', (1, 3, -1), 5, 
                     qr_fact_househ, quadratic_fit, quadratic_partial)
    print a
