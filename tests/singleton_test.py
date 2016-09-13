# -*- coding: utf-8 -*-

import unittest

from six import with_metaclass
from steenzout.object import Object, Singleton


class MockSingleton1(Object, with_metaclass(Singleton)):

    def __init__(self, value):
        super(MockSingleton1, self).__init__()
        self.attr = value


class MockSingleton2(Object, with_metaclass(Singleton)):

    def __init__(self, value):
        super(MockSingleton2, self).__init__()
        self.attr = value


class SingletonTestCase(unittest.TestCase):
    """Test case for the Singleton class."""

    def test(self):
        x = MockSingleton1(1)
        y = MockSingleton1(1)

        self.assertEqual(1, x.attr)
        self.assertEqual(1, y.attr)
        self.assertEqual(x, y)
        self.assertEqual(id(x), id(y))

        w = MockSingleton2(1)
        z = MockSingleton2(2)

        self.assertEqual(1, w.attr)
        self.assertEqual(1, z.attr)
        self.assertEqual(w, z)
        self.assertEqual(id(w), id(z))
        self.assertNotEqual(id(w), id(x))

        z.attr = 2

        self.assertEqual(2, z.attr)
        self.assertEqual(2, w.attr)
