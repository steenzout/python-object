# python-object

[![pypi](https://img.shields.io/pypi/v/steenzout.object.svg)](https://pypi.python.org/pypi/steenzout.object/)
[![Build Status](https://travis-ci.org/steenzout/python-object.svg?branch=master)](https://travis-ci.org/steenzout/python-object)
[![Code Health](https://landscape.io/github/steenzout/python-object/master/landscape.svg?style=flat)](https://landscape.io/github/steenzout/python-object/master)
[![Coverage Status](https://coveralls.io/repos/github/steenzout/python-object/badge.svg?branch=master)](https://coveralls.io/r/steenzout/python-object)
[![Requirements Status](https://requires.io/github/steenzout/python-object/requirements.svg?branch=master)](https://requires.io/github/steenzout/python-object/requirements/?branch=master)
[![Documentation Status](https://readthedocs.org/projects/python-steenzout-object/badge/?version=latest)](http://python-steenzout-object.readthedocs.io/en/latest/?badge=latest)

[![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg?style=flat)][license]
[![Project Stats](https://www.openhub.net/p/python-steenzout-object/widgets/project_thin_badge.gif)](https://www.openhub.net/p/python-steenzout-object/)

The `steenzout.object` package provides an `Object` class with
pre-defined `__hash__`, `__eq__` and `__ne__` functions.

What's the difference to the `object` class?

Example:

```
>>> o1 = object()
>>> o2 = object()
>>> 
>>> assert o1 == o2
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

If you use `steenzout.object.Object`:

```
>>> from steenzout.object import Object
>>> 
>>> o1 = Object()
>>> o2 = Object()
>>> 
>>> assert o1 == o2
>>>
```

If you sub-class the `Object` class,
`==` and `!=` will still work as expected:

```
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
```


## Test

```
$ tox
```

## Documentation

```
$ tox -e docs
```


## Links

- [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html)
- [stackoverflow > Elegant ways to support equivalence (“equality”) in Python classes](http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes)

[license]:  https://raw.githubusercontent.com/steenzout/python-object/master/LICENSE    "License"
