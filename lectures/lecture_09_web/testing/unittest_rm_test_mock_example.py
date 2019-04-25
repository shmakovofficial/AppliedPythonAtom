#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest_rm_file_fun import rm

import unittest
from unittest import mock


class RmTestCase(unittest.TestCase):
    
    @mock.patch('unittest_rm_file_fun.os')
    def test_rm(self, mock_os):
        rm("any path")
        mock_os.remove.assert_called_with("any path")

