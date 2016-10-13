# -*- coding: utf-8 -*-
#
# Copyright 2016 Pedro Salgado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Object module."""

import itertools
import threading


from steenzout.object.version import __version__


class Object(object):
    """Object class with a `__hash__`, `__eq__`, `__ne__` and `__repr__` implementation."""

    def __hash__(self):
        """Called by built-in function :function:`object.__hash__`.

        See :py:function:`object.__hash__`.

        Returns:
            (integer): hash value.
        """
        return hash(tuple(sorted(self.__dict__.items())))

    def __eq__(self, other):
        """Rich comparison function for the `==` operator.

        Args:
            other (:py:class:`Object`): instance to be compared against.

        Raises:
            :py:class:`exceptions.NotImplementedError` when
                the `other` instance is not a `Object` object.

        Returns:
            (bool): True in case both instances represent the same object;
                False otherwise.
        """
        if other is self:
            return True
        elif isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

    def __ne__(self, other):
        """Rich comparison function for the `!=` operator.

        Args:
            other (:py:class:`Object`): instance to be compared against.

        Raises:
            :class:`exceptions.NotImplementedError` when
                the `other` instance is not a `Object` object.

        Returns:
            (bool) True in case `self` and `other`
            do not represent the same object; False otherwise.
        """
        if isinstance(other, self.__class__):
            return not self == other
        return NotImplemented

    def __repr__(self):
        """Return the “official” string representation of this object.

        Returns:
            (str): the “official” string representation of this object.
        """
        return '%s(%r)' % (self.__class__, self.__dict__)

    def __str__(self):
        """Returns the "informal" string representation of this object

        Returns:
            (str): the "informal" string representation of this object.
        """
        return ' '.join(itertools.chain(
            ('%s.%s' % (self.__class__.__module__, self.__class__.__name__),),
            ('%s=%s' % x for x in sorted(self.__dict__.items()))))


class Singleton(type):
    """Singleton metaclass."""

    instance = None

    def __call__(cls, *args, **kwargs):
        """Return singleton instance.

        Args:
            cls: the class.
            args: initializer function arguments.
            kwargs: initializer function keyword arguments.
        """
        if cls.instance is None:
            with threading.Lock():
                if cls.instance is None:
                    cls.instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.instance


def version():
    """Return this package version.

    Returns:
        (str): package version.
    """
    return __version__
