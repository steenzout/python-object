# -*- coding: utf-8 -*-

import unittest

import steenzout.object


class AttributesTestCase(unittest.TestCase):
    """steenzout.object package test cases."""

    def test_version(self):
        """Test version function."""

        self.assertTrue(
            steenzout.object.version() == steenzout.object.__version__
        )
