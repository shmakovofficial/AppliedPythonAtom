#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from unittest import mock

from unittest_rm_file_fun import rm


class RmTestCase(unittest.TestCase):

    @mock.patch('unittest_rm_file_fun.os')
    def test_rm(self, mock_os):
        rm("any path")
        mock_os.remove.assert_called_with("any path")
