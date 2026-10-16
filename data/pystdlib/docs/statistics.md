# statistics

## statistics.LinearRegression(slope, intercept)

LinearRegression(slope, intercept)

## statistics.NormalDist(mu=0.0, sigma=1.0)

Normal distribution of a random variable

## statistics.NormalDist.cdf(self, x)

Cumulative distribution function. P(X <= x)

## statistics.NormalDist.from_samples(...)

Make a normal distribution instance from sample data.

## statistics.NormalDist.inv_cdf(self, p)

Finds the value of the random variable such that the probability of
the variable being less than or equal to that value equals the given
probability.

This function is also called the percent point function or quantile
function.

## statistics.NormalDist.overlap(self, other)

Measures the agreement between two normal probability distributions.
Returns a value between 0.0 and 1.0 giving the overlapping area in
the two underlying probability density functions.

>>> N1 = NormalDist(2.4, 1.6)
    >>> N2 = NormalDist(3.2, 2.0)
    >>> N1.overlap(N2)
    0.8035050657330205

## statistics.NormalDist.pdf(self, x)

Probability density function. P(x <= X < x+dx) / dx

## statistics.NormalDist.quantiles(self, n=4)

Returns a list of (n - 1) cut points separating the intervals.

Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
Set *n* to 100 for percentiles which gives the 99 cuts points that
separate the normal distribution in to 100 equal sized groups.

## statistics.NormalDist.samples(self, n, *, seed=None)

Generate *n* samples for a given mean and standard deviation.

## statistics.NormalDist.zscore(self, x)

Compute the Standard Score. (x - mean) / stdev

Describes *x* in terms of the number of standard deviations
above or below the mean of the normal distribution.

## statistics.correlation(x, y, /, *, method='linear')

Pearson's correlation coefficient Return the Pearson's correlation coefficient for two inputs. Pearson's
correlation coefficient *r* takes values between -1 and +1. It measures
the strength and direction of a linear relationship.

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> correlation(x, x)
1.0
>>> correlation(x, y)
-1.0

If *method* is "ranked", computes Spearman's rank correlation coefficient
for two inputs.  The data is replaced by ranks.  Ties are averaged
so that equal values receive the same rank.  The resulting coefficient
measures the strength of a monotonic relationship.

Spearman's rank correlation coefficient is appropriate for ordinal
data or for continuous data that doesn't meet the linear proportion
requirement for Pearson's correlation coefficient.

## statistics.covariance(x, y, /)

Covariance Return the sample covariance of two inputs *x* and *y*. Covariance
is a measure of the joint variability of two inputs.

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> covariance(x, y)
0.75
>>> z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> covariance(x, z)
-7.5
>>> covariance(z, x)
-7.5

## statistics.fmean(data, weights=None)

This runs faster than the mean() function and it always returns a float.
If the input dataset is empty, it raises a StatisticsError.

>>> fmean([3.5, 4.0, 5.25])
4.25

## statistics.geometric_mean(data)

Raises a StatisticsError if the input dataset is empty
or if it contains a negative value.

Returns zero if the product of inputs is zero.

No special efforts are made to achieve exact results.
(However, this may change in the future.)

>>> round(geometric_mean([54, 24, 36]), 9)
36.0

## statistics.harmonic_mean(data, weights=None)

The harmonic mean is the reciprocal of the arithmetic mean of the
reciprocals of the data.  It can be used for averaging ratios or
rates, for example speeds.

Suppose a car travels 40 km/hr for 5 km and then speeds-up to
60 km/hr for another 5 km. What is the average speed?

>>> harmonic_mean([40, 60])
    48.0

Suppose a car travels 40 km/hr for 5 km, and when traffic clears,
speeds-up to 60 km/hr for the remaining 30 km of the journey. What
is the average speed?

>>> harmonic_mean([40, 60], weights=[5, 30])
    56.0

If ``data`` is empty, or any element is less than zero,
``harmonic_mean`` will raise ``StatisticsError``.

## statistics.kde(data, h, kernel='normal', *, cumulative=False)

The basic idea is to smooth the data using a kernel function
to help draw inferences about a population from a sample.

The degree of smoothing is controlled by the scaling parameter h
which is called the bandwidth.  Smaller values emphasize local
features while larger values give smoother results.

The kernel determines the relative weights of the sample data
points.  Generally, the choice of kernel shape does not matter
as much as the more influential bandwidth smoothing parameter.

Kernels that give some weight to every sample point:

normal (gauss)
   logistic
   sigmoid

Kernels that only give weight to sample points within
the bandwidth:

rectangular (uniform)
   triangular
   parabolic (epanechnikov)
   quartic (biweight)
   triweight
   cosine

If *cumulative* is true, will return a cumulative distribution function.

A StatisticsError will be raised if the data sequence is empty.

