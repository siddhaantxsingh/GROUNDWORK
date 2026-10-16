# random

## random.Random(x=None)

Used to instantiate instances of Random to get generators that don't
share state.

Class Random can also be subclassed if you want to use a different basic
generator of your own devising: in that case, override the following
methods:  random(), seed(), getstate(), and setstate().
Optionally, implement a getrandbits() method so that randrange()
can cover arbitrarily large ranges.

## random.Random.betavariate(self, alpha, beta)

Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0.
Returned values range between 0 and 1.

The mean (expected value) and variance of the random variable are:

E[X] = alpha / (alpha + beta)
    Var[X] = alpha * beta / ((alpha + beta)**2 * (alpha + beta + 1))

## random.Random.binomialvariate(self, n=1, p=0.5)

Binomial random variable. Gives the number of successes for *n* independent trials
with the probability of success in each trial being *p*:

sum(random() < p for i in range(n))

Returns an integer in the range:   0 <= X <= n

The mean (expected value) and variance of the random variable are:

E[X] = n * p
    Var[x] = n * p * (1 - p)

## random.Random.choice(self, seq)

Choose a random element from a non-empty sequence.

## random.Random.choices(self, population, weights=None, *, cum_weights=None, k=1)

Return a k sized list of population elements chosen with replacement. If the relative weights or cumulative weights are not specified,
the selections are made with equal probability.

## random.Random.expovariate(self, lambd=1.0)

Exponential distribution. lambd is 1.0 divided by the desired mean.  It should be
nonzero.  (The parameter would be called "lambda", but that is
a reserved word in Python.)  Returned values range from 0 to
positive infinity if lambd is positive, and from negative
infinity to 0 if lambd is negative.

The mean (expected value) and variance of the random variable are:

E[X] = 1 / lambd
    Var[X] = 1 / lambd ** 2

## random.Random.gammavariate(self, alpha, beta)

Gamma distribution. Not the gamma function!

Conditions on the parameters are alpha > 0 and beta > 0.

The probability distribution function is:

x ** (alpha - 1) * math.exp(-x / beta)
  pdf(x) =  --------------------------------------
              math.gamma(alpha) * beta ** alpha

The mean (expected value) and variance of the random variable are:

E[X] = alpha * beta
    Var[X] = alpha * beta ** 2

## random.Random.gauss(self, mu=0.0, sigma=1.0)

Gaussian distribution. mu is the mean, and sigma is the standard deviation.  This is
slightly faster than the normalvariate() function.

Not thread-safe without a lock around calls.

## random.Random.getstate(self)

Return internal state; can be passed to setstate() later.

## random.Random.lognormvariate(self, mu, sigma)

Log normal distribution. If you take the natural logarithm of this distribution, you'll get a
normal distribution with mean mu and standard deviation sigma.
mu can have any value, and sigma must be greater than zero.

## random.Random.normalvariate(self, mu=0.0, sigma=1.0)

Normal distribution. mu is the mean, and sigma is the standard deviation.

## random.Random.paretovariate(self, alpha)

Pareto distribution. alpha is the shape parameter.

## random.Random.randbytes(self, n)

Generate n random bytes.

## random.Random.randint(self, a, b)

Return random integer in range [a, b], including both end points.

## random.Random.randrange(self, start, stop=None, step=1)

Choose a random item from range(stop) or range(start, stop[, step]). Roughly equivalent to ``choice(range(start, stop, step))`` but
supports arbitrarily large ranges and is optimized for common cases.

## random.Random.sample(self, population, k, *, counts=None)

Returns a new list containing elements from the population while
leaving the original population unchanged.  The resulting list is
in selection order so that all sub-slices will also be valid random
samples.  This allows raffle winners (the sample) to be partitioned
into grand prize and second place winners (the subslices).

Members of the population need not be hashable or unique.  If the
population contains repeats, then each occurrence is a possible
selection in the sample.

Repeated elements can be specified one at a time or with the optional
counts parameter.  For example:

sample(['red', 'blue'], counts=[4, 2], k=5)

is equivalent to:

sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)

To choose a sample from a range of integers, use range() for the
population argument.  This is especially fast and space efficient
for sampling from a large population:

sample(range(10000000), 60)

## random.Random.seed(self, a=None, version=2)

The only supported seed types are None, int, float,
str, bytes, and bytearray.

None or no argument seeds from current time or from an operating
system specific randomness source if available.

If *a* is an int, all bits are used.

For version 2 (the default), all of the bits are used if *a* is a str,
bytes, or bytearray.  For version 1 (provided for reproducing random
sequences from older versions of Python), the algorithm for str and
bytes generates a narrower range of seeds.

## random.Random.setstate(self, state)

Restore internal state from object returned by getstate().

## random.Random.shuffle(self, x)

Shuffle list x in place, and return None.

## random.Random.triangular(self, low=0.0, high=1.0, mode=None)

Triangular distribution. Continuous distribution bounded by given lower and upper limits,
and having a given mode value in-between.

http://en.wikipedia.org/wiki/Triangular_distribution

The mean (expected value) and variance of the random variable are:

E[X] = (low + high + mode) / 3
    Var[X] = (low**2 + high**2 + mode**2 - low*high - low*mode - high*mode) / 18

## random.Random.uniform(self, a, b)

The mean (expected value) and variance of the random variable are:

E[X] = (a + b) / 2
    Var[X] = (b - a) ** 2 / 12

## random.Random.vonmisesvariate(self, mu, kappa)

Circular data distribution. mu is the mean angle, expressed in radians between 0 and 2*pi, and
kappa is the concentration parameter, which must be greater than or
equal to zero.  If kappa is equal to zero, this distribution reduces
to a uniform random angle over the range 0 to 2*pi.

## random.Random.weibullvariate(self, alpha, beta)

Weibull distribution. alpha is the scale parameter and beta is the shape parameter.

## random.SystemRandom(x=None)

Alternate random number generator using sources provided by the operating system (such as /dev/urandom on Unix or CryptGenRandom on Windows). Not available on all systems (see os.urandom() for details).

## random.SystemRandom.getrandbits(self, k)

getrandbits(k) -> x. Generates an int with k random bits.

## random.SystemRandom.getstate(self, *args, **kwds)

Method should not be called for a system random number generator.

## random.SystemRandom.randbytes(self, n)

Generate n random bytes.

## random.SystemRandom.random(self)

Get the next random number in the range 0.0 <= X < 1.0.

## random.SystemRandom.seed(self, *args, **kwds)

Stub method. Not used for a system random number generator.

## random.SystemRandom.setstate(self, *args, **kwds)

Method should not be called for a system random number generator.
