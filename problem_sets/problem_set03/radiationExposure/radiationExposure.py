from riemannIntegral import f
# def f(x):
#     """Curve function of ...

#     """
#     import math
#     return 10 * math.e ** (math.log(0.5) / 5.27 * x)


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    Args:
        start: integer, the time at which exposure begins
        stop: integer, the time at which exposure ends
        step: float, the width of each rectangle. You can assume that
              the step size will always partition the space evenly.

    Returns:
        float, the amount of radiation exposed to between start and stop times.

    Raises:

    '''
    # FILL IN YOUR CODE HERE...
    mbq = 0

    def frange(start, stop, step):
        while start < stop:
            yield start
            start += step

    for newStart in frange(start, stop, step):
        mbq += f(newStart) * step

    return mbq

# ----------
# Test cases
# ----------

print radiationExposure(0, 5, 1)          # ==> 39.10318784326239
print radiationExposure(5, 11, 1)         # ==> 22.94241041057671
print radiationExposure(0, 11, 1)         # ==> 62.0455982538
print radiationExposure(40, 100, 1.5)     # ==> 0.434612356115

# --------------------------------------
# More test cases from the course grader
# --------------------------------------

print radiationExposure(12, 16, 1)        # ==> 6.848645835538622
print radiationExposure(0, 4, 0.25)       # ==> 1148.6783342153556
print radiationExposure(5, 10, 0.25)      # ==> 513.4662018628549
print radiationExposure(0, 3, 0.1)        # ==> 559.2259707824549
print radiationExposure(14, 20, 0.1)      # ==> 523.4527522388149
print radiationExposure(48, 72, 0.4)      # ==> 268.79947333082856
print radiationExposure(72, 96, 0.4)      # ==> 82.61081970598813
print radiationExposure(0, 40, 1)         # ==> 4066.0849302266774
print radiationExposure(100, 400, 4)      # ==> 843.5828023451531
print radiationExposure(1000, 4000, 15)   # ==> 3.6525375905841067e-06
print radiationExposure(0, 60, 0.5)       # ==> 2542.768831286683
print radiationExposure(60, 120, 0.5)     # ==> 1203.5229215597114
print radiationExposure(600, 1200, 5)     # ==> 2.799597134148232

###############################################################################

# NOTES:
