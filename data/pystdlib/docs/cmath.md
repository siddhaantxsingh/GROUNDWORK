# cmath

## cmath.acos(z, /)

Return the arc cosine of z.

## cmath.acosh(z, /)

Return the inverse hyperbolic cosine of z.

## cmath.asin(z, /)

Return the arc sine of z.

## cmath.asinh(z, /)

Return the inverse hyperbolic sine of z.

## cmath.atan(z, /)

Return the arc tangent of z.

## cmath.atanh(z, /)

Return the inverse hyperbolic tangent of z.

## cmath.cos(z, /)

Return the cosine of z.

## cmath.cosh(z, /)

Return the hyperbolic cosine of z.

## cmath.exp(z, /)

Return the exponential value e**z.

## cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

rel_tol
    maximum difference for being considered "close", relative to the
    magnitude of the input values
  abs_tol
    maximum difference for being considered "close", regardless of the
    magnitude of the input values

Return True if a is close in value to b, and False otherwise.

For the values to be considered close, the difference between them must
be smaller than at least one of the tolerances.

-inf, inf and NaN behave similarly to the IEEE 754 Standard.  That is,
NaN is not close to anything, even itself. inf and -inf are only close
to themselves.

## cmath.isfinite(z, /)

Return True if both the real and imaginary parts of z are finite, else False.

## cmath.isinf(z, /)

Checks if the real or imaginary part of z is infinite.

## cmath.isnan(z, /)

Checks if the real or imaginary part of z not a number (NaN).

## cmath.log(...)

If the base is not specified, returns the natural logarithm (base e) of z.

## cmath.log10(z, /)

Return the base-10 logarithm of z.

## cmath.phase(z, /)

Return argument, also known as the phase angle, of a complex.

## cmath.polar(z, /)

Convert a complex from rectangular coordinates to polar coordinates. r is the distance from 0 and phi the phase angle.

## cmath.rect(r, phi, /)

Convert from polar coordinates to rectangular coordinates.

## cmath.sin(z, /)

Return the sine of z.

## cmath.sinh(z, /)

Return the hyperbolic sine of z.

## cmath.sqrt(z, /)

Return the square root of z.

## cmath.tan(z, /)

Return the tangent of z.

## cmath.tanh(z, /)

Return the hyperbolic tangent of z.
