# -*- coding: utf-8 -*-

"""
.. module:: steenzout.object.tests
    :synopsis: Test cases for the steenzout.object package.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""

# -*- coding: utf-8 -*-

import unittest

from steenzout.object import Object


class MockA(Object):
    pass


class MockB(object):
    pass


class ObjectTestCase(unittest.TestCase):
    """Test case for the Object class."""

    def test_hash(self):
        """Test for the __hash__ function."""

        o1 = Object()
        o2 = Object()
        a = MockA()

        self.assertEqual(hash(o1), hash(o2))
        self.assertNotEqual(hash(o1), hash(a))

    def test_eq(self):
        """Test for the __eq__ function."""

        o1 = Object()
        o2 = Object()
        a = MockA()

        self.assertTrue(o1 == o1)
        self.assertTrue(o1 == o2)

        self.assertFalse(id(o1) == id(o2))
        self.assertFalse(o1 == a)

    def test_neq(self):
        """Test for the __neq__ function."""

        o1 = Object()
        o2 = Object()
        a = MockA()

        self.assertFalse(o1 != o1)
        self.assertFalse(o1 != o2)

        self.assertTrue(o1 != a)
