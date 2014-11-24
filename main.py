from gauss_newton import *

def main():
    filename = raw_input('Please input the name of the text file containing the points: ')

    a = float(raw_input('Please input the initial guess for parameter a: '))
    print "........................................" 

    b = float(raw_input('Please input the initial guess for parameter b: '))
    print "........................................" 
    
    c = float(raw_input('Please input the initial guess for parameter c: '))
    print "........................................" 

    guess = a, b , c
    iterations = int(raw_input('How many iterations?: '))

    print "1.) quadratic"
    print "2.) exponential"
    print "3.) logarithmic"
    print "4.) rational"

    option = raw_input('Which curve would you like to approximate?' +
                        '\nPlease select the corresponding number: ')

    if option == "1":
        result = gn_qua(filename, guess, iterations)
    elif option == "2":
        result = gn_exp(filename, guess, iterations)
    elif option == "3":
        result = gn_log(filename, guess, iterations)
    elif option == "4":
        result = gn_rat(filename, guess, iterations)

    print "................................"    
    print "The answer is {}".format(result)

def gn_qua(filename, initial_guess, iterations):
    """
    Computes gauss newton using a quadratic fit

    Input:
        filename: the name of the file containing the points
        initial_guess: the initial guesses for for the parameters a, b, and c
        iterations: number of iterations to run the gauss-newton algorithm

    Returns:
        the parameters giving the best approximation for the appropriate curve
        matching the given points
    """
    return gauss_newton(filename, initial_guess, iterations,
                        qr_fact_househ, quadratic_fit, quadratic_partial)


def gn_exp(filename, initial_guess, iterations):
    """
    Computes gauss newton using an exponential fit

    Input:
        filename: the name of the file containing the points
        initial_guess: the initial guesses for for the parameters a, b, and c
        iterations: number of iterations to run the gauss-newton algorithm

    Returns:
        the parameters giving the best approximation for the appropriate curve
        matching the given points
    """
    return gauss_newton(filename, initial_guess, iterations,
                        qr_fact_househ, exponential_fit, exponential_partial)

def gn_log(filename, initial_guess, iterations):
    """
    Computes gauss newton using a logarithmic fit

    Input:
        filename: the name of the file containing the points
        initial_guess: the initial guesses for for the parameters a, b, and c
        iterations: number of iterations to run the gauss-newton algorithm

    Returns:
        the parameters giving the best approximation for the appropriate curve
        matching the given points
    """
    return gauss_newton(filename, initial_guess, iterations, 
                        qr_fact_househ, logarithmic_fit, logarithmic_partial)

def gn_rat(filename, initial_guess, iterations):
    """
    Computes gauss newton using a rational fit

    Input:
        filename: the name of the file containing the points
        initial_guess: the initial guesses for for the parameters a, b, and c
        iterations: number of iterations to run the gauss-newton algorithm

    Returns:
        the parameters giving the best approximation for the appropriate curve
        matching the given points
    """
    return gauss_newton(filename, initial_guess, iterations,
                        qr_fact_househ, rational_fit, rational_partial)

if __name__ == '__main__':
    main()