import numpy as np
import math

def power_method(A, initial_guess, tolerance, max_iterations):
    """
    Input:
        A: a square matrix with floating point real numbers as entries

        initial_guess: vector of n floating point real numbers that serves as
            the initial guess for an eigenvector of A

        tolerance: positive floating point real number that determines when the
            approximation is close enough

        max_iterations: positive integer giving the maximum number of times to
            iterate the power method befor quiting

    Returns:
        {
        value: the eigenvalue of A
        vector: the eigenvector of A
        iterations: the number of iterations
        trace: the trace of A 
        det: the determinant of A
        }
    """
    # load A and initial_guess into a numpy array
    A = np.array(A)
    initial_guess = np.array(initial_guess)

    # we're going to need this later for computing the next eigenvector
    prior_eigenvalue = 0

    # load the first iteraton before starting the algorithm
    u = np.dot(A, initial_guess)
    eigenvalue = u[0]
    u = u / float(eigenvalue)
    initial_guess = u
    iterations = 1

    while abs(eigenvalue - prior_eigenvalue) > tolerance:
        prior_eigenvalue = eigenvalue
        u = np.dot(A, initial_guess)
        eigenvalue = u[0]
        u = u / float(eigenvalue)
        initial_guess = u
        iterations += 1

        # we need to quit if we haven't found the eigenvalue within the
        # alloted iterations
        if iterations > max_iterations:
            return None
    
    return {
        'value': eigenvalue,
        'vector': u,
        'iterations': iterations,
        'trace': trace(A),
        'det': determinant(A)
    }

def trace(A):
    """
    Input:
        A: a 2 by 2 matrix

    Returns:
        the trace of A
    """

    # since A will always be a 2 by 2 matrix we can just hardcode this
    return A[0][0] * A[1][1]

def invert(A):
    """
    Input:
        A: a 2 by 2 matrix

    Returns:
        the inverse of A
    """

    # since A will always be a 2 by 2 matrix we can just hardcode this
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    cofactor = np.array([[d, -b],
                        [-c, a]])
    
    return determinant(A) * cofactor

def determinant(A):
    """ 
    Input:
        A: a 2 by 2 matrix

    Returns:
        the determinant of A
    """

    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    return a * d - b * c
