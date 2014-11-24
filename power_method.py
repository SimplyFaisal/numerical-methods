import numpy as np
import math
import matplotlib.pyplot as plot
import random

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
    return A[0][0] + A[1][1]

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

def get_matrix():
    """
    Returns: a two by two matrix with a nonzero determinant
    """
    A = np.array(rand_matrix(-2,2))
    if not determinant(A):
        return get_matrix()
    return A

def rand_matrix(low, high):
    """ 
    Input:
        low: the lower bound
        high: the upper bound

    Returns:
        a two by two array whose elements are in [low, high]
    """
    return [[random.uniform(low, high) for i in range(2)] for i in range(2)]

def main():
    """
    Performs the graphing actions of this part of the assignment
    """
    #initialize a 1000 matrices
    matrices = []
    while len(matrices) < 1000:
        matrices.append(get_matrix())
    inverses = [invert(m) for m in  matrices]

    e = 0.00005
    max_runs = 100
    
    # the next two for loops run power_method on all the matrices and their
    # inverses. if the eigenvalue is found then the resulting data is added
    # to the list
    data = []
    for m in matrices:
        power_method_result = power_method(m, [1,1], e, max_runs)
        if power_method_result:
            data.append(power_method_result)
    
    inverse_data = []
    for inverse in inverses:
        power_method_result = power_method(inverse, [1,1], e, max_runs)
        if power_method_result:
            inverse_data.append(power_method_result)

    # Graph Matrices Data
    plot.figure(1)
    plot.title('Determinant vs. Trace')
    plot.xlabel('Determinant')
    plot.ylabel('Trace')
    plot.scatter([m['det'] for m in data],
                 [m['trace'] for m in data],
                 c = [m['iterations'] for m in data])
    # plot.show()

    # Graph Inverse Matrices Data
    plot.figure(2)
    plot.title(' Inverse Determinant vs. Trace')
    plot.xlabel('Determinant')
    plot.ylabel('Trace')
    t = []

    plot.scatter([m['det'] for m in inverse_data],
                 [m['trace'] for m in inverse_data],
                 c = [m['iterations'] for m in inverse_data])
    plot.show()

if __name__ == '__main__':
    main()
