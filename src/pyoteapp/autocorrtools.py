r"""
This module provides several tools involving correlated noise.

There is a function for calculating auto-correlation coefficients
and a class for use in generating random noise with specified auto-correlation
characteristics.

Example:
    >>> noise_gen = CorrelatedNoiseGenerator(acfcoeffs=[1.0, 0.5, 0.3, 0.1])
    >>> test_noise = noise_gen.corr_normal(num_values=100000)
    >>> autocorr(test_noise, lastlag=6)
    [1.0,
     0.50094352543708198,
     0.30158412855919509,
     0.10104967953428118,
     0.002665198305403594,
     0.0024066568197502591,
     0.0012079072002819918]
"""

# coding: utf-8

from numpy import zeros, random, convolve
from scipy.stats.stats import pearsonr
from scipy.linalg import cholesky

__all__ = ['CorrelatedNoiseGenerator', 'autocorr']


def selfcorr(x, lag=1):
    """ computes the self-correlation of a vector for a specified lag.
        This is a support function for autocorr.
    
        Args:
            x (float array): array to be correlated
            lag (int): specifies the lag for the correlation calculation
        
        Returns:
            a single correlation coefficient at the specified lag.
    """

    n = len(x)

    if len(x) <= lag + 1:
        raise Exception("lag is too large for x array")

    y1 = x[lag:]
    y2 = x[:n - lag]
    corr = pearsonr(y1, y2)[0]
    return corr


def autocorr(x, lastlag=10):
    """ computes the self-correlation coefficients of x 
        from lag = 0 to lag = lastlag
    
        Args:
            x (float array): array to be correlated
            lastlag (int): the final lag value to be calculated
    """

    if lastlag + 1 >= len(x):
        raise Exception("laglast is too large")

    lags = range(0, lastlag + 1)
    corrs = [selfcorr(x, lag) for lag in lags]
    return corrs

# Our goal is to produce gaussian noise that has a specified auto-correlation response when given as an
# argument to ```autocorr()```. To do that, we build an auto-correlation matrix that has the desired
# auto-correlation coefficients in the off-diagonal terms.


def build_acf_matrix(acfcoeffs, size):
    """ builds a normalized auto-correlation matrix
        that has dimensions of size*size.
        
        Args:
            acfcoeffs (float array): the desired auto-correlation coefficients
            size (int): the size of the ultimate noise array
    """

    ans = zeros((size, size))
    k = len(acfcoeffs)
    m = min(k, size)  # Just in case k > size

    for i in range(m):
        for j in range(size - i):
            ans[j, j + i] = acfcoeffs[i]
            ans[j + i, j] = acfcoeffs[i]

    return ans


class CorrelatedNoiseGenerator:
    """ This correlated noise generator class takes advantage of the fact that the entries in the cholesky
        decomposition of the acf matrix rapidly approach limiting values.  This means that we do not need to build
        a large acf matrix: instead we make it large enough that the entries in the cholesky matrix have reached
        limiting values. We extract those limiting values along with a matching set of initial random numbers.
    """

    def __init__(self, acfcoeffs):
        """ Uses acfcoeffs and cholesky decomposition to calculate final_coeffs, the
            limiting values in the cholesky matrix columns. There will be as many such
            values as there are entries in acfcoeffs.

            An initial set of N[0,1] random numbers are generated and stored in r[].
            With this setup completed, correlated random number can be generated by:

                r[] convolve final_coeffs[]
        """

        if len(acfcoeffs) < 1:
            raise Exception("Invalid acfcoeffs array.")
        if acfcoeffs[0] != 1.0:
            raise Exception("Invalid acfcoeffs list; first entry not equal to 1.0")

        self.acf_length = len(acfcoeffs)

        # We only make the acf_matrix big enough to allow the subsequent cholesky
        # decomposition to reach limiting values. A size of 10 times the number of
        # acfcoeffs is more than adequate.
        self.acfmatrix = build_acf_matrix(acfcoeffs, size=self.acf_length * 10)

        self.noise_matrix = cholesky(self.acfmatrix, lower=False)
        # The noise_matrix is composed mostly of zeroes. For each column, there
        # will be as many non-zero entries as there are in acfcoeffs. The limiting
        # values are in the bottom of the last column.
        self.final_coeffs = self.noise_matrix[-self.acf_length:, -1]

    def corr_normal(self, num_values):
        """ Calculates and returns a NumPy ndarray of length
            num_values. The values are normally distributed with a mean of
            zero, a standard deviation of 1, and an auto-correlation that
            closely approximates the values given by acfcoeffs when this
            object was instantiated.

            Args:
                num_values (int): the desired length of the output array
        """

        return convolve(self.final_coeffs, random.normal(size=num_values), 'same')
