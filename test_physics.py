import unittest
import physics

class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_bouyancy(10, 1000), 98100.0)
        self.assertRaises(ValueError, physics.calculate_bouyancy,-2, 3)
        self.assertRaises(ValueError, physics.calculate_bouyancy,2, -3)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(100,10), True)
        self.assertEqual(physics.will_it_float(5,5000), None)
        self.assertRaises(ValueError, physics.will_it_float,2, -3)
        self.assertRaises(ValueError, physics.will_it_float,-2, 3)

    def test_calculate_pressure(self):
        self.assertAlmostEqual(physics.calculate_pressure(10), 98100)
        self.assertAlmostEqual(physics.calculate_pressure(-10), 98100)
        self.assertNotEqual(physics.calculate_pressure(200), 98100.0)


if __name__ == "__main__":
    unittest.main()

