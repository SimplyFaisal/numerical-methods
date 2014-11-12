import math
import numpy as np
from util import FileReader
import matplotlib.pyplot as plot

def gauss_newton(filename, initial_guess, iterations, fit, partial):
    """
    Input:
        filename: the name of the file containing the points
        initial_guess: the initial guesses for for the parameters a, b, and c
        iterations: number of iterations to run the gauss-newton algorithm
        fit: the curve to approximate (function)
        partial: the partial derivative of the curve (function)

    Returns:
        the parameters giving the best approximation for the appropriate curve
        matching the given points
    """
    points = FileReader().vectorize(filename)
    B = np.array(initial_guess)
    r = residuals(B, points, fit)
    J = jacobian(B , r, partial)

    for i in range(iterations):
        Q, R = np.linalg.qr(J)
        x = np.linalg.lstsq(R, np.dot(Q.transpose(), r))[0]
        B = B - x
        r = residuals(B, points, fit)
        J = jacobian(B, r, partial)
        
    return B


def qr_fact_househ(A):
    """
    Input:
        A: a matrix
    
    Returns:
        (q, r) the qr factorization of matrix A using householder reflections
    """
    pass

def qr_fact_givens(A):
    """
    Input:
        A: a matrix
    
    Returns:
        (q, r) the qr factorization of A using givens rotations
    """
    pass

def househ_reflection(column):
    """
    Input:
        column: a column of a matrix

    Returns:
        H: the result of a householder reflection performed on the column
    """
    pass

def residuals(B, points, curve):
    """
    Input:
        B: vector (a, b , c)
        points: the points used to construct the residual
        curve: the curve used to construct the residual
    
    Returns:
        the residual vector

    """
    return np.array([ y - curve(B, x) for x, y in points])

def jacobian(B, R, partial):
    """
    Input:
        B: vector (a, b, c)
        R: the residual vector
        partial: the partial used to construct the jacobian

    Returns:
        The jacobian formed by the inputs
    """
    j = [[partial(B, index, r) for index, b in enumerate(B)] for r in R]
    return np.array(j)


def quadratic_fit(B, x):
    """
    Input:
        B: vector with 3 coordinates
        x: a value

    Returns:
        B(x)        
    """
    a = B[0]
    b = B[1]
    c = B[2]
    return (math.pow(a, 2)) + (b * x) + c

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
    a = B[0]
    b = B[1]
    c = B[2]
    return a * math.pow(math.e, b * x) + c

def exponential_partial(B, index, value):
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
        return -math.pow(math.e, b * value)
    if index == 1:
        return - value * a * math.pow(math.e, b * value)
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
    a = B[0]
    b = B[1]
    c = B[2]
    return a * math.log10(x + b) + c


def rational_fit(B, x):
    """
    Input:
        B: vector with 3 coordinates
        x: a value

    Returns:
       the rational fit  B(x)        
    """
    a = B[0]
    b = B[1]
    c = B[2]
    return ((a * x) / (x + b)) + c

def rational_partial(B, index, value):
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
        return -float(value) / (value + b)
    if index == 1:
        return - value / math.pow(value + 1, 2)
    if index == 2:
        return -1

if __name__ == '__main__':
    a = gauss_newton('quadratic.txt', (1, 3, -1), 5, quadratic_fit, quadratic_partial)
