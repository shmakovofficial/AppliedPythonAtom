#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
import tempfile
import unittest

from unittest_rm_file_fun import rm


class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "w") as f:
            f.write("Delete me!")

    def test_rm(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")
