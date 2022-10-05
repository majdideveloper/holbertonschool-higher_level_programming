#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

     def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
   
if __name__ == '__main__':
    unittest.main()
