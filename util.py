import sys
import numpy as np
class FileReader(object):

    def vectorize(self, filename):
        """
        Input:
            filename: text file containing n 2 dimensional tuples of points

        Returns:
            a vector representation of the points in the file
        """
        try:
            lines = open(filename, 'r').read().splitlines()
        except IOError:
            print "File IOError"
            print "Unable to read from from file {}".format(filename)
            print "Exiting now."
            sys.exit()
        vector = []
        for line in lines:
            x , y = line.split(',')
            vector.append((float(x),float(y)))
        return np.array(vector) 

if __name__ == '__main__':
    pass