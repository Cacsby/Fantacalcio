import unittest

from main import main


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_main(self):
        response = main()


