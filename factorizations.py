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
    q = reduce(lambda x, y: np.dot(x,y), reflections[1:])
    r = np.dot(q.transpose(),A)
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
    reflections.append(A)
    for i in range(0, cols):
        for j in range(0, rows):
            if i == j:
                pivot = A[i][j]
                pivot_pos = (i, j)
            if i < j:
                if A[j][i]:
                    G = givens_matrix(rows, pivot, A[j][i], pivot_pos, (j, i))
                    reflections.append(G)
                    A = np.dot(G, A)
    R = A
    Q = reduce(lambda x, y: np.dot(x.transpose(), y.transpose()), reflections[1:])
    return Q, R

def givens_rotation():
    pass
    
def givens_matrix(rows, xval, yval, xpos, ypos):
    """
        Input:
            A
            x:
            y:

        Returns:
            the givens matrix for the x and y
    """
    I = np.eye(rows)
    c = xval / math.pow(math.pow(xval, 2) + math.pow(yval, 2), 0.5)
    s = - yval / math.pow(math.pow(xval, 2) + math.pow(yval, 2), 0.5)
    I[xpos[0]][xpos[0]] = c
    I[ypos[0]][ypos[0]] = c
    I[xpos[0]][ypos[0]] = -s
    I[ypos[0]][xpos[0]] = s
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
    b = np.array([[6, 5, 0],
                  [5, 1, 4],
                  [0, 4, 3]])
    c = np.array([[12, -51, 4],
                  [6, 167, -68],
                  [-4, 24, -41]])
    q , r = qr_fact_givens(c)
    print q
    print r
    print np.dot(q,r)