Example
-------

Given a sample of six data points, construct a continuous
function that estimates the underlying probability density:

>>> sample = [-2.1, -1.3, -0.4, 1.9, 5.1, 6.2]
    >>> f_hat = kde(sample, h=1.5)

Compute the area under the curve:

>>> area = sum(f_hat(x) for x in range(-20, 20))
    >>> round(area, 4)
    1.0

Plot the estimated probability density function at
evenly spaced points from -6 to 10:

>>> for x in range(-6, 11):
    ...     density = f_hat(x)
    ...     plot = ' ' * int(density * 400) + 'x'
    ...     print(f'{x:2}: {density:.3f} {plot}')
    ...
    -6: 0.002 x
    -5: 0.009    x
    -4: 0.031             x
    -3: 0.070                             x
    -2: 0.111                                             x
    -1: 0.125                                                   x
     0: 0.110                                            x
     1: 0.086                                   x
     2: 0.068                            x
     3: 0.059                        x
     4: 0.066                           x
     5: 0.082                                 x
     6: 0.082                                 x
     7: 0.058                        x
     8: 0.028            x
     9: 0.009    x
    10: 0.002 x

Estimate P(4.5 < X <= 7.5), the probability that a new sample value
will be between 4.5 and 7.5:

>>> cdf = kde(sample, h=1.5, cumulative=True)
    >>> round(cdf(7.5) - cdf(4.5), 2)
    0.22

References
----------

Kernel density estimation and its application:
https://www.itm-conferences.org/articles/itmconf/pdf/2018/08/itmconf_sam2018_00037.pdf

Kernel functions in common use:
https://en.wikipedia.org/wiki/Kernel_(statistics)#kernel_functions_in_common_use

Interactive graphical demonstration and exploration:
https://demonstrations.wolfram.com/KernelDensityEstimation/

Kernel estimation of cumulative distribution function of a random variable with bounded support
https://www.econstor.eu/bitstream/10419/207829/1/10.21307_stattrans-2016-037.pdf

## statistics.kde_random(data, h, kernel='normal', *, seed=None)

Providing a *seed* allows reproducible selections within a single
thread.  The seed may be an integer, float, str, or bytes.

A StatisticsError will be raised if the *data* sequence is empty.

Example:

>>> data = [-2.1, -1.3, -0.4, 1.9, 5.1, 6.2]
>>> rand = kde_random(data, h=1.5, seed=8675309)
>>> new_selections = [rand() for i in range(10)]
>>> [round(x, 1) for x in new_selections]
[0.7, 6.2, 1.2, 6.9, 7.0, 1.8, 2.5, -0.5, -1.8, 5.6]

## statistics.linear_regression(x, y, /, *, proportional=False)

Return the slope and intercept of simple linear regression
parameters estimated using ordinary least squares. Simple linear
regression describes relationship between an independent variable
*x* and a dependent variable *y* in terms of a linear function:

y = slope * x + intercept + noise

where *slope* and *intercept* are the regression parameters that are
estimated, and noise represents the variability of the data that was
not explained by the linear regression (it is equal to the
difference between predicted and actual values of the dependent
variable).

The parameters are returned as a named tuple.

>>> x = [1, 2, 3, 4, 5]
>>> noise = NormalDist().samples(5, seed=42)
>>> y = [3 * x[i] + 2 + noise[i] for i in range(5)]
>>> linear_regression(x, y)  #doctest: +ELLIPSIS
LinearRegression(slope=3.17495..., intercept=1.00925...)

If *proportional* is true, the independent variable *x* and the
dependent variable *y* are assumed to be directly proportional.
The data is fit to a line passing through the origin.

Since the *intercept* will always be 0.0, the underlying linear
function simplifies to:

y = slope * x + noise

>>> y = [3 * x[i] + noise[i] for i in range(5)]
>>> linear_regression(x, y, proportional=True)  #doctest: +ELLIPSIS
LinearRegression(slope=2.90475..., intercept=0.0)

## statistics.mean(data)

>>> mean([1, 2, 3, 4, 4])
2.8

>>> from fractions import Fraction as F
>>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
Fraction(13, 21)

>>> from decimal import Decimal as D
>>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
Decimal('0.5625')

If ``data`` is empty, StatisticsError will be raised.

## statistics.median(data)

When the number of data points is odd, return the middle data point.
When the number of data points is even, the median is interpolated by
taking the average of the two middle values:

>>> median([1, 3, 5])
3
>>> median([1, 3, 5, 7])
4.0

## statistics.median_grouped(data, interval=1.0)

The *data* can be any iterable of numeric data with each value being
exactly the midpoint of a bin.  At least one value must be present.

The *interval* is width of each bin.

For example, demographic information may have been summarized into
consecutive ten-year age groups with each group being represented
by the 5-year midpoints of the intervals:

