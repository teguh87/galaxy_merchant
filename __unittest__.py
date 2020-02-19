import unittest

from main import Main

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.trx = Main()
    
    def test_init(self):
        self.trx.process('glob is I prok is V pish is X tegj is L')
        pass