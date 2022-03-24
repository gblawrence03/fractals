from complex import Complex

# z is initially 0
# c is the image coordinate
# we recur with fc(fc(0, c), c)
# where z and c are complex numbers
def fc(z, c) :
    return z.square() + c

threshold = 4
iterations = 100

# returns True if it is in the set (i.e it doesn't reach the threshold)
# returns the number of iterations taken to reach the threshold otherwise
def isMandelbrot(c, n = iterations, z = Complex(0, 0)):
    if z.magnitude() > threshold:
        return iterations - n
    if n == 0:
        return True
    return isMandelbrot(c, n - 1, fc(z, c))