>>> demographics = Counter({
    ...    25: 172,   # 20 to 30 years old
    ...    35: 484,   # 30 to 40 years old
    ...    45: 387,   # 40 to 50 years old
    ...    55:  22,   # 50 to 60 years old
    ...    65:   6,   # 60 to 70 years old
    ... })

The 50th percentile (median) is the 536th person out of the 1071
member cohort.  That person is in the 30 to 40 year old age group.

The regular median() function would assume that everyone in the
tricenarian age group was exactly 35 years old.  A more tenable
assumption is that the 484 members of that age group are evenly
distributed between 30 and 40.  For that, we use median_grouped().

>>> data = list(demographics.elements())
    >>> median(data)
    35
    >>> round(median_grouped(data, interval=10), 1)
    37.5

The caller is responsible for making sure the data points are separated
by exact multiples of *interval*.  This is essential for getting a
correct result.  The function does not check this precondition.

Inputs may be any numeric type that can be coerced to a float during
the interpolation step.

## statistics.median_high(data)

When the number of data points is odd, the middle value is returned.
When it is even, the larger of the two middle values is returned.

>>> median_high([1, 3, 5])
3
>>> median_high([1, 3, 5, 7])
5

## statistics.median_low(data)

When the number of data points is odd, the middle value is returned.
When it is even, the smaller of the two middle values is returned.

>>> median_low([1, 3, 5])
3
>>> median_low([1, 3, 5, 7])
3

## statistics.mode(data)

``mode`` assumes discrete data, and returns a single value. This is the
standard treatment of the mode as commonly taught in schools:

>>> mode([1, 1, 2, 3, 3, 3, 3, 4])
    3

This also works with nominal (non-numeric) data:

>>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
    'red'

If there are multiple modes with same frequency, return the first one
encountered:

>>> mode(['red', 'red', 'green', 'blue', 'blue'])
    'red'

If *data* is empty, ``mode``, raises StatisticsError.

## statistics.multimode(data)

Will return more than one result if there are multiple modes
or an empty list if *data* is empty.

>>> multimode('aabbbbbbbbcc')
['b']
>>> multimode('aabbbbccddddeeffffgg')
['b', 'd', 'f']
>>> multimode('')
[]

## statistics.pstdev(data, mu=None)

Return the square root of the population variance. See ``pvariance`` for arguments and other details.

>>> pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
0.986893273527251

## statistics.pvariance(data, mu=None)

data should be a sequence or iterable of Real-valued numbers, with at least one
value. The optional argument mu, if given, should be the mean of
the data. If it is missing or None, the mean is automatically calculated.

Use this function to calculate the variance from the entire population.
To estimate the variance from a sample, the ``variance`` function is
usually a better choice.

Examples:

>>> data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
>>> pvariance(data)
1.25

If you have already calculated the mean of the data, you can pass it as
the optional second argument to avoid recalculating it:

>>> mu = mean(data)
>>> pvariance(data, mu)
1.25

Decimals and Fractions are supported:

>>> from decimal import Decimal as D
>>> pvariance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
Decimal('24.815')

>>> from fractions import Fraction as F
>>> pvariance([F(1, 4), F(5, 4), F(1, 2)])
Fraction(13, 72)

## statistics.quantiles(data, *, n=4, method='exclusive')

Returns a list of (n - 1) cut points separating the intervals.

Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
Set *n* to 100 for percentiles which gives the 99 cuts points that
separate *data* in to 100 equal sized groups.

The *data* can be any iterable containing sample.
The cut points are linearly interpolated between data points.

If *method* is set to *inclusive*, *data* is treated as population
data.  The minimum value is treated as the 0th percentile and the
maximum value is treated as the 100th percentile.

## statistics.stdev(data, xbar=None)

Return the square root of the sample variance. See ``variance`` for arguments and other details.

>>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
1.0810874155219827

## statistics.variance(data, xbar=None)

data should be an iterable of Real-valued numbers, with at least two
values. The optional argument xbar, if given, should be the mean of
the data. If it is missing or None, the mean is automatically calculated.

Use this function when your data is a sample from a population. To
calculate the variance from the entire population, see ``pvariance``.

Examples:

>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> variance(data)
1.3720238095238095

If you have already calculated the mean of your data, you can pass it as
the optional second argument ``xbar`` to avoid recalculating it:

>>> m = mean(data)
>>> variance(data, m)
1.3720238095238095

This function does not check that ``xbar`` is actually the mean of
``data``. Giving arbitrary values for ``xbar`` may lead to invalid or
impossible results.

Decimals and Fractions are supported:

>>> from decimal import Decimal as D
>>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
Decimal('31.01875')

>>> from fractions import Fraction as F
>>> variance([F(1, 6), F(1, 2), F(5, 3)])
Fraction(67, 108)
