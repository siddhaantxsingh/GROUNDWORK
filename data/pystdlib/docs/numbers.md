# numbers

## numbers.Complex()

In short, those are: a conversion to complex, .real, .imag, +, -,
*, /, **, abs(), .conjugate, ==, and !=.

If it is given heterogeneous arguments, and doesn't have special
knowledge about them, it should fall back to the builtin complex
type as described below.

## numbers.Complex.conjugate(self)

(x+y*i).conjugate() returns (x-y*i).

## numbers.Integral()

Integral adds methods that work on integral numbers. In short, these are conversion to int, pow with modulus, and the
bit-string operations.

## numbers.Number()

All numbers inherit from this class. If you just want to check if an argument x is a number, without
caring what kind, use isinstance(x, Number).

## numbers.Rational()

To Real, Rational adds numerator and denominator properties. The numerator and denominator values should be in lowest terms,
with a positive denominator.

## numbers.Real()

To Complex, Real adds the operations that work on real numbers. In short, those are: a conversion to float, trunc(), divmod,
%, <, <=, >, and >=.

Real also provides defaults for the derived operations.

## numbers.Real.conjugate(self)

Conjugate is a no-op for Reals.
