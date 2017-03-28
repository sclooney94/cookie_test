# -*- coding: utf-8 -*-

import unittest2
from mock import patch, MagicMock
from realone.realone import print_1_to_10
from StringIO import StringIO

class TestBusinessProcess(unittest2.TestCase):
    """ The goal, or acceptance criteria should be reminded here
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_1_to_100(self, PrintMock):
        print_1_to_10()
        self.assertEqual(PrintMock.getvalue(), '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')