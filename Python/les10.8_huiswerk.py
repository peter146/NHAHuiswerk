import unittest

class TestsGelijkeWaarden(unittest.TestCase):
    def test_variabele(self):
        x = "huiswerk"
        y = "huiswerk"
        self.assertEqual(x,y)

if __name__=="__main__":
    unittest.main()
