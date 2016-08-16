The :py:mod:`steenzout.object` package provides an
:py:class:`Object <steenzout.object.Object>` class with
pre-defined
:py:meth:`__hash__<steenzout.object.Object.__hash__>`,
:py:meth:`__eq__<steenzout.object.Object.__eq__>` and
:py:meth:`__ne__<steenzout.object.Object.__ne__>` functions.

What's the difference to the :py:class:`object` class?

Example::

   >>> o1 = object()
   >>> o2 = object()
   >>>
   >>> assert o1 == o2
   >>> Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AssertionError

If you use :py:class:`Object <steenzout.object.Object>`::

   >>> from steenzout.object import Object
   >>>
   >>> o1 = Object()
   >>> o2 = Object()
   >>>
   >>> assert o1 == o2

If you sub-class the :py:class:`Object <steenzout.object.Object>` class,
``==`` and ``!=`` will still work as expected::

   >>> class A(Object):
   >>>     pass
   ...
   ...

   >>> class B(Object):
   >>>     pass
   ...
   ...

   >>> a = A()
   >>> b = B()

   >>> a == b
   >>> False

   >>> a != b
   >>> True
