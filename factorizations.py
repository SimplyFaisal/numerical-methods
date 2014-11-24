import numpy as np 
import math

def qr_fact_househ(A):
    """
    Input:
        A: a matrix
    
    Returns:
        (q, r) the qr factorization of matrix A using householder reflections
    """
    rows, height  = A.shape
    H = househ_reflection(A.transpose()[0])
    reflections = []
    reflections.append(A)
    reflections.append(H)
    for i in range(1, height):
        # multiply in reverse order to get the latest H
        resultant = reduce(lambda x, y: np.dot(x, y), reflections[::-1])
        column = resultant.transpose()[i][i:]
        minor = househ_reflection(column)
        H = embed(np.eye(rows), minor)
        reflections.append(H)

    # Compute q by multiplying together all of the H's in order
    q = reduce(lambda x, y: np.dot(x, y), reflections[1:])
    r = np.dot(q.transpose(), A)

    print 'Q is '
    print q
    print 'R is '
    print r

    return q, r

def qr_fact_givens(A):
    """
    Input:
        A: a matrix
    
    Returns:
        (q, r) the qr factorization of A using givens rotations
    """
    rows, cols = A.shape
    reflections = []
    for i in range(0, cols):
        for j in range(0, rows):
            if i == j:
                pivot_pos = (j, i)
            if i < j:
                if A[j][i]:
                    G = givens_rotation(A, np.eye(rows), pivot_pos, (j, i))
                    reflections.append(G)
                    A = np.dot(G, A)
    R = A
    Q = reduce(lambda x, y: np.dot(x.transpose(), y.transpose()), reflections)
    return Q, R

def givens_rotation(A, I, xpos, ypos):
    """
        Input:
            A:
            xpos:
            ypos:

        Returns:
            the givens matrix for the x and y
    """
    x , y = xpos
    i , j = ypos

    xval = A[x][y]
    yval = A[i][j]

    r = math.hypot(xval, yval)
    c = xval / r
    s = yval / r

    I[i][i] = c
    I[j][j] = c
    I[j][i] = s
    I[i][j] = -s
    return I

def househ_reflection(column):
    """
    Input:
        column: a column of a matrix

    Returns:
        H: the result of a householder reflection performed on the column
    """
    height = len(column)
    v = add(column, norm(column) * np.eye(height, 1))
    u = v / norm(v)
    H = np.eye(height)  - 2 * u * u.transpose()
    return H

def norm(vector):
    """
        Input:
            vector:

        Returns:
            the euclidean norm of the vector
    """
    _sum = math.fsum([math.pow(x, 2) for x in vector])
    return math.sqrt(_sum)

def add(a, b):
    """
    Why can't I just add two vectors??
        Input:
            a: a vector of size n
            b: another vector of size n

        Returns:
            a vector sum of the two vectors
    """
    return np.array([x + y for x, y in zip(a, b)])

def embed(matrix, minor):
    """
        Input:
            matrix: The identity matrix to embed the minor into
            minor: The smaller matrix that we want to embed

        Returns:
            The matrix that was passed in with the values modified to be the values
            of the embeded matrix
    """
    R, C = matrix.shape
    r, c = minor.shape

    # Due to the way that I am doing the mapping from the smaller matrix to the larger
    # matrix the elements are reversed both horizontally and vertically, the easy way to
    # fix this is just to reverse the minor matrix then perform the mapping.
    minor = np.flipud(np.fliplr(minor))
    for x in range(r):
        for y in range(c):
            matrix[R - x - 1][C - y - 1] = minor[x][y]
    return matrix

if __name__ == '__main__':
    b = np.array([[1, 2, 1],
                  [2, 3, 2],
                  [1, 2, 2]])
    c = np.array([[2, -1, 0],
                  [1, 2, -1],
                  [2, -1, 2]])

    q , r = qr_fact_givens(b)
    #v, w = qr_fact_househ(c)
    print r
    print np.dot(q, r)
    # print w
