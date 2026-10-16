# abc

## abc.ABC()

Helper class that provides a standard way to create an ABC using inheritance.

## abc.ABCMeta(name, bases, namespace, /, **kwargs)

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).

## abc.ABCMeta.register(cls, subclass)

Register a virtual subclass of an ABC. Returns the subclass, to allow usage as a class decorator.

## abc.abstractclassmethod(callable)

A decorator indicating abstract classmethods. Deprecated, use 'classmethod' with 'abstractmethod' instead:

class C(ABC):
        @classmethod
        @abstractmethod
        def my_abstract_classmethod(cls, ...):
            ...

## abc.abstractmethod(funcobj)

A decorator indicating abstract methods. Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.  abstractmethod() may be used to declare
abstract methods for properties and descriptors.

Usage:

class C(metaclass=ABCMeta):
        @abstractmethod
        def my_abstract_method(self, arg1, arg2, argN):
            ...

## abc.abstractproperty(fget=None, fset=None, fdel=None, doc=None)

A decorator indicating abstract properties. Deprecated, use 'property' with 'abstractmethod' instead:

class C(ABC):
        @property
        @abstractmethod
        def my_abstract_property(self):
            ...

## abc.abstractstaticmethod(callable)

A decorator indicating abstract staticmethods. Deprecated, use 'staticmethod' with 'abstractmethod' instead:

class C(ABC):
        @staticmethod
        @abstractmethod
        def my_abstract_staticmethod(...):
            ...

## abc.update_abstractmethods(cls)

If a class has had one of its abstract methods implemented after the
class was created, the method will not be considered implemented until
this function is called. Alternatively, if a new abstract method has been
added to the class, it will only be considered an abstract method of the
class after this function is called.

This function should be called before any use is made of the class,
usually in class decorators that add methods to the subject class.

Returns cls, to allow usage as a class decorator.

If cls is not an instance of ABCMeta, does nothing.
