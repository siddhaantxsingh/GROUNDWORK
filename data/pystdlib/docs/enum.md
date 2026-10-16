# enum

## enum.Enum(new_class_name, /, names, *, module=None, qualname=None, type=None, start=1, boundary=None)

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
  <Color.RED: 1>

- value lookup:

>>> Color(1)
  <Color.RED: 1>

- name lookup:

>>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.

## enum.EnumCheck(*values)

various conditions to check an enumeration for

## enum.EnumDict(cls_name=None)

Track enum member order and ensure member names are not reused. EnumType will use the names found in self._member_names as the
enumeration member names.

## enum.EnumMeta(cls, bases, classdict, *, boundary=None, _simple=False, **kwds)

Metaclass for Enum

## enum.EnumType(cls, bases, classdict, *, boundary=None, _simple=False, **kwds)

Metaclass for Enum

## enum.Flag(new_class_name, /, names, *, module=None, qualname=None, type=None, start=1, boundary=None)

Support for flags

## enum.FlagBoundary(*values)

control how out of range values are handled "strict" -> error is raised [default for Flag] "conform" -> extra bits are discarded "eject" -> lose flag status "keep" -> keep flag status and all bits [default for IntFlag]

## enum.IntEnum(new_class_name, /, names, *, module=None, qualname=None, type=None, start=1, boundary=None)

Enum where members are also (and must be) ints

## enum.IntFlag(new_class_name, /, names, *, module=None, qualname=None, type=None, start=1, boundary=None)

Support for integer-based Flags

## enum.ReprEnum(new_class_name, /, names, *, module=None, qualname=None, type=None, start=1, boundary=None)

Only changes the repr(), leaving str() and format() to the mixed-in type.

## enum.StrEnum(new_class_name, /, names, *, module=None, qualname=None, type=None, start=1, boundary=None)

Enum where members are also (and must be) strings

## enum.auto(value=_auto_null)

Instances are replaced with an appropriate value in Enum class suites.

## enum.bin(num, max_bits=None)

Like built-in bin(), except negative values are represented in twos-complement, and the leading bit always indicates sign (0=positive, 1=negative). >>> bin(10)
'0b0 1010'
>>> bin(~10)   # ~10 is -11
'0b1 0101'

## enum.global_enum(cls, update_str=False)

decorator that makes the repr() of an enum member reference its module instead of its class; also exports all members to the enum's module's global namespace

## enum.global_enum_repr(self)

use module.enum_name instead of class.enum_name the module is the last module in case of a multi-module name

## enum.global_flag_repr(self)

use module.flag_name instead of class.flag_name the module is the last module in case of a multi-module name

## enum.global_str(self)

use enum_name instead of class.enum_name

## enum.member(value)

Forces item to become an Enum member during class creation.

## enum.nonmember(value)

Protects item from becoming an Enum member during class creation.

## enum.property(fget=None, fset=None, fdel=None, doc=None)

Instance access is the same as property(), but access to an attribute through the enum class will instead look in the class' _member_map_ for a corresponding enum member.

## enum.unique(enumeration)

Class decorator for enumerations ensuring unique member values.

## enum.verify(*checks)

Check an enumeration for various constraints. (see EnumCheck)
