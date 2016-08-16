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
"""
.. module:: steenzout.object
    :synopsis: Python object package.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""

from steenzout.object.version import __version__


class Object(object):
    """
    Object class with a `__hash__`, `__eq__` and `__ne__` implementation.
    """

    def __hash__(self):
        """
        Called by built-in function :function:`object.__hash__` and
        for operations on members of hashed collections
        (see :function:`object.__hash__`).

        :return: hash value.
        :rtype: integer
        """
        return hash(tuple(sorted(self.__dict__.items())))

    def __eq__(self, other):
        """
        Rich comparison function for the `==` operator.

        :param other: instance to be compared against.
        :type other: :class:`Object`.

        :raises: :class:`exceptions.NotImplementedError`
            in case the `other` instance is not a `Object` object.

        :return: True in case both instances represent the same object;
            False otherwise.
        :rtype: bool
        """
        if other is self:
            return True
        elif isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

    def __ne__(self, other):
        """
        Rich comparison function for the `!=` operator.

        :param other: instance to be compared against.
        :type other: :class:`Object`.

        :raises: :class:`exceptions.NotImplementedError`
            in case the `other` instance is not a `Object` object.

        :return: True in case `self` and `other`
            do not represent the same object; False otherwise.
        :rtype: bool
        """
        if isinstance(other, self.__class__):
            return not self == other
        return NotImplemented
