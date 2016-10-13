# -*- coding: utf-8 -*-

import unittest

from steenzout.object import Object


class ObjectTestCase(unittest.TestCase):
    """Test case for the Object class."""

    def test_hash(self):
        """Test for the __hash__ function."""

        o1 = Object()
        o2 = Object()
        a = object()

        self.assertEqual(hash(o1), hash(o2))
        self.assertNotEqual(hash(o1), hash(a))

    def test_eq(self):
        """Test for the __eq__ function."""

        o1 = Object()
        o2 = Object()
        a = object()

        self.assertTrue(o1 == o1)
        self.assertTrue(o1 == o2)

        self.assertFalse(id(o1) == id(o2))
        self.assertFalse(o1 == a)

    def test_neq(self):
        """Test for the __neq__ function."""

        o1 = Object()
        o2 = Object()
        a = object()

        self.assertFalse(o1 != o1)
        self.assertFalse(o1 != o2)

        self.assertTrue(o1 != a)

    def test_repr(self):
        """Test for the __repr__ function."""
        o1 = Object()

        self.assertEqual("<class 'steenzout.object.Object'>({})", repr(o1))

    def test_str(self):
        """Test for the __str__ function."""
        o1 = Object()
        self.assertEqual(str(o1), 'steenzout.object.Object')

        class Mock(Object):
            def __init__(self):
                self.x = 1
                self.y = 'a'
                self.l = ['a']
                self.d = {'a': 1}
                self.b = True

        m1 = Mock()
        assert str(m1) == 'tests.object_test.Mock b=True d={\'a\': 1} l=[\'a\'] x=1 y=a'
