import unittest
import count as count
class TestCalculator(unittest.TestCase):
    def test_int_add(self):
        self.assertEqual(count.add(1, 3), 4)

    def test_int2_add(self):
        self.assertEqual(count.add(7, 2), 9)
	
	def test_float_add(self):
        self.assertEqual(count.add(7.1, 2), 9.1)
		
	def test_float2_add(self):
        self.assertEqual(count.add(1.3, 3), 4.3)
    
    def test_int_copy(self):
        self.assertEqual(count.copy(9), 9)

    def test_float_copy2(self):
        self.assertEqual(count.copy(5.4), 5.4)
		
	def test_float_copy3(self):
        self.assertEqual(count.copy(11.2), 11.2)

if __name__ == '__main__':
    unittest.main()
