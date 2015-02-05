#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#import json
#import time
import unittest
from app150204 import ConvertList150204

class TestApp150204(unittest.TestCase):

    app = None
    rdict = None

    def setUp(self):
        self.app = ConvertList150204()
        self.rdict = self.app.buildDict()

    def test_rdict_none(self):
        self.assertIsNotNone(self.rdict)

    def test_meta_count(self):
        # http://data.gov.tw/data_list
        self.assertEqual(self.rdict['meta']['count'],4245)

if __name__ == "__main__":
    unittest.main()
